import time, sys

#Task00
#La fonction f renvoie la valeur de 2x+1 pour x l'argument passe a la fonction
#La fonction g renvoie toujours 7
def f(x) :
    return 2*x+1
def g() :
    return 7

y = f(2)
#print ("00 :", y)
y = f(5) + g()
#print ("00b :", y)

#Task01
def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato () :
    print("O O O O O O")
def ham():
    print("============")

def burger():
    bread()
    lettuce()
    ham()
    tomato()
    ham()
    bread()

#Task02
# for i in range(42):
#     print("\n")
#     burger()

#Task03
def task03(n):
    if n<1:
        print("I cant do this")
    else:
        for i in range(n):
            print("\n")
            burger()

#Task04
def veggieBurger():
    bread()
    lettuce()
    tomato()
    lettuce()
    tomato()
    bread()

def task04(n, vegetarian=False):
    if n<1:
        print("I cant do this")
    else:
        if vegetarian:
            for i in range(n):
                print("\n")
                veggieBurger()
        else:
            for i in range(n):
                print("\n")
                burger()
        
#Challenge
def challenge(n,i):
    if i==0:
        return 1
    else:
        return n*challenge(n, i-1)
def challenge2(n,i):
    return pow(n,i)


def challengeD(n,i):
    startingTime1 = time.time()
    challenge(n,i)
    duration1 = time.time() - startingTime1
    startingTime2 = time.time()
    challenge2(n,i)
    duration2 = time.time() - startingTime2
    return (duration1, duration2)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                print("La fonction f renvoie la valeur de 2x+1 pour x l'argument passe a la fonction.")
                print("La fonction g renvoie toujours 7.")
            case '01':
                burger()
            case '02':
                for i in range(42):
                    print("\n")
                    burger()
            case '03':
                task03(3)
            case '04':
                task04(2, True)
            case "challenge":
                print(challengeD(42,84))
                print(challengeD(42,168))

