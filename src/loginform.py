from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import signup as s
import menu as m

uid =0
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)
        
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        Frame_login = Frame(self.root)
        Frame_login.place(x=150,y=150,height=340,width=500)

        title = Label(Frame_login,text="Login Here",font=("Arial",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_login,text="Phonebook User's",font=("Arial",15,"bold"),fg="#ff0000",bg="white").place(x=90,y=100)

        lbl_user = Label(Frame_login,text="Email id:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login,text="Password:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=210)
        self.txt_pass = Entry(Frame_login,show="*",bg="lightgrey")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget = Button(Frame_login,text="Forget Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",15)).place(x=90,y=280)
        Or =  Label(self.root,text="OR",font=("Arial",20,"bold"),fg="#d77337",bg="white").place(x=360,y=510)
        sign_up = Button(self.root,text="Sign Up",bg="white",fg="#d77337",command=self.sign,bd=0,font=("times new roman",30)).place(x=450,y=500)
        Login_btn = Button(self.root,command=self.login,text="Login",fg="white",bg="#d77337",bd=0,font=("times new roman",30), activebackground="#f00", activeforeground="#fff")
        Login_btn.place(x=200,y=500)
        
        
    def login(self):
        t = self.txt_user.get()
        p = self.txt_pass.get()
        t=str(t)
        p=str(p)
        a=[]
        con = sqlite3.connect("details")
        c = con.cursor()
        c.execute('''SELECT Email_id FROM LoginDetails''')
        for i in c.fetchall():
            for j in range(1):
                a.append(i[0])
        if t =="" or p =="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif t !="" and p != "":
            for i in a:
                if i == t:
                    c.execute('''SELECT Password FROM LoginDetails where Email_id=:f''',{'f':t})
                    pa = c.fetchall()
                    if pa[0][0] == p:
                        messagebox.showerror("YES","Welcome to your PHONEBOOK!!!",parent=self.root) 
                        c.execute('''SELECT U_id FROM LoginDetails where Email_id=:f''',{'f':t})
                        f = c.fetchall()
                        global uid
                        uid = int(f[0][0])
                        obj = m.Menu(self.root)
                        self.root.mainloop()
                        break
                    else:
                        messagebox.showerror("No","Password Wrong",parent=self.root)
        else:
            messagebox.showerror("Error","Username/Password is wrong\n Try again!!!",parent=self.root)
        con.commit()
        con.close()
    def sign(self):
        obj = s.SignUp(self.root)
        self.root.mainloop()