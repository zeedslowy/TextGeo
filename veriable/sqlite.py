import sqlite3

# Bağlantı oluştur
connection = sqlite3.connect("example.db")

# Cursor (İşaretçi) oluştur
cursor = connection.cursor()

# Örnek sorgu
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
print(result)

# Bağlantıyı kapat
connection.close()
