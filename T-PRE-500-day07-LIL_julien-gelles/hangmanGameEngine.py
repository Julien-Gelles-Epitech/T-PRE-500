import random, sys
from hangmanWordList import *
from hangmanWordListFR import *

def randomWord(list):
    randomRange = len(list)-1
    randomNumber = random.randint(0,randomRange)
    return list[randomNumber].upper()

def easyWordInit():
    word = ""
    numberReveal = len(superSecretWord)//2
    randomLettersIndex = random.sample(range(1, len(superSecretWord)), numberReveal)
    for i in range(len(superSecretWord)):
        if i in randomLettersIndex:
            word+=superSecretWord[i]+" "
        else:
            word+="_ "
    return word+"/"
    

def wordInit():
    word = ""
    for caractere in superSecretWord:
        word+="_ "
    return word+"/"

def revealWord():
    word = ""
    for caractere in superSecretWord:
        word+=caractere+" "
    return word+"/"

def correctInput(inputStr):
    if len(inputStr)==0:
        return False
    else:
        return inputStr.isalpha()

def inputLetter():
    inputStr = input("-> ")
    while not correctInput(inputStr):
        inputStr = input("-> ")
    return inputStr.upper()

def allIndex(caractere, word):
    return [i for i in range(len(word)) if word[i]==caractere]

def replaceCaractere(caractere, word, index):
    wordList = list(word)
    wordList[index] = caractere
    newWord = "".join(wordList)
    return newWord

def inputCheck():
    newWord = wordStatus
    point = 0
    if len(inputStr) == 1:
        if easyMode and inputStr in lettersGiven:
            print("Letter already given.")
        else:
            if inputStr in lettersGiven:
               point = 1 
            else:
                index = allIndex(inputStr, superSecretWord)
                if len(index) == 0:
                    point = 1
                for i in index:
                    newWord = replaceCaractere(inputStr, newWord, 2*i)
                lettersGiven.append(inputStr)
    else:
        if inputStr == superSecretWord:
            newWord = revealWord()
        else:
            point = 1
    return (newWord, point)

def checkEnd():
    return ('_' in wordStatus) 



def displayGame():
    display = wordStatus+" "+str(points)
    if points>1:
        display+=" points\n"
    else:
        display+=" point\n"
    print(display)

def displayEnd():
        size1=len(superSecretWord)+15
        size2=17
        size3=len(2*lettersGiven)+12
        if points>9:plus4=2
        elif points<2:plus4=0
        else:plus4=1
        if easyMode:size4=plus4+31
        else:size4=plus4+19
        maximum=max(size1, size2, size3, size4)
        
        print("┌───"+(maximum*"─")+"┐")
        print("│", superSecretWord+": correct guess",(maximum-size1)*" ","│")
        print("│", "Congratulations !",(maximum-size2)*" ","│")
        print("│", "Your guess: ", *lettersGiven,(maximum-size3)*" ","│")
        msg = "│ Your score: "+str(points)
        if points>1:
            msg+=" points"
        else:
            msg+=" point"
        if easyMode:
            msg+=" (easy mode)"
        print(msg,(maximum-size4)*" ","│")
        print("└───"+(maximum*"─")+"┘")
        

def forcePoints(num):
    points+=num


if __name__ == '__main__':

    lang = ['-fr', '-FR']
    if len(list(set(lang) & set(sys.argv)))>0:
        superSecretWord = randomWord(word_listFR)
    else:
        superSecretWord = randomWord(word_list)

    gameStatus = True
    lettersGiven = []
    points = 0

    modes = ['-easy', '-EASY', '-e', '-E']

    if len(list(set(modes) & set(sys.argv)))>0:
        easyMode = True
        wordStatus = easyWordInit()
    else:
        easyMode = False
        wordStatus = wordInit()

    while gameStatus:
        displayGame()
        inputStr = inputLetter()
        checkRes = inputCheck()
        newWord = checkRes[0]
        points+=checkRes[1]
        wordStatus = newWord
        gameStatus = checkEnd()

    displayEnd()

    
    
