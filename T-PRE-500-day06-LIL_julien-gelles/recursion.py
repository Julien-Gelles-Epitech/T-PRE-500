import os, sys

#Task01
def task01(s):
    if len(s)==0 or len(s)==1:
        return True
    else:
        return s[0]==s[-1] and task01(s[1:-1])
    
def task01b(s):
    c=" ?,;.:/~#\"'(){}[]-|`_\\“<>§^¨£$øµ*+=°@"
    for e in c:
        s=s.replace(e, "")
    s=s.lower()
    return s

#Task02
def task02(dir, index=0, l=set()):
    file_path = os.listdir(dir)
    for i in range(len(file_path)):
        if i==(len(file_path)-1):
            l.add(index)
            s="└──"
        else:
            if index in l: l.remove(index)
            s="├──"          
        m=""
        for j in range(index):
            if j in l: m+="    "
            else: m+="│   "
        s=m+s
        print(s, file_path[i])
        if os.path.isdir(dir+"/"+file_path[i]):
            task02(dir+"/"+file_path[i]+"/", index+1, l)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                print(task01(task01b("Was it a car or a cat I saw?")))
            case '02':
                task02("/home/julien/Documents/")