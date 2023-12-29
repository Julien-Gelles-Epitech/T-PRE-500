import random, sys, time
from tkinter import *

word_list=[]

def manageWordsFile(f):
    fichier = open(f, "r")
    line = fichier.readline()
    while len(line)>0:
        line = line.replace("\n", "")
        word_list.append(line) 
        line = fichier.readline()
    fichier.close()

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
        size4=len(2*lettersGiven)+12
        if points>9:plus5=2
        elif points<2:plus5=0
        else:plus5=1
        if easyMode:size5=plus5+31
        else:size5=plus5+19
        if wordValue(superSecretWord)>9:size3=25
        else:size3=24
        size6=16
        if duration>9:size6+=1
        if duration>99:size6+=1
        if duration>999:size6+=1
        maximum=max(size1, size3, size4, size5)
        
        print("┌───"+(maximum*"─")+"┐")
        print("│", superSecretWord+": correct guess",(maximum-size1)*" ","│")
        print("│", "Congratulations !",(maximum-17)*" ","│")
        print("│ Word score difficulty:", wordValue(superSecretWord), (maximum-size3)*" ","│")
        print("│", "Your guess: ", *lettersGiven,(maximum-size4)*" ","│")

        msg = "│ Your score: "+str(points)
        if points>1:msg+=" points"
        else:msg+=" point"
        if easyMode:msg+=" (easy mode)"
        print(msg,(maximum-size5)*" ","│")

        print("│ Your time:",str(format(duration, '.2f'))+"s",(maximum-size6)*" ","│")
        if record:print("│ *-!-!-New Record-!-!-*",(maximum-22)*" ", "│")
        print("└───"+(maximum*"─")+"┘")
        
def forcePoints(num):
    points+=num

def manageScores():
    bestScores={}
    record=False
    fichier = open("score.txt", "r")
    line = fichier.readline()
    while len(line)>0:
        line = line.replace("\n", "")
        score = line.split(':')
        bestScores[score[0]]=int(score[1])
        line = fichier.readline()
    fichier.close()
    if str(wordValue(superSecretWord)) in bestScores and bestScores[str(wordValue(superSecretWord))]>points:
        record=True
    if easyMode:
        bestScores[str(wordValue(superSecretWord))+"e"]=points
    else:
        bestScores[str(wordValue(superSecretWord))]=points
    fichier = open("score.txt", "w")
    for score in bestScores:
        fichier.write(score+":"+str(bestScores[score])+"\n")
    fichier.close()
    return record


letterValue = {'A':1,
               'B':3,
               'C':3,
               'D':2,
               'E':1,
               'F':4,
               'G':2,
               'H':4,
               'I':1,
               'J':8,
               'K':5,
               'L':1,
               'M':3,
               'N':1,
               'O':1,
               'P':3,
               'Q':10,
               'R':1,
               'S':1,
               'T':1,
               'U':1,
               'V':4,
               'W':4,
               'X':8,
               'Y':4,
               'Z':10
               }

def wordValue(word):
    score=0
    letters=""
    for letter in word:
        letter = letter.upper()
        if letter not in letters:
            score+=letterValue[letter]

        letters+=letter
    return score


if __name__ == '__main__':

    modes = ['-e', '-E']
    cheat = ['-c', '-C']
    french = ['-fr','-FR']
    graphic = ['-g', '-G']

    if len(list(set(graphic) & set(sys.argv)))>0:
        window = Tk()
        window.title("Window")
        window.geometry("1600x900")

        canvas = Canvas(window, height=900, width=1600)
        canvas.pack()

        canvas.create_rectangle(55,5,1545,840, fill="#a67532", outline="#584a1b", width=5)
        canvas.create_rectangle(125,75,1475,770, fill="#4d7536", outline="#584a1b", width=5)
        canvas.create_rectangle(5,840,1595,895, fill="#8d5e2a", outline="#584a1b", width=5)
        canvas.create_rectangle(200,810,330,835, fill="#292826", outline="#292826", width=5)
        canvas.create_line(196,810,335,810, width=10, fill="#871715")
        canvas.create_line(100,835,150,835, width=5, fill="#f3f4f8")
        canvas.create_line(400,835,465,835, width=5, fill="#f3f4f8")
        canvas.create_line(475,835,500,835, width=5, fill="#f3f4f8")

        # def switch(i):
        #     btnL[i-1].configure(bg="red", fg="yellow")
        #     print(i-1)
        
        # def makeButton(n,x,y,i): 
        #     btn = Button(window, text =n, command=switch(i), background='#4d7536', foreground="#f3f4f8", font=('Helvetica 20 bold'), activeforeground='#4d7536', highlightthickness=0, activebackground='#f3f4f8', width=10, height=3)
        #     btn.pack()
        #     btn.place(x=x,y=y)
        #     return btn
        
        # btnL=[]
        # btn1=makeButton("Easy",1200,200,0)
        # btnL.append(btn1)
        # btn2=makeButton("Normal",1200,300,1)
        # btnL.append(btn2)
        # btn3=makeButton("Fr",1200,400,3)
        # btnL.append(btn3)
        # btn4=makeButton("En",1200,500,4)
        # btnL.append(btn4)
        # btn5=makeButton("Play",1200,600,5)
        # btnL.append(btn5)

        window.after(5000, window.destroy)
        window.mainloop()
    else:

        if len(list(set(french) & set(sys.argv)))>0:
            manageWordsFile("hangmanWordListFR.txt")
        else:
            manageWordsFile("hangmanWordList.txt")
        
        superSecretWord = randomWord(word_list)
        if len(list(set(cheat) & set(sys.argv)))>0:
            print(superSecretWord)

        gameStatus = True
        lettersGiven = []
        points = 0
        record=False

        if len(list(set(modes) & set(sys.argv)))>0:
            easyMode = True
            wordStatus = easyWordInit()
        else:
            easyMode = False
            wordStatus = wordInit()

        startingTime = time.time()
        while gameStatus:
            displayGame()
            inputStr = inputLetter()
            checkRes = inputCheck()
            newWord = checkRes[0]
            points+=checkRes[1]
            wordStatus = newWord
            gameStatus = checkEnd()

        duration = time.time() - startingTime
        record = manageScores()
        displayEnd()
    

    
    
