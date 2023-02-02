import sqlite3

con = sqlite3.connect(r'./PBDB.db')

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






