from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import add as a
import deletecon as d
import displaycon as dis
import searchcon as s

class Menu:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)
        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        Frame_menu = Frame(self.root)
        Frame_menu.place(x=100,y=15,height=640,width=1000)

        title = Label(Frame_menu,text="What would you like to do ?",font=("Arial",35,"bold"),fg="#ff0000",bg="white").place(x=90,y=30)
        desc = Label(Frame_menu,text="Phonebook User's menu",font=("Arial",15,"bold"),fg="#ff0000",bg="white").place(x=90,y=100)

        add_contacts = Button(self.root,command=self.add,text="Add Contacts    ",fg="white",bg="#00ff00",font=("times new roman",50)).place(x=110,y=200)
        delete_contacts = Button(self.root,command=self.delete,text="Delete Contact",fg="white",bg="#ff0000",bd=0,font=("times new roman",50)).place(x=600,y=200)
        display_contacts = Button(self.root,command=self.display,text="Display Contacts",fg="white",bg="#dd00aa",bd=0,font=("times new roman",50)).place(x=110,y=400)
        search_contacts = Button(self.root,command=self.search,text="Search Contacts",fg="white",bg="#d77337",bd=0,font=("times new roman",50)).place(x=600,y=400)

    def add(self):
        root1 = Toplevel()
        obj = a.Add_Contacts(root1)
        root1.mainloop()
    def delete(self):
        root1 = Toplevel()
        d.Delete_Contacts(root1)
        root1.mainloop()
    def display(self):
        root1 = Toplevel()
        dis.Display_Contacts(root1)
        root1.mainloop()
    def search(self):
        root1 = Toplevel()
        s.Search_Contacts(root1)
        root1.mainloop()
