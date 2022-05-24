#displaycon.py
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import loginform as log

#root = Tk()

class Display_Contacts:
    def __init__(self,root):
        self.root = root
        self.root.title("Phonebook")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True,True)

        self.bg=ImageTk.PhotoImage(file="image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_dis = Frame(self.root)
        Frame_dis.place(x=100,y=100,height=640,width=800)

        title = Label(self.root,text="Your Contacts Here",font=("Arial",35,"bold"),fg="#d77337",bg="white").place(x=100,y=5)
        uid = log.uid
        tname = 'tab' + str(uid)
        con = sqlite3.connect("details")
        c = con.cursor()
        c.execute('''SELECT * FROM {}'''.format(tname))
        lst = c.fetchall()
        lst = [('Name','Phone number','City')] + lst
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(Frame_dis, width=20, fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i+100, column=j)
                self.e.insert(END, lst[i][j])