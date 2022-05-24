from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import loginform as l
import re
class SignUp:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1000x700+100+50")
        self.root.resizable(True,True)
        
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_signup = Frame(self.root)
        Frame_signup.place(x=100,y=15,height=640,width=700)

        title = Label(Frame_signup,text="Signup Here",font=("Arial",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_signup,text="Phonebook User's",font=("Arial",15,"bold"),fg="#ff0000",bg="white").place(x=90,y=100)

        lbl_fname = Label(Frame_signup,text="First name:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=140)
        self.txt_fname=Entry(Frame_signup,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=90,y=170,width=350,height=35)

        lbl_lname = Label(Frame_signup,text="Last name:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=210)
        self.txt_lname=Entry(Frame_signup,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=90,y=240,width=350,height=35)

        lbl_email = Label(Frame_signup,text="Email id:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=280)
        self.txt_email=Entry(Frame_signup,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=90,y=310,width=350,height=35)

        lbl_pass = Label(Frame_signup,text="Password:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=350)
        self.txt_pass = Entry(Frame_signup,show="*",bg="lightgrey")
        self.txt_pass.place(x=90,y=380,width=350,height=35)

        lbl_passc = Label(Frame_signup,text="Re-enter Password:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=420)
        self.txt_passc = Entry(Frame_signup,show="*",bg="lightgrey")
        self.txt_passc.place(x=90,y=450,width=350,height=35)

        Or =  Label(self.root,text="OR",font=("Arial",20,"bold"),fg="#d77337",bg="white").place(x=360,y=560)
        sign_up = Button(self.root,text="Sign Up",command=self.Sign,fg="white",bg="#d77337",bd=0,font=("times new roman",30)).place(x=450,y=550)
        Login_btn = Button(self.root,text="Login",command=self.log,bg="white",fg="#d77337",bd=0,font=("times new roman",30)).place(x=200,y=550)
    
    def log(self):
        obj = l.Login(self.root)
        self.root.mainloop()
    def Sign(self):
        fn=str(self.txt_fname.get())
        ln=str(self.txt_lname.get())
        em=str(self.txt_email.get())
        p1=str(self.txt_pass.get())
        p2=str(self.txt_passc.get())
        messagebox.showinfo("INFO",)
        con = sqlite3.connect("details")
        c = con.cursor()
        c.execute('''SELECT * FROM LoginDetails''')
        uid = len(c.fetchall()) + 1
        name = 'tab' + str(uid)
        messagebox.showinfo("INFO",em)
        c.execute("INSERT INTO LoginDetails VALUES(:u,:e,:p)",{'u':uid,'e':em,'p':p1})
        c.execute('''INSERT INTO Details VALUES(:u1,:f,:l,:e,:p3)''',{'u1':uid,'f':fn,'l':ln,'e':em,'p3':p1})
        c.execute('''CREATE TABLE {} (Name text,PhoneNumber INTEGER,City text)'''.format(name))
        con.commit()
        con.close()
        messagebox.showinfo("INFO","Congrats!!!\n You logged in successfully!!!")
        self.root.destroy()
        root = Toplevel()
        obj = l.Login(root)
        root.mainloop()