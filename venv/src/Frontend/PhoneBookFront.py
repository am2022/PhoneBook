import sys
sys.path.insert(0, '../')
from Backend import PhoneBookBack
from tkinter import *

root_win = Tk()
root_win.title("phonebook")
root_win.configure(bg="white")
root_win.geometry("900x500")
root_win.resizable(width=False, height=False)

data = PhoneBookBack.data("PBDB.db")

lb_main = Listbox(root_win, height=31, width=40)
lb_main.place(x=0, y=0)

btn_add = Button(root_win, text="+", width=4, bg="green")
btn_add.place(x=860, y=0)

root_win.mainloop()
