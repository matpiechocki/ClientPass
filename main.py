import re
import string
import random
import os #cls
import winsound
from time import sleep
cls = lambda: print('\n' * 100)

def winSound_Start():
    frequency = 1000
    duration = 100
    winsound.Beep(frequency, duration)
    frequency = 1500
    duration = 100
    winsound.Beep(frequency, duration)
    frequency = 1000
    duration = 100
    winsound.Beep(frequency, duration)
    frequency = 1500
    duration = 100
    winsound.Beep(frequency, duration)
def winSound_Option():
    frequency = 1500
    duration = 100
    winsound.Beep(frequency, duration)
def winSound_Error():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
    frequency = 2000
    duration = 1000
    winsound.Beep(frequency, duration)
    frequency = 1500
    duration = 1000
    winsound.Beep(frequency, duration)
    frequency = 1000
    duration = 1000
    winsound.Beep(frequency, duration)
    frequency = 500
    duration = 1000
    winsound.Beep(frequency, duration)

def CheckPassoword():   #option 1
    passw = input('Write here your password to check quality: ')
    if (len(passw) >= 8):
        print('Password length...OK')
        sleep(1)
        if (re.search(r"[a-z]", passw) is None):
            print('Lowercase...EMPTY !')
            winSound_Error()
            print('Return to menu...')
            sleep(1)
            main_function()
        else:
            print('Lowercase...OK')
            sleep(1)
            if (re.search(r"[A-Z]", passw) is None):
                print('Uppercase...EMPTY !')
                winSound_Error()
                print('Return to menu...')
                sleep(1)
                main_function()
            else:
                print('Uppercase...OK')
                sleep(1)
                if (re.search(r"\d", passw) is None):
                    print('Searching digit...NO DIGIT !')
                    winSound_Error()
                    print('Return to menu...')
                    sleep(1)
                    main_function()
                else:
                    print('Searching digit...OK')
                    sleep(1)
                    if (re.search(r"[ ~`!@#$%^&*()<>,.?+-/[\\\]_{}'|"+r'"]', passw) is None):
                        print('Special characters search...NOT OK')
                        winSound_Error()
                        print('Return to menu...')
                        sleep(1)
                        main_function()
                    else:
                        print('Special characters search...OK')
                        sleep(1)
                        print('Password checked. Password is strong. Return to menu...')
                        winSound_Option()
                        sleep(3)
                        cls()
                        main_function()
    else:
        print('Password length...TOO SHORT !')
        winSound_Error()
        print('Return to menu...')
        sleep(1)
        main_function()
def GeneratorPassword(): #option 2
    choice = input('Start Automatic or Manual [A/M]: ')
    winSound_Option()
    if(choice=='A' or choice=='a'):
        GeneratorPassword_A()
    elif(choice=='M' or choice=='m'):
        GeneratorPassword_M()
    else:
        print('1.GeneratorPassword')
        print('2.Menu')
        choice2 = input('Return to menu or Return to GP options [1-2]: ')
        winSound_Option()
        if(choice2 == '1'):
            GeneratorPassword()
        elif(choice2 == '2'):
            print('Return to menu...')
            sleep(1)
            main_function()
        else:
            print('Wrong option!')
            winSound_Error()
            print('Return to menu...')
            sleep(1)
            main_function()
