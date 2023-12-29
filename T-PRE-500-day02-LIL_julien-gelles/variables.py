import sys

#Task01
def task1(n):
    sum = 0
    j = 1
     
    for i in range(1, n + 1):
        sum = sum + j
        j = (j * 10) + 1
         
    print(sum) 

task1(3)

#Task02
#print(17**1024)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                task1(3)
            case '02':
                print(17**1024)