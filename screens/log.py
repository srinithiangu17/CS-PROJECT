import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from db_connection import get_connection
from screens.shared_data import SharedData
import matplotlib.dates as mdates
from datetime import datetime
from screens.option import open_option
def get_workout_data(username, conn):
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT workout_date, duration, intensity FROM workouts WHERE username = %s ORDER BY workout_date ASC",
            (username,))
        return cur.fetchall()
    except:
        return []

def get_durations_data(username, conn):
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT workout_date, duration FROM workouts WHERE username = %s ORDER BY workout_date ASC",
            (username,))
        return cur.fetchall()
    except:
        return []

def show_progress(username):
    root = tk.Tk()
    root.title(f"PROGRESS - {username.upper()}")
    root.geometry("1200x800")

    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def draw_gradient():
        canvas.delete("gradient")
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

    def update_gradient(event):
        draw_gradient()

    canvas.bind("<Configure>", update_gradient)

    conn = get_connection()
    if not conn:
        return

    workouts = get_workout_data(username, conn)
    duration = get_durations_data(username, conn)


    left_frame = tk.Frame(canvas, bg="black")
    canvas.create_window(10, 10, anchor="nw", window=left_frame)

    label = tk.Label(left_frame, text="Daily Workouts", font=("Arial", 18, "bold"), bg="black", fg="white")
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


    right_frame = tk.Frame(canvas, bg="black")
    canvas.create_window(500, 70, anchor="nw", window=right_frame)

    fig = Figure(figsize=(5, 5), dpi=100, facecolor='black')
    ax = fig.add_subplot(111, facecolor='black')

    if duration:

        dates = [row[0] for row in duration]
        dur = [row[1] for row in duration]


        intensities = [row[2] for row in workouts]


        combined = sorted(zip(dates, dur, intensities), key=lambda x: x[0])
        dates, dur, intensities = zip(*combined)


        color_map = {
            "EASY": "green",
            "MODERATE": "yellow",
            "HARD": "red"
        }

        point_colors = [color_map.get(i.upper(), "white") for i in intensities]


        ax.plot(dates, dur, color="white")

        ax.scatter(dates, dur, color=point_colors, s=80)

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_ha('right')

        ax.set_title("PROGRESS", color='white', fontsize=20)
        ax.set_ylabel("Duration (min)", color='white')
        ax.set_xlabel("Date", color='white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.grid(True, color="white", linestyle="--", alpha=0.3)

    else:
        ax.text(0.5, 0.5, "No Data", ha="center", va="center", color="white")

    chart_canvas = FigureCanvasTkAgg(fig, master=right_frame)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().pack(fill="both", expand=True)
    back_button = ctk.CTkButton(root, text="BACK TO OPTIONS",
            fg_color="#4a90e2", hover_color="#357ABD",
            font=("Arial Rounded MT Bold", 28), text_color="white",
            command=lambda: [root.destroy(), open_option(username)]
        )
    back_button.place(x=20, y=350)

    root.mainloop()