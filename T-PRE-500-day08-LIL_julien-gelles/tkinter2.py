import sys
from tkinter import *
from PIL import Image,ImageTk

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case '01':
                window = Tk()
                window.title("Window")
                frame = Frame(window)
                frame.pack()

                def printInput():
                    print(ent.get().upper())

                ent = Entry(window, bd=5 )
                ent.pack(side=LEFT)

                btn = Button(window, text="Bouton", bg="grey", fg="white", command=printInput)
                btn.pack(side=LEFT)

                window.mainloop()
            case '02':
                
                window = Tk()
                img = Image.open("186633.jpg")
                bg= ImageTk.PhotoImage(img)

                window.title("Window")
                window.geometry(str(img.width)+'x'+str(img.height))
                frame = Frame(window)
                frame2 = Frame(window)  
                frame.pack(side=TOP)
                frame2.pack(side=TOP)

                def printInput():
                    print(ent.get().upper())

                ent = Entry(frame, bd=5 )
                ent.pack(side=LEFT)

                btn = Button(frame, text="Bouton", bg="grey", fg="white", command=printInput)
                btn.pack(side=LEFT)
            
                cnv= Canvas(frame2, width=img.width, height=img.height)
                cnv.pack()

                cnv.create_image(0,0,anchor=NW,image=bg)

                window.mainloop()
            case '03':
                window = Tk()
                window.title("Window")
                window.geometry("850x600")

                cnv = Canvas(window, width=850, height=600, bg="ivory")
                cnv.pack()

                def stickman0():
                    cnv.create_line((425,225),(375,275), width=7, fill="purple")
                    cnv.create_line((425,225),(475,275), width=7, fill="yellow")
                    cnv.create_line((425,125),(375,175), width=7, fill="red")
                    cnv.create_line((425,125),(475,175), width=7, fill="blue")
                    cnv.create_line((425,100),(425,230), width=7, fill="green")
                
                def stickman1():
                    cnv.delete("all")
                    stickman0()
                    cnv.create_oval((400,50),(450,100), outline="lime", fill="lime")
                    window.after(1000, stickman2)

                def stickman2():
                    cnv.delete("all")
                    stickman0()
                    cnv.create_oval((370,20),(480,130), outline="red", fill="red")
                    window.after(1000, stickman1)

                stickman1()
                window.after(6000, window.destroy)
                window.mainloop()
            case 'challenge':
                window = Tk()
                window.title("Window")
                window.geometry("1000x1000")

                cnv = Canvas(window, bg="#1f5c2e")
                cnv.pack(expand=True, fill=BOTH)

                cnv.create_oval(325,450,850,650, outline="#343434", fill="#343434")
                cnv.create_oval(325,460,800,640, outline="#272727", fill="#272727")
                cnv.create_oval(325,475,725,625, outline="#202020", fill="#202020")
                cnv.create_oval(325,495,625,605, outline="#131313", fill="#131313")

                cnv.create_oval(190,160,620,610, outline="#E5E5E5", fill="#E5E5E5")
                cnv.create_oval(200,180,570,570, outline="#ECECEC", fill="#ECECEC")
                cnv.create_oval(215,210,495,510, outline="#F3F3F3", fill="#F3F3F3")
                cnv.create_oval(235,250,395,430, outline="#FAFAFA", fill="#FAFAFA")

                window.after(15000, window.destroy)
                window.mainloop()
            case '04':
                window = Tk()
                window.title("Window")
                window.geometry("1000x1000")

                cnv = Canvas(window, bg="white")
                cnv.pack(expand=True, fill=BOTH)
                repeat=True

                def pose1():
                    cnv.delete("all")
                    
                    cnv.create_line((425,100),(425,230), width=7) #body

                    cnv.create_line((390,120),(460,140), width=7) #top

                    cnv.create_line((391,117),(360,190), width=7) #left arm
                    cnv.create_oval((350,180),(370,200), outline="black", fill="black")
                    cnv.create_line((459,138),(430,210), width=7) #right arm
                    cnv.create_oval((420,200),(440,220), outline="black", fill="black")

                    cnv.create_line((390,230),(460,230), width=7) #bottom

                    cnv.create_line((392,229),(350,330), width=7) #left leg
                    cnv.create_oval((320,325),(360,337), outline="black", fill="black")
                    cnv.create_line((457,229),(440,330), width=7) #right leg
                    cnv.create_oval((430,325),(470,337), outline="black", fill="black")

                    cnv.create_oval((400,50),(450,100), width=6) #head

                    window.after(300, pose1b)

                def pose2():
                    cnv.delete("all")

                    cnv.create_line((425,100),(425,230), width=7) #body

                    cnv.create_line((460,120),(390,140), width=7) #top

                    cnv.create_line((458,119),(490,190), width=7) #left arm
                    cnv.create_oval((480,180),(500,200), outline="black", fill="black")
                    cnv.create_line((391,138),(420,210), width=7) #right arm
                    cnv.create_oval((408,200),(430,220), outline="black", fill="black")

                    cnv.create_line((390,230),(460,230), width=7) #bottom

                    cnv.create_line((392,228),(410,330), width=7) #left leg
                    cnv.create_oval((380,325),(420,337), outline="black", fill="black")
                    cnv.create_line((458,228),(500,330), width=7) #right leg
                    cnv.create_oval((490,325),(530,337), outline="black", fill="black")

                    cnv.create_oval((400,50),(450,100), width=6) #head

                    window.after(300, pose2b)

                def pose2b():
                    cnv.delete("all")

                    cnv.create_line((425,120),(425,250), width=7) #body

                    cnv.create_line((460,140),(390,160), width=7) #top

                    cnv.create_line((458,140),(530,150), width=7) #left arm
                    cnv.create_oval((518,140),(538,160), outline="black", fill="black")
                    cnv.create_line((390,160),(460,170), width=7) #right arm
                    cnv.create_oval((450,160),(470,180), outline="black", fill="black")

                    cnv.create_line((390,250),(460,250), width=7) #bottom

                    cnv.create_line((390,250),(420,280), width=7) #left leg
                    cnv.create_line((418,279),(410,330), width=7) #left leg
                    cnv.create_oval((400,325),(440,337), outline="black", fill="black")
                    cnv.create_line((459,249),(490,280), width=7) #right leg
                    cnv.create_line((489,279),(500,330), width=7) #right leg
                    cnv.create_oval((490,325),(530,337), outline="black", fill="black")

                    cnv.create_oval((400,70),(450,120), width=6) #head

                    window.after(500, pose1)

                def pose1b():
                    cnv.delete("all")

                    cnv.create_line((425,120),(425,250), width=7) #body

                    cnv.create_line((390,140),(460,160), width=7) #top

                    cnv.create_line((391,140),(320,150), width=7) #left arm
                    cnv.create_oval((310,140),(330,160), outline="black", fill="black")
                    cnv.create_line((460,160),(390,170), width=7) #right arm
                    cnv.create_oval((380,160),(400,180), outline="black", fill="black")

                    cnv.create_line((390,250),(460,250), width=7) #bottom

                    cnv.create_line((391,249),(360,280), width=7) #left leg
                    cnv.create_line((360,280),(351,329), width=7) #left leg
                    cnv.create_oval((320,325),(360,337), outline="black", fill="black")
                    cnv.create_line((459,249),(430,280), width=7) #right leg
                    cnv.create_line((430,280),(420,330), width=7) #right leg
                    cnv.create_oval((390,325),(430,337), outline="black", fill="black")

                    cnv.create_oval((400,70),(450,120), width=6) #head

                    window.after(500, pose2)

                pose1()

                window.after(10000, window.destroy)
                window.mainloop()




