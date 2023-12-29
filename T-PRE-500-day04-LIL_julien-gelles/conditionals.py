import sys

#Task00
# (42>12) verifie la condition: 42 est plus grand que 12 => True
# (12=12) ne veut rien dire, = sert a affecter une valeur a une variable
# (12==12) verifie la condition: 12 est egal a 12 => True
# ("hello"=="world") verifie la condition: "hello" est egale a "world" => False
# (218 >= 118) verifie la condition: 218 est plus grand ou egal a 118 => True
# ("a".upper()=="A") verifie la condition: "a" mis en majuscule est egale a "A" => True
# (1*2*3*4<=9) verifie la condition: 1*2*3*4 est inferieur a 9 => False
# ("z" in "azerty") verifie la condition: le caractere "z" est compris dans le mot "azerty"

#Task01
def task01():
    n = input("Can I get some number ? :  ")
    if n=="42":
        print("Correct answer")

#Task02
def task02():
    n = input("A last number ? :  ")
    while not n.isnumeric():
        n = input('Not a number wtf oO :  ')
    if int(n)%2==0:
        print("This integer is even")
    else:
        print("This integer is odd")

#Task03
def task03():
    s = input("Password ? :  ")
    if s=="Open sesame":
        print("Access granted")
    elif s=="Will you open, you goddamn !¤*@":
        print("Access fucking granted ayaaaaa")
    else:
        print("Permission denied")

#Task04
def task04():
    n = input("Yea i know i lied about the last number, need some more -éè :  ")
    while not n.isnumeric():
        print('Not a number wtf oO')
        n = input()
    n = int(n)
    if (n==42 or n<=21 or n%2==0 or n/2<21 or (n%2!=0 and n>=45)):
        print("OK")
    else:
        print("You got wrong my poor friend!")

#Task05
def task05():
    a=42
    b=41
    if a==b:
        print("A and B are the same")
    if b<=a:
        print("B is equal or lower than A")
    if b!=a:
        print("B is different from A")



if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                print("(42>12) verifie la condition: 42 est plus grand que 12 => True")
                print("12=12) ne veut rien dire, = sert a affecter une valeur a une variable")
                print("12==12) verifie la condition: 12 est egal a 12 => True")
                print("('hello'=='world') verifie la condition: 'hello' est egale a 'world' => False")
                print("(218 >= 118) verifie la condition: 218 est plus grand ou egal a 118 => True")
                print("('a'.upper()=='A') verifie la condition: 'a' mis en majuscule est egale a 'A' => True")
                print("(1*2*3*4<=9) verifie la condition: 1*2*3*4 est inferieur a 9 => False")
                print("('z' in 'azerty') verifie la condition: le caractere 'z' est compris dans le mot 'azerty'")
            case '01':
                task01()
            case '02':
                task02()
            case '03':
                task03()
            case '04':
                task04()
            case '05':
                task05()

