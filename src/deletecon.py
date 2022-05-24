from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import loginform as log
import quicksort as q

class Delete_Contacts:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)
        
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        Frame_add = Frame(self.root)
        Frame_add.place(x=100,y=50,height=500,width=1000)
    
        title = Label(Frame_add,text="Delete a contact Here",font=("Arial",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_name = Label(Frame_add,text="Name of the contact:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=140)
        self.txt_name=Entry(Frame_add,font=("times new roman",15),bg="lightgrey")
        self.txt_name.place(x=90,y=170,width=350,height=35)

        lbl_number = Label(Frame_add,text="Number of the contact:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=210)
        self.txt_number=Entry(Frame_add,font=("times new roman",15),bg="lightgrey")
        self.txt_number.place(x=90,y=240,width=350,height=35)

        add = Button(self.root,text="Delete",command=self.Delete,fg="white",bg="#d77337",bd=0,font=("times new roman",30)).place(x=200,y=450)
        ex = Button(self.root,text="Exit",command=self.e,bg="white",fg="#d77337",bd=0,font=("times new roman",30)).place(x=450,y=450)
    
    def Delete(self):
        # Database code
        con = sqlite3.connect("details")
        c = con.cursor()

        uid = log.uid
        name = self.txt_name.get()
        num = self.txt_number.get()
        tname = 'tab' + str(uid)
        if name != "" and num == "":
            c.execute('''DELETE FROM {} WHERE Name=:n1'''.format(tname),{'n1':name})
            messagebox.showinfo("INFO","Details with entered name are deleted SUCCESSFULLY!!!")
        elif name == "" and num != "":
            c.execute('''DELETE FROM {} WHERE PhoneNumber=:n1'''.format(tname),{'n1':num})
            messagebox.showinfo("INFO","Details with entered number are deleted SUCCESSFULLY!!!")
        elif name != "" and num!="":
            c.execute('''DELETE FROM {} WHERE PhoneNumber=:n1'''.format(tname),{'n1':num})
            messagebox.showinfo("INFO","Details deleted SUCCESSFULLY!!!")
        else:
            messagebox.showerror("ERROR","NOTHING ENTERED!!!")
        c.execute('''SELECT * FROM {}'''.format(tname))
        a = c.fetchall()
        a = q.get(a,len(a))
        c.execute('''DELETE FROM {}'''.format(tname))
        for i in a:
            c.execute('''INSERT INTO {} VALUES(:n,:num,:city)'''.format(tname),{'n':i[0],'num':i[1],'city':i[2]})
        con.commit()
        con.close()
    def e(self):
        self.root.destroy()