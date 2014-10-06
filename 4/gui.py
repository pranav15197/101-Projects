<<<<<<< HEAD
import sys
from Tkinter import *
def mHello():
    mtext = ment.get()
    mLable2 = Label(mGui,text=mtext).pack()


mGui = Tk()
mGui.geometry('450x450+500+200')
ment = StringVar()
mGui.title('Sample Window')


mLable = Label(mGui,text='mylable').pack()

mButton = Button(mGui,text='click',command = mHello).pack()

mEntry = Entry(mGui,textvariable = ment).pack()

mGui.mainloop()

















#mLable = Label(text='my2ndlable',fg='red',bg='blue').grid(row=1,column=0)
#mLable = Label(text='my3rdlable command',fg='red',bg='blue').grid(row=0,column=1,sticky=W)

#mLable = Label(text='mylable',fg='red',bg='blue').place(x=200,y=220)#fg means foreground,bg is background
#mSecLable = Label(text='my2ndlable',fg='red',bg='blue').pack()#fg means foreground,bg is background
=======
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
>>>>>>> f5bd88d1cf4cb45fb0b548ea10eb3c64265849db
