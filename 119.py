import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

rec = {"name": "Ali", "code": 40318, "job": "Database Admin"}
rec = tuple(rec.values())

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()


# for i in records:
#     print(i)

# cur.execute("DELETE FROM employees;")

def save():
    cur.execute(f"INSERT INTO employees(name,code,job) VALUES (?,?,?);", (rec[0], rec[1], rec[2]))


users = [i[1:] for i in records]
# for i in users :
#     print(i)
#
if rec in users:
    print("User already exists in db")
else:
    save()
    print("User added to database")

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    print(i)

print(len(records), "Users exist in db")

con.commit()
con.close()
