#EINLOGGEN
enter = input("Passwort eingeben:\n")
enter = str(enter)

Password = False
if enter == "1418":
    Password = True
    print("Eingegebenes Passwort ist richtig.")
if enter != "1418":
    print("Passwort falsch.")

accounts = {
    "Eintrag1": "\n info1 id 0",
    "Eintrag2": "\n info2 id 1",
    "Eintrag3": "\n info3 id 2",
    "Eintrag4": "\n info4 id 3",
    "Eintrag5": "\n info5 id 4",
    "Eintrag6": "\n info6  id 5",
    "Eintrag7": "\n info7 id 6",
    "Eintrag8": "\n info8 id 7",
    "l": "\n Eintrag1: info1 id 0 \n Eintrag2: info2 id 1 \n Eintrag3: info3 id 2 \n Eintrag4: info4 id 3 \n Eintrag5: info5 id 4 \n Eintrag6: info6 id 5 \n Eintrag7: info7 id 6 \n Eintrag8: info8 id 7"
}


    #EINGABEN

if Password:
    chooseaccount = input("\nNach Account suchen oder 'L' eingeben für ganze Liste: ").lower()

    if chooseaccount in accounts:
        print(accounts[chooseaccount])
    else:
        print("Ungültige Eingabe. Schließen Sie das Programm und versuchen Sie es nochmal.")

#ENDE      
input("\nDrücken Sie die Enter Taste, um das Fenster zu schließen. ")
