import sqlite3

class data:
    def __init__(self, database_name):
        self.con = sqlite3.connect(f'../Backend/{database_name}')
        self.cursorObj = self.con.cursor()

    def __del__(self):
        self.con.close()

    def LoadAll(self):
        self.cursorObj.execute('SELECT * FROM contact')

        rows = self.cursorObj.fetchall()

        return rows

    def Add(self, name, family, phonenumber,address):
        entities = (name, family, phonenumber,address)
        self.cursorObj.execute("INSERT INTO contact(Name,Family,PhoneNumber,Address)VALUES (?,?,?,?)", entities)
        self.con.commit()

    def Remove(self, contactID):
        self.cursorObj.execute(f"DELETE FROM contact WHERE ID='{contactID}'")
        self.con.commit()

    def Update(self, contactID, name, family, phonenumber,adress):
        self.cursorObj.execute(f"UPDATE contact SET Name='{name}',Family='{family}',PhoneNumber='{phonenumber}',Adress='{adress}' WHERE ID='{contactID}'")
        self.con.commit()

    def SearchByID(self, contactID):
        self.cursorObj.execute(f"SELECT * FROM contact WHERE ID='{contactID}'")

        rows = self.cursorObj.fetchall()

        return rows

    def SearchByName(self, name):
        self.cursorObj.execute(f"SELECT * FROM contact WHERE Name='{name}'")

        rows = self.cursorObj.fetchall()

        return rows

    def SearchByFamily(self, family):
        self.cursorObj.execute(f"SELECT * FROM contact WHERE Family='{family}'")

        rows = self.cursorObj.fetchall()

        return rows

    def SearchByPhoneNumber(self, phonenumber):
        self.cursorObj.execute(f"SELECT * FROM contact WHERE PhoneNumber='{phonenumber}'")

        rows = self.cursorObj.fetchall()

        return rows

