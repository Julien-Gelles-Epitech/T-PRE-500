import sys

#Task01
the_ambassadors_banquet_guests = ["Jeanne", "Eva", "Max"]

def task01(name):
    if name in the_ambassadors_banquet_guests:
        print("Welcome in buddy")
    else:
        print("Nah, get lost!")

#Task02
def task02(l):
    return list(dict.fromkeys(l))

#Task03
meetings=[["Monday", "3:30 PM", "Samantha", "Eva"],
          ["Monday", "3:30 PM", "Joe", "Samantha"],
          ["Wednesday", "3:30 PM", "Joe"],
          ["Friday", "3:30 PM", "Joe", "Paul", "Eva"],
          ["Friday", "3:30 PM", "Paul", "Samantha"]]

def task03(name):
    meetings_list=[]
    for e in meetings:
        if name in e: meetings_list.append(e[0:2])
    if meetings_list == []: print("U got no meetings nerd oO")
    else:
        print(name + " | Your meeting list: ")
        for m in meetings_list:
            print(str(m[0])+" -> "+str(m[1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                task01("Paul")
                task01("Eva")
            case '02':
                print(task02([1,4,7,1,3,7,7,4,0,8,0]))
            case '03':
                task03("Samantha")
                task03("Paul")
                task03("Jerem")