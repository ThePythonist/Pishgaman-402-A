import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

students = [
    {"name": "Amirali", "code": "40211", "job": "Backend Developer"},
    {"name": "Parsa", "code": "40212", "job": "Frontend Developer"},
    {"name": "Mehrzad", "code": "40213", "job": "Security Engineer"},
    {"name": "Mohammad Mehdi", "code": "40214", "job": "DevOps Engineer"},
    {"name": "Bahar", "code": "40214", "job": "Civil Engineer"},
    {"name": "Mehrdad", "code": "40214", "job": "Data Engineer"},
]

cur.execute("CREATE TABLE IF NOT EXISTS employees (name,code,job);")

# for person in students:
#     cur.execute(f"INSERT INTO employees VALUES (?,?,?)", (person['name'], person['code'], person['job']))

# for person in students:
#     cur.execute(f"INSERT INTO employees VALUES ({person['name']},{person['name']},{person['name']}")


cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    print(i)
# print(records)

con.commit()
con.close()
print('Done')
