import sqlite3

con = sqlite3.connect(r'./PBDB.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM contact')

    rows = cursorObj.fetchall()

    # for row in rows:
    #
    #     data = [].append(row)
    # return data
    return rows

bac = sql_fetch(con)
for person in range(len(bac)):
    for item in range(1,4):
        print(bac[person][item])
    print("--==--==--==--")

