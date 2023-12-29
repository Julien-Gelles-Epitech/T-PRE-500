import sys

#Task00
def lower(s, n, c=0):
    if len(s)==0:
        return c>=n
    else:
        if s[0].islower():
            c+=1
        return lower(s[1:], n, c)
 
def upper(s, n, c=0):
    if len(s)==0:
        return c>=n
    else:
        if s[0].isupper():
            c+=1
        return upper(s[1:], n, c)

def alpha(s, n, c=0):
    if len(s)==0:
        return c>=n
    else:
        if s[0].isalpha():
            c+=1
        return alpha(s[1:], n, c)

def special(s, n, c=0):
    if len(s)==0:
        return c>=n
    else:
        if not s[0].isalpha() and not s[0].isdigit():
            c+=1
        return special(s[1:], n, c)

def digit(s, n, c=0):
    if len(s)==0:
        return c>=n
    else:
        if s[0].isdigit():
            c+=1
        return digit(s[1:], n, c)
    

#Task01
def check_password(f, n, s):
    return f(s,n)

mysecretpassword="abcd/."
#print(check_password(lower, 4, mysecretpassword) and check_password(special, 2, mysecretpassword))

#Task02
#J'aime pas/pas tant compris la question alors je fais la mienne a ma sauce
def check_password_error():
    pwd=input("Enter a password: ")
    while not (check_password(lower, 1, pwd) and check_password(upper, 1, pwd) and check_password(special, 1, mysecretpassword) and check_password(digit, 1, pwd)):
        pwd = input("Enter a correct password\n(It must contain at least 1 upper letter, 1 lower letter, 1 special character and 1 digit) : ")
    print("Noice ;³")
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                print(lower("abc", 3))
                print(upper("ABCD", 4))
                print(alpha("Ab", 2))
                print(special("?-/", 3))
                print(digit("12345", 5))
            case '01':
                print(check_password(lower, 4, mysecretpassword) and check_password(special, 2, mysecretpassword))
            case '02':
                check_password_error()