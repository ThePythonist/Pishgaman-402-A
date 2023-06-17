import jdatetime

today = str(jdatetime.datetime.now())
today = today.split()
fullhour = today[1]


print(f"Emrooz {today[0]} ast va saat {fullhour[0:5]} ast")
