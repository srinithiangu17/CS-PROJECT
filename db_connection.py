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
    
def insert_workout(username, duration, intensity):
    conn = get_connection()
    if not conn:
        return False

    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO workouts (username, workout_date, duration, intensity)
            VALUES (%s, CURDATE(), %s, %s)
        """, (username, int(duration), intensity))
        conn.commit()
        return True
    except Exception as e:
        print("Insert workout error:", e)
        return False
    finally:
        conn.close()
