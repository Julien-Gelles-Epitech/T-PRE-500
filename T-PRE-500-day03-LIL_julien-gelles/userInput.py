import re, sys

#Task00
def task00():
    print('Hey, whats ur name mate ?')
    name = input()
    print('Hello, ' + name +'!')

#Task01
def task01():
    print('Hey, whats ur name mate ?')
    name = input()
    print('Hello, ' + name.capitalize() +'!')

#Task02
def task02():
    print('Sup friend, can you give me a number plz ?')
    x = input()
    while not x.isnumeric():
        print('Thats not a number bro .. give me one plz')
        x = input()
    print('And a second number plz ?')
    y = input()
    while not y.isnumeric():
        print('Mm, not a number .. give me one plz')
        y = input()
    z=int(x)+int(y)
    print("=> " + x + " + " + y + " = " + str(z) + ", quick math ! (ツ)_/¯")

#Task03
def task03():
    print('Hey, I might feel invasive to u but i need an other number :)')
    x = input()
    try:
        x = int(x)
    except ValueError:
        pass
    print(type(x))

#Task04
def task04():
    print("Tell me something, whatever you want but make sentences and use ponctuations, ty!")
    str = input()
    str = str.replace("?", ".").replace("!", ".")
    str = re.sub('[.][ ]+', '.', str)
    str = str.split(".")
    firstWords = []
    for sentence in str:
        firstWords.append(sentence.split(" ")[0])
    print(" ".join(firstWords))

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