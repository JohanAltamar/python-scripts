import mysql.connector
import datetime
dbConnect = {
    'host':'localhost',
    'user':'johanaltro',
    'password':'jar12345',
    'database':'bioing_project',
    'port': 5306}

conn = mysql.connector.connect(**dbConnect)
cursor = conn.cursor()
cursor.execute("SELECT * FROM schedule_medicines")
meds = cursor.fetchall()
user = '1140857788'
print (meds)
