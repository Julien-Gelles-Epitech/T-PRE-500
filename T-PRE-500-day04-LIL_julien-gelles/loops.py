import sys

#Task00
def task00():
    for i in range(1000):
        print(i+1)

#Task01
def task01():
    s = input("Gimme a single word:  ")
    if s.isnumeric() or " " in s:
        print("Thats what i thought, u just retard -_- anyway")
    s2=""
    for letters in s:
        s2+=letters*2
    print(s2)

#Task02
def task02():
    for i in range(10000, 0, -1):
        if i/7 == i//7:
            print(i)

#Task03
def task03():
    for i in range(-30, 31):
        res=""
        if i/3 == i//3:
            res+="Fizz"
        if i/5 == i//5:
            res+="Buzz"
        print(i, ':', res)

#Task04
def task04():
    for i in range(99,1,-1):
        print(i, "bottles of age-appropriate beverage on the wall")
    print("1 bottle of age-appropriate beverage on the wall")
    print("Nananananananananana Nanananananana")
    print("Nanana Nanana Nananananananana Nana")

#Task05()
def task05():
    n = input("Im sure you know what u have to do:  ")
    while not n.isnumeric():
        n = input('I expected u to know i needed a number :  ')
    n = int(n)
    for i in range(2, n//2+1):
        res="multiples-"+str(i)+":  "
        for j in range(n-1, 0, -1):
            if j//i == j/i:
                res+= str(j)+" "
        print(res)

#Challenge
def c():
    n,s,t,v=int(input()),input(),1,"aeiouyAEIOUY"
    if n==0:return
    while t and s!="":
        if s[0] in v:t=0
        s=s[1:]
    print(n) if t<1 or n>41 else print(s)

def d():
    x,y=int(input()),input()
    if x!=0:print(y) if set("aeiouyAEIOUY").isdisjoint(y) or x>41 else print(x);exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                task00()
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
            case "challenge":
                d()
                