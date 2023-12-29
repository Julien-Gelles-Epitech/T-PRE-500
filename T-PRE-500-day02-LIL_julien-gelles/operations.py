import sys

#Task01
# print(1+1)
# print(30+12)
# print(777+(-735))
# print(1+2+3+5+7+11+13)

#Task02
# print(84-42)
# print(0-(-42))
# print(2*21)
# print((-6)*(-7))
# print(2+5*8)
# print((3+(3*4-2*2)*3-2)*2-3)

#Task03
#84/2 est une division classique, avec potentiellement des décimals, tandis que 84//2 est une division euclidienne qui renvoie un entier

#Task04
#(8+(-3)+(-7)+2 = 0 or 84/0 c'est impossible donc renvoie une erreur

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print(1+1)
                print(30+12)
                print(777+(-735))
                print(1+2+3+5+7+11+13)
            case '02':
                print(84-42)
                print(0-(-42))
                print(2*21)
                print((-6)*(-7))
                print(2+5*8)
                print((3+(3*4-2*2)*3-2)*2-3)
            case '03':
                print("84/2 est une division classique, avec potentiellement des décimals, tandis que 84//2 est une division euclidienne qui renvoie un entier.")
            case '04':
                print("(8+(-3)+(-7)+2 = 0 or 84/0 c'est impossible donc renvoie une erreur.")