import sqlite3

class data:
    def __init__(self, database_name):
        self.con = sqlite3.connect(f'./{database_name}')

    def LoadAll(con):

        cursorObj = con.cursor()

        cursorObj.execute('SELECT * FROM contact')

        rows = cursorObj.fetchall()

        return rows

    def Add(con,name,family,phonenumber):
        entities = (name,family,phonenumber)
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO contact(Name,Family,PhoneNumber)VALUES (?,?,?)",entities)
        con.commit()



    def Remove(con,contactID):
        cursorObj = con.cursor()
        cursorObj.execute(f"DELETE FROM contact WHERE ID='{contactID}'")
        con.commit()

    def Update(con,contactID,name,family,phonenumber):
        cursorObj = con.cursor()
        cursorObj.execute(f"UPDATE contact SET Name='{name}',Family='{family}',PhoneNumber='{phonenumber}' WHERE ID='{contactID}'")
        con.commit()


    def SearchByID(con,contactID):
        cursorObj = con.cursor()

        cursorObj.execute(f"SELECT * FROM contact WHERE ID='{contactID}'")

        rows = cursorObj.fetchall()

        return rows

    def SearchByName(con,name):
        cursorObj = con.cursor()

        cursorObj.execute(f"SELECT * FROM contact WHERE Name='{name}'")

        rows = cursorObj.fetchall()

        return rows

    def SearchByFamily(con,family):
        cursorObj = con.cursor()

        cursorObj.execute(f"SELECT * FROM contact WHERE Family='{family}'")

        rows = cursorObj.fetchall()

        return rows

    def SearchByPhoneNumber(con,phonenumber):
        cursorObj = con.cursor()

        cursorObj.execute(f"SELECT * FROM contact WHERE PhoneNumber='{phonenumber}'")

        rows = cursorObj.fetchall()

        return rows
