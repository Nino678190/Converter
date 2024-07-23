nok = 0.085
sek = 0.084
dkk = 0.12
#eingabe = 100

def frage():
    nochmal = input("Nochmal y or n:")
    if nochmal == 'y':
        starten()
    else:
        exit()

def NokToEur(eingabe):
    output = eingabe * nok
    output = round(output,2)
    print(output)
    frage()

def SekToEur(eingabe):
    output = eingabe * sek
    output = round(output,2)
    print(output)
    frage()

def DkkToEur(eingabe):
    output = eingabe * dkk
    output = round(output,2)
    print(output)
    frage()

def EurToDkk(eingabe):
    output = (1/dkk)*eingabe
    output = round(output,2)
    print(output)
    frage()

def EurToSek(eingabe):
    output = (1/sek)*eingabe
    output = round(output,2)
    print(output)
    frage()

def EurToNok(eingabe):
    output = (1/nok)*eingabe
    output = round(output,2)
    print(output)
    frage()

#NokToEur(eingabe)

def starten():
    print("1: NOK to Euro")
    print("2: SEK to Euro")
    print("3: DKK to Euro")
    print("4: Euro to DKK")
    print("5: Euro to SEK")
    print("6: Euro to NOK")
    auswahl = input("Was soll umgerechnet werden?")
    eingabe = int(input("Welche Menge?"))
    if auswahl == '1':
        NokToEur(eingabe)
    elif auswahl == '2':
        SekToEur(eingabe)
    elif auswahl == '3':
        DkkToEur(eingabe)
    elif auswahl == '4':
        EurToDkk(eingabe)
    elif auswahl == '5':
        EurToSek(eingabe)
    elif auswahl == '6':
        EurToNok(eingabe)
    else:
        print("ungueltige Eingabe")
        starten()

starten()
