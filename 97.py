students = [
    {"name": "Amirali", "code": "40211", "job": "Backend Developer"},
    {"name": "Parsa", "code": "40212", "job": "Frontend Developer"},
    {"name": "Mehrzad", "code": "40213", "job": "Security Engineer"},
    {"name": "Mohammad Mehdi", "code": "40214", "job": "DevOps Engineer"},
    {"name": "Bahar", "code": "40214", "job": "Civil Engineer"},
    {"name": "Mehrdad", "code": "40214", "job": "Data Engineer"},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Student Name</th>
    <th>Student Code</th>
    <th>Student Job</th>
  </tr>

"""

for student in students:
    html += f"""
  <tr>
    <td>{student['name']}</td>
    <td>{student['code']}</td>
    <td>{student['job']}</td>
  </tr>
"""

html += """
</table>
</body>
</html>
"""
open("info.html", "w").write(html)
