import psycopg2

# Bağlantı oluştur
connection = psycopg2.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Cursor (İşaretçi) oluştur
cursor = connection.cursor()

# Örnek sorgu
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
print(result)

# Bağlantıyı kapat
connection.close()