def GeneratorPassword_A():  #option 2A
    try:
        passwLength = int(input('Password length [8-12]: '))
        winSound_Option()
        #passwLength = int(passwLength)
        if (passwLength >= 8 and passwLength <= 12):
            passwPunctuation = string.punctuation
            #print(passwPunctuation)
            passwPunctuation = passwPunctuation.replace('+', '')
            passwPunctuation = passwPunctuation.replace('-', '')
            passwPunctuation = passwPunctuation.replace('=', '')
            passwPunctuation = passwPunctuation.replace('_', '')
            passwPunctuation = passwPunctuation.replace('`', '')
            passwPunctuation = passwPunctuation.replace('~', '')
            #print(passwPunctuation)
            passwSign = string.ascii_letters + string.digits + passwPunctuation
            #print(passwSign)
            passw = []
            for x in range(passwLength):
                passw.append(random.choice(passwSign))
            print('Generating password...')
            sleep(1)
            print(''.join(passw))
            returnGP = input('Generate Password again [Y/N]: ')
            winSound_Option()
            if (returnGP == 'Y' or returnGP == 'y'):
                print('Return to GeneratorPassword...')
                sleep(1)
                cls()
                GeneratorPassword()
            elif (returnGP == 'N' or returnGP == 'n'):
                print('Return to menu...')
                sleep(1)
                cls()
                main_function()
            else:
                print('Wrong answer!')
                winSound_Error()
                print('Return to menu...')
                sleep(1)
                cls()
                main_function()
        else:
            print('Password length not between <8-12>')
            winSound_Error()
            returnGP = input('Do you want try again [Y/N]: ')
            winSound_Option()
            if (returnGP == 'Y' or returnGP == 'y'):
                print('Return to GeneratorPassword...')
                sleep(1)
                cls()
                GeneratorPassword()
            elif (returnGP == 'N' or returnGP == 'n'):
                print('Return to menu...')
                sleep(1)
                cls()
                main_function()
            else:
                print('Wrong answer!')
                winSound_Error()
                print('Return to menu...')
                sleep(1)
                cls()
                main_function()
    except:
        print('Wrong!')
        winSound_Error()
        print('Return to menu...')
        sleep(1)
        cls()
        main_function()
def GeneratorPassword_M():  #option 2M
    try:
        passwLength = int(input('Password length [8-12]: '))
        winSound_Option()
        if (passwLength <= 12 and passwLength >= 8):
            counter = passwLength
            print('!=0 and <=: ', counter - 4)
            numberUppercase = int(input('How many Uppercase Letters: '))
            winSound_Option()
            if (numberUppercase <= (counter - 4) and numberUppercase != 0):
                print('!=0 and <=: ', counter - (3 + numberUppercase))
                numberDigits = int(input('How many Digits: '))
                winSound_Option()
                if (numberDigits <= (counter - (3 + numberUppercase)) and numberDigits != 0):
                    print('!=0  and <=: ', counter - (2 + numberUppercase + numberDigits))
                    numberSymbols = int(input('How many Symbols: '))
                    winSound_Option()
                    if (numberSymbols <= (counter - (2 + numberUppercase + numberDigits)) and numberSymbols != 0):
                        numberLowercase = int(passwLength - (numberUppercase + numberDigits + numberSymbols))

                        passwUppercase = string.ascii_uppercase
                        passwLowerCase = string.ascii_lowercase
                        passwDigits = string.digits
                        passwSymbols = string.punctuation
                        passwSymbols = passwSymbols.replace('+', '')
                        passwSymbols = passwSymbols.replace('-', '')
                        passwSymbols = passwSymbols.replace('=', '')
                        passwSymbols = passwSymbols.replace('_', '')
                        passwSymbols = passwSymbols.replace('`', '')
                        passwSymbols = passwSymbols.replace('~', '')

                        passwU = []
                        for x in range(numberUppercase):
                            passwU.append(random.choice(passwUppercase))
                        U = (''.join(passwU))
                        passwD = []
                        for x in range(numberDigits):
                            passwD.append(random.choice(passwDigits))
                        D = (''.join(passwD))
                        passwS = []
                        for x in range(numberSymbols):
                            passwS.append(random.choice(passwSymbols))
                        S = (''.join(passwS))
                        passwL = []
                        for x in range(numberLowercase):
                            passwL.append(random.choice(passwLowerCase))
                        L = (''.join(passwL))
                        # print(U+D+S+L)
                        passwPrototype = (U + D + S + L)
                        # print(passwPrototype)
                        passwGeneral = ''.join(random.sample(passwPrototype, len(passwPrototype)))
                        print('Generating password...')
                        sleep(1)
                        print(passwGeneral)
                        returnGP = input('Generation password again [Y/N]: ')
                        winSound_Option()
                        if(returnGP == 'Y' or returnGP == 'y'):
                            print('Return to GeneratorPassword_Manual...')
                            sleep(1)
                            GeneratorPassword_M()
                        elif(returnGP == 'N' or returnGP == 'n'):
                            print('Return to menu...')
                            sleep(1)
                            main_function()
                        else:
                            print('Wrong option!')
                            winSound_Error()
                            print('Return to menu...')
                            sleep(1)
                            main_function()
                    else:
                        print('Wrong symbol length!')
                        winSound_Error()
                        print('Try again...')
                        sleep(1)
                        GeneratorPassword_M()
                else:
                    print('Wrong digit length!')
                    winSound_Error()
                    print('Try again...')
                    sleep(1)
                    GeneratorPassword_M()
            else:
                print('Wrong uppercase length!')
                winSound_Error()
                print('Try again...')
                sleep(1)
                GeneratorPassword_M()
        else:
            print('Wrong password length!')
            winSound_Error()
            print('Try again...')
            sleep(1)
            GeneratorPassword_M()
    except:
        print('Wrong, no int!')
        winSound_Error()
        print('Return to menu...')
        sleep(1)
        main_function()
