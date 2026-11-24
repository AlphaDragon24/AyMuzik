import sys as Renox300, subprocess as Renox301, importlib as Renox302

def Renox303(Renox304, Renox305=None):
    try:
        Renox302.import_module(Renox304)
    except ImportError:
        try:
            Renox301.run([Renox300.executable, "-m", "pip", "install", Renox305 or Renox304], check=True)
        except Exception:
            pass

for Renox307, Renox308 in [("httpx", "httpx[http2]"), ("kivy", "kivy")]:
    Renox303(Renox307, Renox308)

from kivy.app import App as Renox1
from kivy.clock import Clock as Renox2
from kivy.metrics import dp as Renox3
from kivy.uix.floatlayout import FloatLayout as Renox94
from kivy.uix.boxlayout import BoxLayout as Renox4
from kivy.uix.anchorlayout import AnchorLayout as Renox5
from kivy.uix.label import Label as Renox6
from kivy.uix.button import Button as Renox7
from kivy.uix.behaviors import ButtonBehavior as Renox85
from kivy.uix.textinput import TextInput as Renox107
from kivy.graphics import Color as Renox8, RoundedRectangle as Renox9, Line as Renox10, Rectangle as Renox12
from kivy.graphics.texture import Texture as Renox13
from kivy.core.window import Window as Renox11
import webbrowser as Renox79, httpx as Renox110, json as Renox111, threading as Renox112

class Renox400(Renox94):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Renox401 = Renox13.create(size=(1, 4), colorfmt='rgba')
        Renox402 = b''
        for Renox403 in [(18,10,38), (36,14,66), (12,20,60), (6,8,26)]:
            Renox402 += bytes([Renox403[0], Renox403[1], Renox403[2], 255])
        Renox401.blit_buffer(Renox402, colorfmt='rgba', bufferfmt='ubyte')
        Renox401.wrap = 'clamp_to_edge'
        with self.canvas.before:
            Renox8(1,1,1,1)
            self.Renox404 = Renox12(texture=Renox401, pos=self.pos, size=self.size)
            self.Renox405 = Renox8(0.55, 0.30, 1.0, 0.20)
            self.Renox406 = Renox9(pos=(0,0), size=(Renox3(320), Renox3(320)), radius=[Renox3(160)])
            self.Renox407 = Renox8(0.20, 0.55, 1.0, 0.16)
            self.Renox408 = Renox9(pos=(0,0), size=(Renox3(300), Renox3(300)), radius=[Renox3(150)])
        self.bind(pos=self.Renox409, size=self.Renox409)

    def Renox409(self, *Renox410):
        self.Renox404.pos = self.pos
        self.Renox404.size = self.size
        self.Renox406.pos = (self.width - Renox3(200), self.height - Renox3(180))
        self.Renox408.pos = (-Renox3(120), -Renox3(120))

class Renox17(Renox7):
    def __init__(self, Renox19, Renox20, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0,0,0,0)
        self.Renox19 = Renox19
        self.Renox20 = Renox20
        with self.canvas.before:
            self.Renox113 = Renox8(*Renox19)
            self.Renox21 = Renox9(pos=self.pos, size=self.size, radius=[Renox3(18)])
        with self.canvas.after:
            self.Renox114 = Renox8(*Renox20)
            self.Renox22 = Renox10(rounded_rectangle=(self.x,self.y,self.width,self.height,Renox3(18)), width=1.4)
        self.bind(pos=self.Renox23, size=self.Renox23)

    def Renox23(self, *Renox24):
        self.Renox21.pos = self.pos
        self.Renox21.size = self.size
        self.Renox22.rounded_rectangle = (self.x,self.y,self.width,self.height,Renox3(18))

    def Renox76(self, Renox77, Renox78):
        self.Renox113.rgba = Renox77
        self.Renox114.rgba = Renox78

class Renox82(Renox85, Renox6):
    pass

class Renox200(Renox4):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.Renox203 = Renox8(1, 1, 1, 0.06)
            self.Renox201 = Renox9(pos=self.pos, size=self.size, radius=[Renox3(18)])
            self.Renox204 = Renox8(0.60, 0.45, 1.0, 0.55)
            self.Renox202 = Renox10(rounded_rectangle=(self.x,self.y,self.width,self.height,Renox3(18)), width=1.3)
        self.bind(pos=self.Renox205, size=self.Renox205)

    def Renox205(self, *Renox206):
        self.Renox201.pos = self.pos
        self.Renox201.size = self.size
        self.Renox202.rounded_rectangle = (self.x,self.y,self.width,self.height,Renox3(18))

class Renox220(Renox4):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.Renox223 = Renox8(1, 1, 1, 0.05)
            self.Renox221 = Renox9(pos=self.pos, size=self.size, radius=[Renox3(24)])
            self.Renox224 = Renox8(1, 1, 1, 0.10)
            self.Renox222 = Renox10(rounded_rectangle=(self.x,self.y,self.width,self.height,Renox3(24)), width=1.2)
        self.bind(pos=self.Renox225, size=self.Renox225)

    def Renox225(self, *Renox226):
        self.Renox221.pos = self.pos
        self.Renox221.size = self.size
        self.Renox222.rounded_rectangle = (self.x,self.y,self.width,self.height,Renox3(24))

class Renox210(Renox107):
    def Renox211(self, *Renox212):
        Renox213 = self.line_height if self.line_height else self.font_size
        Renox214 = max((self.height - Renox213) / 2.0, 0)
        self.padding = [0, Renox214, 0, Renox214]

