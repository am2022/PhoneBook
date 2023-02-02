from ..Backend import PhoneBookBack
con = sqlite3.connect(r'./PBDB.db')

baeckend = PhoneBookBack.LoadAll(con)

print(baeckend)