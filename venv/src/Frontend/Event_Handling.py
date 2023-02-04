from tkinter import  *
from tkinter import messagebox
from src.Backend import PhoneBookBack

back = PhoneBookBack.data("PBDB.db")

class Events:
        def __init__(self,root_Windows):
                self.root_wind = root_Windows

        def btnAddContactClick(self):
                AddContact_win = Toplevel(self.root_wind)
                AddContact_win.title("Add Contact")
                AddContact_win.configure(bg="#F0F0F0")
                AddContact_win.geometry("375x320")
                AddContact_win.resizable(width=False,height=False)
                #----------------------lbl_Name----------------------------
                lbl_Name = Label(AddContact_win,text="Name:",bg="#F0F0F0",font = ("Tahoma",12))
                lbl_Name.place(x=12,y=9)
                #----------------------txt_Name----------------------------
                txt_Name = Entry(AddContact_win,bg="white",font=("Tahoma",12),width=27)
                txt_Name.place(x=109,y=6)

                #----------------------lbl_Family----------------------------
                lbl_Family = Label(AddContact_win,text="Family:",bg="#F0F0F0",font = ("Tahoma",12))
                lbl_Family.place(x=12,y=55)
                #----------------------txt_Family----------------------------
                txt_Family = Entry(AddContact_win,bg="white",font=("Tahoma",12),width=27)
                txt_Family.place(x=109,y=51)

                #----------------------lbl_PhoneNumber----------------------------
                lbl_PhoneNumber = Label(AddContact_win,text="PhoneNumber:",bg="#F0F0F0",font = ("Tahoma",9))
                lbl_PhoneNumber.place(x=12,y=101)
                #----------------------txt_PhoneNumber----------------------------
                txt_PhoneNumber = Spinbox(AddContact_win,bg="white",font=("Tahoma",12),width=26,from_=0,to=99999999999)
                txt_PhoneNumber.pack()
                txt_PhoneNumber.place(x=109,y=96)


                #----------------------lbl_Address----------------------------
                lbl_Address = Label(AddContact_win,text="Address:",bg="#F0F0F0",font = ("Tahoma",12))
                lbl_Address.place(x=12,y=144)
                #----------------------txt_Address----------------------------
                txt_Address = Text(AddContact_win,bg="white",font=("Tahoma"),width=22,height=4)
                txt_Address.place(x=109,y=140)

                def getInfoContact():
                        strName = txt_Name.get()
                        strFamily = txt_Family.get()
                        strPhoneNumber = txt_PhoneNumber.get()
                        strAddress = txt_Address.get(1.0,"end-1c")
                        try:
                                back.Add(strName, strFamily, strPhoneNumber, strAddress)
                                messagebox.showinfo("Done!","Contact saved successfully")
                        except:
                                messagebox.showerror("Failed!","There is a problem")



                #----------------------btn_Add----------------------------
                btn_Add = Button(AddContact_win,bg="#F0F0F0",font=("Tahoma",12),text="Add",command=getInfoContact)
                btn_Add.place(x=109,y=275)
                #----------------------btn_Cancle----------------------------
                btn_Cancel = Button(AddContact_win,text="Cancel",bg="#F0F0F0",font = ("Tahoma",12),command=AddContact_win.destroy)
                btn_Cancel.place(x=290,y=275)