class Renox18(Renox1):
    def build(self):
        Renox11.clearcolor = (0.03, 0.02, 0.09, 1)
        Renox36 = Renox400()

        Renox40 = Renox5(anchor_x='center', anchor_y='center')

        Renox230 = Renox220(orientation='vertical', padding=[Renox3(24), Renox3(26), Renox3(24), Renox3(26)], spacing=Renox3(16))
        Renox230.size_hint = (0.88, None)
        Renox230.bind(minimum_height=Renox230.setter('height'))

        Renox38 = Renox6(text='Instagram Reset', font_size='27sp', bold=True, color=(1,1,1,1), halign='center', valign='middle', size_hint_y=None, height=Renox3(42))
        Renox230.add_widget(Renox38)

        Renox207 = Renox200(orientation='horizontal', size_hint_y=None, height=Renox3(56))
        self.Renox115 = Renox210(
            hint_text='Email Or Username...',
            hint_text_color=(0.70,0.68,0.85,1),
            foreground_color=(1,1,1,1),
            cursor_color=(0.65,0.45,1,1),
            background_normal='',
            background_active='',
            background_color=(0,0,0,0),
            font_size='17sp',
            halign='center',
            multiline=False
        )
        self.Renox115.bind(height=self.Renox115.Renox211, size=self.Renox115.Renox211)
        Renox207.add_widget(self.Renox115)
        Renox230.add_widget(Renox207)

        self.Renox119 = Renox17(
            Renox19=(0.55, 0.20, 0.95, 0.85),
            Renox20=(0.80, 0.55, 1.0, 0.9),
            text='Send Reset',
            font_size='20sp',
            bold=True,
            color=(1,1,1,1),
            size_hint_y=None,
            height=Renox3(56)
        )
        self.Renox119.bind(on_press=self.Renox120)
        Renox230.add_widget(self.Renox119)

        self.Renox121 = Renox6(
            text='',
            font_size='13sp',
            color=(1,1,1,0.85),
            halign='center',
            valign='top',
            size_hint_y=None,
            height=Renox3(0)
        )
        self.Renox121.bind(width=lambda i, v: setattr(i, 'text_size', (v, None)))
        self.Renox121.bind(texture_size=lambda i, v: setattr(i, 'height', v[1]))
        Renox230.add_widget(self.Renox121)

        Renox86 = Renox4(orientation='vertical', spacing=Renox3(2), size_hint_y=None, height=Renox3(58))
        Renox83 = Renox6(text='Developer By', font_size='13sp', color=(1,1,1,0.4), halign='center', valign='middle', size_hint_y=None, height=Renox3(20))
        Renox84 = Renox82(text='@RenoxPy', font_size='18sp', bold=True, color=(0.55,0.55,1.0,1.0), halign='center', valign='middle', size_hint_y=None, height=Renox3(38))
        Renox84.bind(on_press=self.Renox80)
        Renox86.add_widget(Renox83)
        Renox86.add_widget(Renox84)
        Renox230.add_widget(Renox86)

        Renox40.add_widget(Renox230)
        Renox36.add_widget(Renox40)

        return Renox36

    def Renox120(self, Renox123):
        Renox124 = self.Renox115.text.strip()
        if not Renox124:
            self.Renox121.text = 'Enter email or username'
            self.Renox121.color = (1,0.5,0.5,1)
            return
        self.Renox119.disabled = True
        self.Renox119.Renox76((0.85, 0.60, 0.15, 0.85), (1.0, 0.82, 0.30, 0.9))
        self.Renox121.text = 'Sending...'
        self.Renox121.color = (1,1,1,0.85)
        Renox112.Thread(target=self.Renox125, args=(Renox124,), daemon=True).start()

    def Renox138(self, Renox139):
        try:
            Renox140 = Renox139.get("message")
            if isinstance(Renox140, list):
                Renox140 = " ".join(str(x) for x in Renox140)
            if not Renox140:
                Renox140 = Renox139.get("title") or Renox139.get("status") or str(Renox139)
            return str(Renox140).strip()
        except:
            return str(Renox139)

    def Renox125(self, Renox126):
        try:
            Renox127 = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
            Renox128 = {
                "email_or_username": Renox126,
                "flow": "fxcal"
            }
            Renox129 = {
                "User-Agent": "Android",
                "x-csrftoken": "missing",
                "accept-language": "en-US,en;q=0.9"
            }
            with Renox110.Client(http2=True, headers=Renox129, timeout=15) as Renox130:
                Renox131 = Renox130.post(Renox127, data=Renox128)
                Renox132 = Renox131.status_code
                try:
                    Renox133 = self.Renox138(Renox131.json())
                except:
                    Renox133 = Renox131.text
                Renox133 = Renox133[:200]
            Renox2.schedule_once(lambda dt: self.Renox134(Renox132, Renox133), 0)
        except Exception as Renox135:
            Renox2.schedule_once(lambda dt: self.Renox134(0, str(Renox135)[:200]), 0)

    def Renox134(self, Renox136, Renox137):
        self.Renox119.disabled = False
        self.Renox119.Renox76((0.55, 0.20, 0.95, 0.85), (0.80, 0.55, 1.0, 0.9))
        if Renox136 == 200:
            self.Renox121.text = Renox137 or 'Request sent'
            self.Renox121.color = (0.55,1,0.65,1)
        else:
            self.Renox121.text = Renox137
            self.Renox121.color = (1,0.55,0.55,1)

    def Renox80(self, Renox81):
        try:
            Renox79.open('https://t.me/RenoxPy')
        except:
            pass

if __name__ == '__main__':
    Renox18().run()
