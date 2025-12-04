import customtkinter as ctk
from tkinter import messagebox
from tkinter.ttk import Label
import os
from PIL import Image, ImageTk
from tkinter import Canvas
from screens.shared_data import SharedData
from db_connection import insert_workout


class Shared:
    clicked1 = None
    clicked2 = None
    clicked3 = None

def open_selection(username):
    SharedData.username = username    
    from screens.option import open_option
    from screens.workout import open_work

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


    def duration(frame1):
        Shared.clicked1 = ctk.StringVar(value="30")
        seg = ctk.CTkSegmentedButton(
            frame1,
            values=["30", "45", "60"],
            variable=Shared.clicked1,
            font=("Arial Rounded MT Bold", 20),
            selected_color="#4a90e2",
            unselected_color="#1f2a38",
            text_color="white"
        )
        return seg

    def intensity(frame1):
        Shared.clicked2 = ctk.StringVar(value="EASY")
        seg = ctk.CTkSegmentedButton(
            frame1,
            values=["EASY", "MODERATE", "HARD"],
            variable=Shared.clicked2,
            font=("Arial Rounded MT Bold", 20),
            selected_color="#4a90e2",
            unselected_color="#1f2a38",
            text_color="white"
        )
        return seg

    def equipment(frame1):
        Shared.clicked3 = ctk.StringVar(value="NO")
        seg = ctk.CTkSegmentedButton(
            frame1,
            values=["YES", "NO"],
            variable=Shared.clicked3,
            font=("Arial Rounded MT Bold", 20),
            selected_color="#4a90e2",
            unselected_color="#1f2a38",
            text_color="white"
        )
        return seg


    def createMenu(root):
        win = root
        win.title("SELECTION")
        win.geometry("1200x800")

        canvas = Canvas(win, width=500, height=300, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        frame1 = ctk.CTkFrame(win, width=550, height=500, fg_color="#1f2a38", corner_radius=20)
        frame1.place(x=300, y=200)

        workout_label = ctk.CTkLabel(frame1, text="SELECT YOUR PREFERENCES",
                                    font=("Arial Rounded MT Bold", 32),
                                    text_color="white")

        duration_label = ctk.CTkLabel(frame1, text="DURATION:", font=("Arial Rounded MT Bold", 20), text_color="white")
        duration_entry = duration(frame1)

        intensity_label = ctk.CTkLabel(frame1, text="INTENSITY:", font=("Arial Rounded MT Bold", 20), text_color="white")
        intensity_entry = intensity(frame1)

        equipment_label = ctk.CTkLabel(frame1, text="EQUIPMENT:", font=("Arial Rounded MT Bold", 20), text_color="white")
        equipment_entry = equipment(frame1)

        
        def save_and_next(win, open_work):
            Shared.clicked1 = Shared.clicked1.get()
            Shared.clicked2 = Shared.clicked2.get()  
            Shared.clicked3 = Shared.clicked3.get()   

            win.destroy()
            open_work()

        next_button_widget = ctk.CTkButton(
            frame1, text="NEXT",
            fg_color="#4a90e2", hover_color="#357ABD",
            font=("Arial Rounded MT Bold", 28), text_color="white",
            command=lambda: [save_and_next(win, open_work)]
        )

        back_button = ctk.CTkButton(
            frame1, text="BACK TO OPTIONS",
            fg_color="#4a90e2", hover_color="#357ABD",
            font=("Arial Rounded MT Bold", 28), text_color="white",
            command=lambda: [win.destroy(), open_option()]
        )



        workout_label.place(x=10, y=5)

        duration_label.place(x=20, y=120)
        duration_entry.place(x=200, y=115)

        intensity_label.place(x=20, y=200)
        intensity_entry.place(x=200, y=195)

        equipment_label.place(x=20, y=280)
        equipment_entry.place(x=200, y=275 )

        next_button_widget.place(x=360, y=350)
        back_button.place(x=20, y=350)



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
            draw_gradient(canvas, "#020b1b", "#17253d")
            draw_gradient(canvas, "#06193b", "#17253d")

        canvas.bind("<Configure>", update_gradient)

        win.mainloop()
    createMenu(ctk.CTk()) 
