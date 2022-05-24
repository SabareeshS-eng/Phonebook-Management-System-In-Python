from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import loginform as log
import quicksort as q
import dis as d
class Search_Contacts:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)
        
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        Frame_ser = Frame(self.root)
        Frame_ser.place(x=100,y=50,height=500,width=1000)
    
        title = Label(Frame_ser,text="Search a contact Here",font=("Arial",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)

        lbl_name = Label(Frame_ser,text="Enter Name:",font=("Arial",15,"bold"),fg="#d77337",bg="white").place(x=90,y=140)
        self.txt_name=Entry(Frame_ser,font=("times new roman",15),bg="lightgrey")
        self.txt_name.place(x=90,y=170,width=350,height=35)

        s = Button(self.root,text="Search",command=self.search,fg="white",bg="#d77337",bd=0,font=("times new roman",30)).place(x=200,y=450)
        ex = Button(self.root,text="Exit",command=self.exit,bg="white",fg="#d77337",bd=0,font=("times new roman",30)).place(x=450,y=450)
    
    def search(self):
        name = str(self.txt_name.get())
        root1=Toplevel()
        d.Display_Contacts(root1,name)
        root1.mainloop()
    def exit(self):
        self.root.destroy()