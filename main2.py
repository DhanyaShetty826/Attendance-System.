import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="divya",
        password="divyasri@1606",
        database="attendance_system"
    )
    if conn.is_connected():
        print("Database connected successfully.")
except Error as e:
    print(f"Error: {e}")
    exit()
