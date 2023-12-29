import math, sys

#Task01
def task01(n):
    res = 0
    denom = 1

    for i in range(n):
        if i % 2 == 0:
            res += 4/denom
        else:
            res -= 4/denom
        denom+=2

    print(res)

def task01b(n):
    res = 0

    for i in range(1, n, 4):
        res += 4/i
        res -= 4/(i+2)

    print(res)

#Task02
def task02(n):
    res = 1

    for i in range(n, 0, -1):
        res = 6+((i*2-1)**2/res)

    print(res-6)

#Task03
def task03(n,d):
    pgcd = math.gcd(n,d)
    print(str(n//pgcd)+"/"+str(d//pgcd))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                task01(100000)
            case '01b':
                task01b(1000000)
            case '02':
                task02(100000)
            case '03':
                task03(5,10)