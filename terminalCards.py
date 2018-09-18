import pickle
from random import randint
import os.path

if os.path.isfile('mypickle.pk1'):
    pass
else:
    newfile = open('mypickle.pk1','w+')
    flashCards = []

pickleFile = open('mypickle.pk1', 'rb')
try:
    flashCards = pickle.load(pickleFile)
except EOFError:
    print('List is empty...')
pickleFile.close()

def getInput():
    while True:
        try:
            userSelection = int(input( '1: Study flash cards\n' +
                                       '2: Create flash card\n'
                                       '3: Delete flash card\n'
                                       '4: To quit.\n' ))
            while userSelection > 4:
                print('Please enter valid option 1 , 2 or 3!!')
                userSelection = int(input( '1: Study flash cards\n' +
                                           '2: Create flash card\n'
                                           '3: Delete flash card\n'
                                           '4: To quit.\n' ))
            break
        except ValueError:
            print('Please enter 1 , 2 , 3 or 4!')

    return userSelection

def delFlashCard():
    while True:
        for i in range(0, len(flashCards)):
            print(i, flashCards[i])
        while True:
            try:
                delIndex = int(input('Enter card index to delete '))
                while delIndex not in range(0, len(flashCards)):
                    print('enter valid number!')
                    delIndex = int(input('Enter card index to delete '))
                break
            except (IndexError, ValueError) as e:
                print('Please valid number!')

        del flashCards[delIndex]
        for i in range(0, len(flashCards)):
            print(i, flashCards[i])

        output = open('mypickle.pk1', 'wb')
        pickle.dump(flashCards, output)
        output.close()
        while True:
            ans = (input('Delete more cards yes or no? \n')).lower()
            while not ans == 'yes' and not ans == 'no':
                print('Enter valid response!!')
                ans = (input('Delete more cards yes or no? \n')).lower()
            break

        if ans == 'no':
            break

def makeFlashCard():
    i = randint(0, 1000000000)
    name =''
    ans = input("Press ENTER to begin.\nType 'q' to quit making flash cards.\n")
    while ans != 'q':
        name = 'f' + str(i)
        name = []
        while True:
            f = input('Enter front of card: ')
            while f == '':
                print('Please enter something!!')
                f = input('Enter front of card: ')

            b = input('Enter back of card: ')
            while b == '':
                print('Please enter something!!')
                b = input('Enter back of card: ')
            break

        name.append(f)
        name.append(b)
        flashCards.append(name)
        ans = input("Press enter to make another card\nType 'q' to quit making flash cards.\n")

        output = open('mypickle.pk1', 'wb')
        pickle.dump(flashCards, output)
        output.close()




print('**************************************')
print('Welcome to Terminal Flash Cards')
print('**************************************')
print('Enter number to select the option.\n')
userSelection = getInput()

while userSelection != 4:
    if userSelection == 1:
        if flashCards == []:
            print('You do not have any flash cards yet :( \n')
            userSelection = getInput()
            print('\n')
        else:
            for i in range(0, len(flashCards)):
                for z in range(0, len(flashCards[i])):
                    if z == 1:
                        print('----------------------------------------------------')
                        print(flashCards[i][z] + '\n')
                        print('----------------------------------------------------')
                        input('Press enter to see next card...\n')
                    else:
                        print('----------------------------------------------------')
                        print(flashCards[i][z] + '\n')
                        print('----------------------------------------------------')
                        input('Press enter to flip card...\n')
            userSelection = getInput()
    elif userSelection == 2:
        makeFlashCard()
        userSelection = getInput()
    elif userSelection == 3:
        while True:
            if flashCards == []:
                print('You do not have any flash cards to delete yet :( \n')
                userSelection = getInput()
            else:
                delFlashCard()
                break
        userSelection = getInput()

print('*+**+**+**+**+**+**+**+**+**+**+**+**+**+\n-----------------Goodbye-----------------')
