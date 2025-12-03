import mysql.connector
from tkinter import messagebox

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nimai@18",
            database="csproject"
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Cannot connect: {e}")
        return None