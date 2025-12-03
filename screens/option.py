import customtkinter as ctk
from PIL import Image
from screens.selection import open_selection
import os
from tkinter import Canvas
from screens.log import show_progress
def open_option(username):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.title("Options")
    win.geometry("1200x800")
    win.resizable(False, False)
    canvas = Canvas(win, width=500, height=300, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def draw_gradient(canvas, color1, color2):
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        r1, g1, b1 = win.winfo_rgb(color1)
        r2, g2, b2 = win.winfo_rgb(color2)

        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))

            hex_color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'

            canvas.create_line(0, i, width, i, fill=hex_color)
    def update_gradient(event):
        canvas.delete("all")
        draw_gradient(canvas, "#06193b", "#344b73")  

    canvas.bind("<Configure>", update_gradient)


    frame = ctk.CTkFrame(win, fg_color="#1f2a38", corner_radius=20, width=400, height=200)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    create_a_plan = ctk.CTkButton(
        frame,
        text="GENERATE A PLAN",
        font=("Arial", 24, "bold"),
        fg_color="#4a90e2",
        hover_color="#357ABD",
        text_color="white",
        width=380,
        height=80,
        corner_radius=20,
        command=lambda: [win.destroy(), open_selection()]
    )

    create_a_plan.place(x=10, y=10)
    view_progress = ctk.CTkButton(
        frame,
        text="VIEW PROGRESS",
        font=("Arial", 20, "bold"),
        fg_color="#4a90e2",
        hover_color="#357ABD",
        text_color="white",
        width=380,
        height=80,
        corner_radius=20,
        command=lambda: [win.destroy(), show_progress(username)]  # replace "test" with real username later
    )
    view_progress.place(x=10, y=110)