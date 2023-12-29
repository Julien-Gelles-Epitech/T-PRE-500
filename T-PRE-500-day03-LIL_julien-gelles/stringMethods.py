import sys

#Task00
def task00(s):
    return s.lower()

#Task01
def task01(s):
    return s.replace("tu", "ta")

#Task02
string = "hello world"
position = string.find("a")
#print(position)
#Ce code affiche la position du caractere 'a' ou le code erreur -1 s il n est pas trouve

#Task03
p = "abcdefghijklmnop"
#print (p[::-2][:5][::-1][3:])

#[::-2] affiche les caracteres avec un pas -2 (de 2 a partir de la fin)
#[:5] affiche les 5 premiers caracteres
#[::-1] affiche les caracteres dans le sens inverse (pas de -1)
#[3:] affiche les caracteres a partir du troisieme

#Task04
#print(p[-3:][::2])

#Task05
def task05(s):
    str=""
    for i in range(10):
        str+=s
    print(str)

#Task06
def task06(s):
    print(s*10)

#Task07
s1 = "Hello"
s2 = 42
concat = s1 + str(s2)
#print (concat)

#Task08
string1 = "42 "
string2 = "is "
string3 = "the answer"
concat = string1+string2+string3
#print ("The string \""+concat+"\" contains "+ str(len(concat)) +" characters.")

#Challenge
def challenge(s):
    d = {"cat":0, "garden":0, "mice":0}
    s1 = s.lower()
    s2 = s1[::-1]
    for key in d:
        d[key] += s1.count(key)
        d[key] += s2.count(key)
    print(d)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '00':
                print(task00("UPPER To lower"))
            case '01':
                print(task01("tutu on the tuki-kata"))
            case '02':
                print("Ce code affiche la position du caractere 'a' ou le code erreur -1 s il n est pas trouve.")
            case '03':
                print("[::-2] affiche les caracteres avec un pas -2 (de 2 a partir de la fin)")
                print("[:5] affiche les 5 premiers caracteres.")
                print("[::-1] affiche les caracteres dans le sens inverse (pas de -1)")
                print("[3:] affiche les caracteres a partir du troisieme.")
            case '04':
                print(p[-3:][::2])
            case '05':
                task05("Hello")
            case '06':
                task06("Hello")
            case '07':
                print (concat)
            case '08':
                print ("The string \""+concat+"\" contains "+ str(len(concat)) +" characters.")
            case "challenge":
                challenge("thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN")
