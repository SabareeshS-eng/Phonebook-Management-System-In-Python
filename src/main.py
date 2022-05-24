#Import the required modules
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
from loginform import *
from signup import *

root = Toplevel()
obj = Login(root)
root.mainloop()