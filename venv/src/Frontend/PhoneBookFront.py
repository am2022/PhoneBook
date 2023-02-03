import sys
sys.path.insert(0, '../')
from Backend import PhoneBookBack
from tkinter import *

root_win = Tk()
root_win.title("phonebook")
root_win.configure(bg="white")

data = PhoneBookBack.data("PBDB.db")

root_win.mainloop()
