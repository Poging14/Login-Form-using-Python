from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

#-----------Function___
def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def password(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
#----

root=Tk()
root.geometry('990x660+50+20')
bgImage=ImageTk.PhotoImage(file= 'PYTHON.png')
bgLabel=Label(root, image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(root,text='Admin Login',font=('Microsoft Yahei UI light', 23,'bold'), fg='Black')
heading.place(x=610,y=220)

usernameEntry = Entry(root,width=20,font=('Microsoft Yahei UI light', 14,'bold'),bd=0,bg='white',fg='black')
usernameEntry.place(x=590,y=300)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)

#Frame(root,width=250,height=2,bg='blue').place(x=580,y=280)

passwordEntry = Entry(root,width=20,font=('Microsoft Yahei UI light', 14,'bold'),bd=0,bg='white',fg='black')
passwordEntry.place(x=590,y=340)
passwordEntry.insert(0,'Password',)
passwordEntry.bind('<FocusIn>',password)

loginButton=Button(root, text='Login',font=('Open sans',15,'bold'),
                   fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',
                   cursor='hand2',width=19)
loginButton.place(x=590,y=400)
root.mainloop()
