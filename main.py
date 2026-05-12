import pyodbc

server = 'localhost'
database = 'beton'
username = 'tichnut'
password = '1234'
# 1. הגדר את פרטי החיבור שלך
server = 'localhost'  # או 'localhost\SQLEXPRESS' אם זה SQL Express
database = 'beton'
username = 'tichnut'  # שם המשתמש שלך ב-SQL Server
password = 'הסיסמה שלך כאן'





conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=beton;Trusted_Connection=yes;'
)
cursor = conn.cursor()
# שאילתה לשליפת כל הלקוחות
cursor.execute("SELECT id, name, phone FROM Customers")

# שליפת כל השורות
rows = cursor.fetchall()

# הדפסת התוצאות
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Phone: {row.phone}")

print("ppppppppppp")
print("aaaaa")