def SavePassword(): #option 3
    save1 = input('[0] Return to menu \n How many passwords do you want to save? [0-9]: ')
    winSound_Option()
    counter = save1
    counter=int(counter)
    while(counter>0):
        counter = counter-1
        txtFile = open("BasePass.txt","a")
        user = input('Please write username/mail of password: ')
        winSound_Option()
        passw = input('Please write password to save: ')
        winSound_Option()
        account = input('Please write name of place where data are use: ')
        winSound_Option()
        passInfo = 'Username: ',user,'  ||| Password: ', passw,'    ||| Place: ', account, '\n'
        txtFile.writelines(passInfo)
        print('Data password saved!')
        sleep(1)
        txtFile.close()
    else:
        print('Return to menu...')
        sleep(1)
        cls()
        main_function()
def ReadPasswords():    #option 4
    try:
        txtFile = open("BasePass.txt", "r+")
        print('Your Base of Passwords: ')
        print(txtFile.read())
        txtFile.close()
        sleep(5)
        print('Return to menu...')
        sleep(1)
        main_function()
    except:
        print('No BasePass.txt in folder!\nFirst go to 3.SavePassword...')
        sleep(3)
        main_function()
def ExitFunction():    #option 5
    stop=1
    stop=int(stop)
    while(stop==1):
        stop=0


def main_function():
    print('###ClientPass### -> your passwords client!')
    winSound_Start()
    sleep(1)
    print('1. CheckPassword')
    print('2. GeneratorPassword')
    print('3. SavePassword')
    print('4. ReadPasswords')
    print('5. Exit ClientPass')
    option = 0
    try:
        option = input('Choose option [1-5]: ')
        option = int(option)
        if (option == 1):
            winSound_Option()
            cls()
            print('CheckPassword loading...')
            sleep(2)
            cls()
            CheckPassoword()
        elif (option == 2):
            winSound_Option()
            cls()
            print('GeneratorPassword loading...')
            sleep(2)
            cls()
            GeneratorPassword()
        elif (option == 3):
            winSound_Option()
            cls()
            print('SavePassword loading...')
            sleep(2)
            cls()
            SavePassword()
        elif (option == 4):
            winSound_Option()
            cls()
            print('ReadPassword loading...')
            sleep(2)
            cls()
            ReadPasswords()
        elif (option == 5):
            winSound_Option()
            cls()
            print('ClientPass exiting...')
            sleep(2)
            winSound_Start()
            cls()
            ExitFunction()
        else:
            cls()
            print('Wrong number option!')
            winSound_Error()
            print('Try again...')
            sleep(1)
            cls()
            main_function()
    except:
        cls()
        print('Wrong option!')
        winSound_Error()
        print('Try again...')
        sleep(1)
        cls()
        main_function()
main_function()
