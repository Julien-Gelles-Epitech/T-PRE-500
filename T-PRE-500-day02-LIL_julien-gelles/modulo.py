import sys

#Task01
def task01(n, i):
    print(n/i)
    print(n//i)
    print(n%i)

#Task02
def task02(n):
    if n%2 == 0:
        print('Even')
    else:
        print('Odd)')

#Task03
def task03(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

#Task04
def task04(n):
    return int(n)

#Task05
def task05(n):
    return n%1

#Challenge
def challenge(n):
    return str(n)[str(n).index('.')+1:]
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                task01(42,4)
            case '02':
                task02(42)
            case '03':
                print(task03(3471))
            case '04':
                print(task04(12.24))
            case '05':
                print(task05(12.24))
            case "challenge":
                print(challenge(12.24))