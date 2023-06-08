header = input("Enter header : ")
par = input("Enter header : ")

html = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

open("homepage.html", "w").write(html)
