import  sqlite3
from src.Backend import PhoneBookBack

con = sqlite3.connect(r'../Backend/PBDB.db')
load = PhoneBookBack.LoadAll(con)

print(load)

