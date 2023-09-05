from tkinter import *
from tkinter import simpledialog
from wordle import *

# creates a Tk() object
master = Tk()

class NewWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Rules")
        self.geometry("500x500")
        label1=Label(self,text="Enter a five letter word for each guess."+"\n"+"For example, pretend the secret word was HELPS"+"\n"+"\n"+"If a letter in your guess is in the secret word, and is in the right position,"+"\n"+"it will show up with a green highlight"+"\n")
        label1.pack()
        text = Text(self, height=1, width=10,background="gray93")
        text.pack()
        # Insert the text "HAPPY" into the Text widget
        text.insert(END, "HAPPY")
        # Apply formatting to different sections of the text
        text.tag_configure("font", font=("SF Pro", 12))
        text.tag_add("font", "1.0", "1.4")
        text.tag_configure("highlight", background="green2")
        text.tag_add("highlight", "1.0", "1.1")
        label2=Label(self,text="\n"+"If a letter in your guess is in the word, but is not in the right position,"+"\n"+"it will show up in yellow"+"\n")
        label2.pack()
        text1 = Text(self, height=1, width=10,background="gray93")
        text1.pack()
        # Insert the text "HAPPY" into the Text widget
        text1.insert(END, "LUCKY")
        # Apply formatting to different sections of the text
        text1.tag_configure("font", font=("SF Pro", 12))
        text1.tag_add("font", "1.0", "1.4")
        text1.tag_configure("highlight", background="yellow2")
        text1.tag_add("highlight", "1.0", "1.1")
        label3=Label(self,text="\n"+"If a letter in your guess is not in the word at all, there will be no highlight"+"\n")
        label3.pack()
        text2 = Text(self, height=1, width=10,background='gray93')
        text2.pack()
        # Insert the text "HAPPY" into the Text widget
        text2.insert(END, "TRAIN")
        # Apply formatting to different sections of the text
        text2.tag_configure("font", font=("SF Pro", 12))
        text2.tag_add("font","1.0","1.4")

class NewerWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Wordle")
        self.geometry("500x500")
        tries=6
        gamewon=False
        prev=[]
        while tries > 0 and gamewon==False:
            answervalid=False
            label=Label(self,text='You have '+str(tries)+' tries left!')
            label.pack()
            answer=simpledialog.askstring('',"Make a guess: "+"\n")
            answer=answer.upper()
            while answervalid==False:
                if answer.lower() in data_into_list and len(answer)==5 and answer not in prev:
                    answervalid=True
                elif len(answer)!=5:
                    labela=Label(self,text='Must be a five letter word, try again!')
                    labela.pack()
                    answer=simpledialog.askstring('',"Make a guess: "+"\n").upper()
                elif answer in prev:
                    labelb=Label(self,text='You already guessed that, try again!')
                    labelb.pack()
                    answer=simpledialog.askstring('',"Make a guess: "+"\n").upper()
                else:
                    labelc=Label(self,text='Not a real word, try again!')
                    labelc.pack()
                    answer=simpledialog.askstring('',"Make a guess: "+"\n").upper()
            greenlist=[]
            yellowlist=[]
            yellowlist2=[]
            graylist=[]
            printedresult=''
            for x in range(len(answer)):
                if answer[x]==secretword[x]:
                    greenlist.append(x)
                elif answer[x] in secretword:
                    if answer[x] not in yellowlist2:
                        yellowlist.append(x)
                        yellowlist2.append(answer[x])
                    else:
                        graylist.append(x)
                else:
                    graylist.append(x)
            for x in range(5):
                for k in [greenlist,yellowlist,graylist]:
                    if len(k)>x:
                        k[x]=1.0+(k[x]*0.1)
            text=Text(self,height=1,width=10,background='gray93')
            text.pack()
            text.insert(END, answer)
            text.tag_configure("font", font=("SF Pro", 12))
            text.tag_add("font", "1.0", "1.4")
            simple=[1.0,1.1,1.2,1.3,1.4]
            text.tag_configure("highlight-gr",background="green2")
            text.tag_configure("highlight-ye",background="yellow2")
            text.tag_configure("highlight-ay",background="gray70")
            for x in simple:
                if x in greenlist:
                    text.tag_add("highlight-gr",str(x))
                if x in yellowlist:
                    text.tag_add("highlight-ye",str(x))
            tries-=1
            prev.append(answer)
            if answer==secretword:
                gamewon=True
        if gamewon:
            label8=Label(self,text="Congratulations! The word was "+answer+"!")
            label8.pack()
            btn3=Button(self,text='Play again?')
            btn3.bind("<Button>", lambda e: NewerWindow(master))
            btn3.pack(pady=40)
        elif tries == 0:
            label9=Label(self,text='Sorry! The word was '+secretword+'! Better luck next time!')
            label9.pack()
            btn3=Button(self,text='Play again?')
            btn3.bind("<Button>", lambda e: NewerWindow(master))
            btn3.pack(pady=40)

# sets the geometry of main root window
master.geometry("300x300")

label = Label(master, text="Welcome to Wordle!")
label.pack(side=TOP, pady=10)


# a button widget which will open a new window on button click
btn = Button(master, text="Need a rules refresher?")
btn.bind("<Button>", lambda e: NewWindow(master))

btn.pack(pady=10)
btn1 = Button(master, text="Ready to play?")
btn1.bind("<Button>", lambda e: NewerWindow(master))
btn1.pack(pady=20)

# Following line will bind click event
# On any click left / right button
# of the mouse, a new window will be opened

# mainloop, runs infinitely
master.mainloop()
