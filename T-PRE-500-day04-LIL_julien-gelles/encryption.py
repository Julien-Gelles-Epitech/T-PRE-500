import sys

#Task01
def encrypt():
    s=input("Text to encrypt :  ")
    n=input("Shift :  ")
    while not n.isnumeric():
        n = input("Shift (int):  ")
    res=""
    n=int(n)
    for c in s:
        if c==" ":
            res+=" "
        elif c.isupper():
            res+=chr(((ord(c)-65+n)%26)+65)
        else:
            res+=chr(((ord(c)-97+n)%26)+97)
    print(res)

#encrypt()

#Task01.5
def decrypt():
    s=input("Text to decrypt :  ")
    n=input("Shift :  ")
    while not n.isnumeric():
        n = input("Shift (int):  ")
    res=""
    n=int(n)
    for c in s:
        if c.isupper():
            res+=chr(((ord(c)-65-n)%26)+65)
        elif c.islower():
            res+=chr(((ord(c)-97-n)%26)+97)
        else:
            res+=c
    print(res)

#decrypt()

#Task02
def vigenere(mode, str, key):
    res=""
    if mode=="-e":sign=1
    elif mode=="-d":sign=-1
    else:print("no mode")
    for i in range(len(str)):
        car=str[i]
        if car.isupper(): 
            shift=(ord(key[i%len(key)])-65)*sign 
            res+=chr((ord(car)-65+shift) %26+65)
        elif car.islower():
            shift=(ord(key[i%len(key)])-97)*sign
            res+=chr((ord(car)-97+shift) %26+97)
        else:
            res+=car
    print(res)

#python encryption.py
#or
#python encryption.py -mode text key
#to launch Vigenere code

if __name__ == '__main__':
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case '01':
                encrypt()
            case '01.5':
                decrypt()
    elif len(sys.argv) == 4:
        vigenere(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        vigenere("-d", "abc", "def")

            
            
