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
