import sys

#Task00
str = "string in a variable"
#print(str)

#Task01
#print(str[0],str[4])

#Task02
#print(str[-1])

#Task03
#print(str[4:9])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                print(str)
            case '01':
                print(str[0],str[4])
            case '02':
                print(str[-1])
            case '03':
                print(str[4:9])