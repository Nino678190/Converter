nok = 0.084
sek = 0.086
dkk = 0.13
usd = 0.92
isk = 0.0067
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

def UsdToEur(eingabe):
    output = eingabe * usd
    output = round(output,2)
    print(output)
    frage()

def EurToUsd(eingabe):
    output = (1/usd)*eingabe
    output = round(output,2)
    print(output)
    frage()

def IskToEur(eingabe):
    output = eingabe * isk
    output = round(output,2)
    print(output)
    frage()

def EurToIsk(eingabe):
    output = (1/isk)*eingabe
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
    print("7: USD to Euro")
    print("8: Euro to USD")
    print("9: ISK to Euro")
    print("10: Euro to ISK")
    auswahl = input("Was soll umgerechnet werden?")
    eingabe = float(input("Welche Menge?"))
    try:
        val = float(eingabe)
    except ValueError:
        print("Das ist keine Zahl")
        start()
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
    elif auswahl == '7':
        UsdToEur(eingabe)
    elif auswahl == '8':
        EurToUsd(eingabe)
    elif auswahl == '9':
        IskToEur(eingabe)
    elif auswahl == '10':
        EurToIsk(eingabe)
    else:
        print("ungueltige Eingabe")
        starten()

starten()
