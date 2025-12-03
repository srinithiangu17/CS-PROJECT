import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from db_connection import get_connection


# FETCH DATA
def get_workout_data(username, conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT workout_date, duration, intensity FROM workouts WHERE username = %s", (username,))
        return cur.fetchall()
    except:
        return []

def get_durations_data(username, conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT workout_date, duration FROM workouts WHERE username = %s", (username,))
        return cur.fetchall()
    except:
        return []

# SHOW PROGRESS GUI
def show_progress(username):
    root = tk.Tk()
    root.title(f"PROGRESS - {username.upper()}")
    root.geometry("1000x700")

    # Canvas for gradient background
    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # DRAW GRADIENT
    def draw_gradient():
        canvas.delete("gradient")  # only remove old gradient lines
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        r1, g1, b1 = root.winfo_rgb("#020b1b")
        r2, g2, b2 = root.winfo_rgb("#17253d")
        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height
        for i in range(height):
            nr = int(r1 + r_ratio * i)
            ng = int(g1 + g_ratio * i)
            nb = int(b1 + b_ratio * i)
            color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
            canvas.create_line(0, i, width, i, fill=color, tags="gradient")

    # UPDATE ON RESIZE
    def update_gradient(event):
        draw_gradient()

    canvas.bind("<Configure>", update_gradient)

    # DATABASE
    conn = get_connection()
    if not conn:
        return

    workouts = get_workout_data(username, conn)
    duration = get_durations_data(username, conn)

    # LEFT FRAME - WORKOUT TABLE
    left_frame = tk.Frame(canvas, bg="white")
    left_window = canvas.create_window(10, 10, anchor="nw", window=left_frame)

    label = tk.Label(left_frame, text="Daily Workouts", font=("Arial", 18, "bold"), bg="white")
    label.pack(pady=10)

    tree = ttk.Treeview(left_frame, columns=("Date", "Duration", "Intensity"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Duration", text="Duration (min)")
    tree.heading("Intensity", text="Intensity")
    tree.column("Date", width=120)
    tree.column("Duration", width=100, anchor="center")
    tree.column("Intensity", width=100, anchor="center")

    for row in workouts:
        tree.insert("", "end", values=row)
    tree.pack(fill="both", expand=True)

    # RIGHT FRAME 
    right_frame = tk.Frame(canvas, bg="black")
    right_window = canvas.create_window(500, 60, anchor="nw", window=right_frame)

    fig = Figure(figsize=(5, 3), dpi=100)
    ax = fig.add_subplot(111)
    if duration:
        dates = [row[0] for row in duration]
        dur = [row[1] for row in duration]
        ax.plot(dates, dur, marker='o', color='black')
        ax.set_title("progress over time")
        ax.set_ylabel("duration (min)")
    else:
        ax.text(0.5, 0.5, "No Data", ha="center", va="center")

    chart_canvas = FigureCanvasTkAgg(fig, master=right_frame)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().pack(fill="both", expand=True)

    root.mainloop()

'''# MAIN
if __name__ == "__main__":
    username = "test"
    show_progress(username)
'''


