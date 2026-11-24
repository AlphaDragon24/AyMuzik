import asyncio
import logging
from collections import defaultdict
from telegram import Update, InputMediaPhoto, InputMediaVideo
from telegram.error import RetryAfter, TimedOut, Forbidden, BadRequest
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7962500361:AAGWyFEQNfD7iJp2Joic-MGFvAftWQjiVmA"
OWNER_IDS = {7523877985, 7948966404}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Global durumlar
state = type("State", (), {"is_running": False, "stop_requested": False})()
media_groups = defaultdict(list)
media_group_timers = {}
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in OWNER_IDS:
        return
    await update.message.reply_text(
        "**Toplu Medya Basıcı Aktif 🔥**\n\n"
        "Tek medya ya da albüm (toplu fotoğraf/video) at, sonra\n"
        "/bas ile başlat."
    )

async def collect_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in OWNER_IDS:
        return

    if state.is_running:
        await update.message.reply_text("İşlem devam ediyor, /dur yaz.")
        return

    msg = update.message
    uid_str = str(user_id)

    # Tek medya durumu
    if not msg.media_group_id:
        if msg.photo or msg.video or msg.document:
            user_data[uid_str] = {
                "media_type": "single",
                "msg": msg
            }
            await msg.reply_text(
                "**Tek medya alındı**\n\n"
                "Hedef grup ID yaz\nÖrnek: /bas -1001234567890"
            )
        return

    # Albüm toplama
    group_id = msg.media_group_id
    media_groups[group_id].append(msg)

    # Önceki timer varsa iptal et
    if group_id in media_group_timers:
        media_group_timers[group_id].cancel()

    async def process_album(gid):
        await asyncio.sleep(3.0)  # 3 saniye bekle – genelde yeterli olur
        if gid not in media_groups:
            return

        album_messages = media_groups.pop(gid, [])
        if not album_messages:
            return

        # Aynı kullanıcıdan mı kontrolü
        if album_messages[0].from_user.id != user_id:
            return

        media_list = []
        caption = None

        # Mesajları message_id sırasına göre sırala
        for m in sorted(album_messages, key=lambda x: x.message_id):
            if m.caption:
                caption = m.caption  # son caption'ı kullan (genelde ilk olur)

            if m.photo:
                media_list.append(
                    InputMediaPhoto(
                        media=m.photo[-1].file_id,
                        caption=caption if not media_list else None
                    )
                )
            elif m.video:
                media_list.append(
                    InputMediaVideo(
                        media=m.video.file_id,
                        caption=caption if not media_list else None
                    )
                )

        if not media_list:
            await msg.reply_text("Albümde geçerli fotoğraf/video bulunamadı.")
            return

        user_data[uid_str] = {
            "media_type": "album",
            "album": media_list,
            "count": len(media_list)
        }

        await msg.reply_text(
            f"**Albüm toplandı** — {len(media_list)} medya\n\n"
            "Hedef grup ID yaz → Örnek: /bas -1001234567890"
        )

        # Timer temizle
        if gid in media_group_timers:
            del media_group_timers[gid]

    # Yeni timer başlat
    media_group_timers[group_id] = context.application.create_task(
        process_album(group_id)
    )

async def bas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in OWNER_IDS:
        return

    uid_str = str(user_id)
    if uid_str not in user_data or "media_type" not in user_data[uid_str]:
        await update.message.reply_text("Önce medya veya albüm at!")
        return

    args = context.args
    if len(args) != 1:
        await update.message.reply_text("Kullanım: /bas -1001234567890")
        return

    try:
        target = int(args[0])
        user_data[uid_str]["target_group_id"] = target
        user_data[uid_str]["awaiting_delay"] = True
        await update.message.reply_text(
            f"Hedef grup: {target}\n\n"
            "**Kaç saniyede bir atayım?**\n"
            "Örnek: 1.2   veya   2\n"
            "(0.8'den düşük flood ban yedirebilir)"
        )
    except ValueError:
        await update.message.reply_text("Geçersiz grup ID!")

