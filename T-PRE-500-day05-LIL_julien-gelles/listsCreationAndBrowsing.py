import sys

#Task01
l = [1,2,3,4,5]
#print("01:",l[0])

#Task02
#print("02:",l[-1])

#Task03
l.append(6)
#print("03:",l)

#Task04
#print("04:",l)

#Task05
l.pop(-1)
#print("05:",l)

#Task06
l.insert(0,0)
#print("06:",l)

#Task07
#print("07:",l[1:5])

#Task08
m = l.copy()
m.reverse()
#print("08:",m)

#Task09
#print("09:",l[::2])

#Task10
l+=[x for x in range(6,23)]
#print("10:",l)

#Task11
my_first_list = [4,5,6]
my_second_list = [1,2,3]
my_first_list.extend(my_second_list)
#print("11:",my_first_list)

my_first_list = [7,8,9]
my_second_list = [4,5,6]
my_first_list = [*my_first_list, *my_second_list]
#print("11b:",my_first_list)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print(l[0])
            case '02':
                print(l[-1])
            case '03':
                print(l)
            case '04':
                print(l)
            case '05':
                print(l)
            case '06':
                print(l)
            case '07':
                print(l[1:5])
            case '08':
                print(m)
            case '09':
                print(l[::2])
            case '10':
                print(l)
            case '11':
                print(my_first_list)
            case '11b':
                print(my_first_list)