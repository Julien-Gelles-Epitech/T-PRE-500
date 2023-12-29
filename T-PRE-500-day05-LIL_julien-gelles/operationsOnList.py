import numpy, time, random, sys


#Task01
l = [x for x in range(10)]

def task01(l):
    res=1
    for x in l:
        res*=x
    return res

def task01b(l):
    if len(l)==0:
        return 1
    else:
        return l[0] * task01b(l[1:])

#Task02
# Ajoute 10 a toutes les valeurs de la liste
#print("02:", [x+10 for x in [3, 2, 6, 7, 1, 4]])

#Task03
# Ici, lambda x permet de creer une fonction anonyme qui pourra être utilisé avec un valeur par la suite
print("03:", list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))

#Task04
l=[3, 2, 6, 7, 1, 4]
def task04(l):
    if len(l)<1: return
    max,min=l[0],l[0]
    for e in l:
        if e<min: min=e
        if e>max: max=e
    return ("min: "+str(min)+", "+"max: "+str(max))

def task04b(l):
    if len(l) == 0:
        return
    elif len(l) == 1:
        return (l[0],l[0])
    else:
        return (min(l[0], task04b(l[1:])[0]),max(l[0], task04b(l[1:])[1]))

#Task05
m=[9,6,3,8,5,7,0,11,1]
def task05(m):
    res=[]
    for e in m:
        if e<7: res.append(e)
    return res

def task05b(m):
    if len(m) == 0:
        return []
    else:
        return [m[0]] + task05b(m[1:]) if m[0]<7 else task05b(m[1:]) 

#Task06
n = m.copy()
n.sort()
n.reverse()
#print("06: ", n)

o = m.copy()
o.sort(reverse=True)
#print("06b: ", o)

#Task07
# This code multiplies by 2 odd numbers and divide by 2 even numbers in list
print("07: ", [x//2 if x%2==0 else x*2 for x in [42, 3, 4, 18, 3, 10]])

#Test08
# This code filter numbers greater than 10 in list
print("08: ", list(filter(lambda x: x>10, [42, 3, 4, 18, 3, 10])))

#Test09
# This code use the enumerate python function to associate a counter to each value in list as tuples
print("09: ", [*enumerate([42, 3, 4, 18, 3, 10])])

#Task10
#This code match elements in first list with elements in the second in reverse
first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]
magic = [*zip(first_name, last_name[::-1])]
print(magic)

#Challenge
def challenge():
    startingTime = time.time()
    l = [random.randint(0,1) for x in range(1000000)]
    duration = time.time() - startingTime
    return duration

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print(task01([1,2,3,4]))
            case '01b':
                print(task01b([1,2,3,4]))
            case '01c':
                print(numpy.prod([1,2,3,4]))
            case '02':
                print("Ajoute 10 a toutes les valeurs de la liste.")
            case '03':
                print("Ici, lambda x permet de creer une fonction anonyme qui pourra être utilisé avec un valeur par la suite.")
            case '04':
                print(task04(l))
            case '04b':
                print("min: "+str(task04b(l)[0])+", "+"max: "+str(task04b(l)[1]))
            case '04c':
                print("min: "+str(min(l))+", "+"max: "+str(max(l)))
            case '05':
                print(task05(m))
            case '05b':
                print(task05b(m))
            case '05c':
                print([e for e in m if e<7])
            case '06':
                print(n)
            case '06b':
                print(o)
            case '07':
                print("This code multiplies by 2 odd numbers and divide by 2 even numbers in list.")
            case '08':
                print("This code filter numbers greater than 10 in list.")
            case '09':
                print("This code use the enumerate python function to associate a counter to each value in list as tuples.")
            case '10':
                print("This code match elements in first list with elements in the second in reverse.")
            case "challenge":
                print(challenge())