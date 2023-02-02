import  sqlite3
from src.Backend import PhoneBookBack

con = sqlite3.connect(r'../Backend/PBDB.db')

back = PhoneBookBack.data("PBDB.db")
back.Add("ali","moosavi","0123456978")



#print(load)