async def handle_delay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in OWNER_IDS:
        return

    uid_str = str(user_id)
    if uid_str not in user_data or not user_data[uid_str].get("awaiting_delay"):
        return

    text = update.message.text.strip()
    try:
        delay = max(float(text), 1.0)  # 1 saniye altı riskli
        user_data[uid_str]["delay"] = delay
        user_data[uid_str]["awaiting_delay"] = False
        state.is_running = True
        state.stop_requested = False

        target = user_data[uid_str]["target_group_id"]
        media_info = f"Albüm ({user_data[uid_str]['count']} adet)" if user_data[uid_str]["media_type"] == "album" else "Tek medya"

        await update.message.reply_text(
            f"**Bot başlıyor**\n"
            f"Grup: {target}\n"
            f"{media_info}\n"
            f"Hız: her {delay} saniye\n\n"
            f"/dur → durdur"
        )

        context.application.create_task(spam_task(context, user_id))

    except ValueError:
        await update.message.reply_text("Geçerli bir sayı gir (örnek: 1.2)")

async def spam_task(context: ContextTypes.DEFAULT_TYPE, owner_id: int):
    uid_str = str(owner_id)
    if uid_str not in user_data:
        state.is_running = False
        return

    data = user_data[uid_str]
    target = data["target_group_id"]
    delay = data["delay"]
    sent = 0

    try:
        if data["media_type"] == "album":
            media = data["album"]

            while not state.stop_requested:
                try:
                    await context.bot.send_media_group(chat_id=target, media=media)
                    sent += 1
                except RetryAfter as e:
                    await asyncio.sleep(e.retry_after + 2)
                except (TimedOut, Forbidden, BadRequest) as e:
                    logger.warning(f"send_media_group geçici hata: {e}")
                    await asyncio.sleep(6)
                except Exception as e:
                    logger.error(f"send_media_group beklenmeyen hata: {e}")
                    break
                await asyncio.sleep(delay)

        else:  # single
            msg = data["msg"]
            send_func = None
            kwargs = {"chat_id": target, "caption": msg.caption}

            if msg.photo:
                kwargs["photo"] = msg.photo[-1].file_id
                send_func = context.bot.send_photo
            elif msg.video:
                kwargs["video"] = msg.video.file_id
                send_func = context.bot.send_video
            elif msg.document:
                kwargs["document"] = msg.document.file_id
                send_func = context.bot.send_document

            if not send_func:
                await context.bot.send_message(owner_id, "Desteklenmeyen medya türü!")
                return

            while not state.stop_requested:
                try:
                    await send_func(**kwargs)
                    sent += 1
                except RetryAfter as e:
                    await asyncio.sleep(e.retry_after + 2)
                except (TimedOut, Forbidden, BadRequest):
                    await asyncio.sleep(6)
                except Exception as e:
                    logger.error(str(e))
                    break
                await asyncio.sleep(delay)

        status = "Durduruldu" if state.stop_requested else "Bitti"
        await context.bot.send_message(
            owner_id,
            f"**{status}**\nToplam {sent} kez gönderildi."
        )

    except Exception as e:
        logger.exception("Spam task genel hata")
        await context.bot.send_message(owner_id, f"Hata oluştu: {str(e)}")
    finally:
        state.is_running = False
        state.stop_requested = False
        if uid_str in user_data:
            del user_data[uid_str]

async def dur(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in OWNER_IDS:
        return
    if not state.is_running:
        await update.message.reply_text("Zaten çalışan bir işlem yok.")
        return

    state.stop_requested = True
    await update.message.reply_text("Durduruluyor... (biraz bekleyebilir)")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bas", bas))
    app.add_handler(CommandHandler("dur", dur))

    # Medya handler'ları
    app.add_handler(MessageHandler(
        filters.PHOTO | filters.VIDEO | filters.Document.ALL,
        collect_media
    ))

    # Delay girişi için (sayı girildiğinde)
    app.add_handler(MessageHandler(
        filters.TEXT| filters.COMMAND,
        handle_delay
    ))

    print("Toplu Medya Botu başladı")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
