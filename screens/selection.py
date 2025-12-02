#selection.py

from tkinter.ttk import Label
from tkinter import Canvas
from PIL import Image, ImageTk
import customtkinter as ctk

import customtkinter as ctk

class Shared:
    clicked1 = None   # Duration
    clicked2 = None   # Intensity
    clicked3 = None   # Equipment

def open_selection():
    from workout import open_work
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.geometry("700x550")
    win.title("BOYD - Preferences")

    # ===== MAIN FRAME =====
    frame = ctk.CTkFrame(win, width=600, height=480, corner_radius=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ------------ TITLE ------------
    title = ctk.CTkLabel(
        frame,
        text="SELECT YOUR PREFERENCES",
        font=("Arial Rounded MT Bold", 28)
    )
    title.pack(pady=20)

    # ------------ DURATION ------------
    duration_label = ctk.CTkLabel(frame, text="DURATION:", font=("Arial", 20))
    duration_label.pack(pady=(10, 0))

    duration_seg = ctk.CTkSegmentedButton(
        frame,
        values=["30", "45", "60"],     # ONLY ONE CAN BE SELECTED
        font=("Arial", 16),
        height=45
    )
    duration_seg.set("30")            # default
    duration_seg.pack(pady=5)

    # ------------ INTENSITY ------------
    intensity_label = ctk.CTkLabel(frame, text="INTENSITY:", font=("Arial", 20))
    intensity_label.pack(pady=(20, 0))

    intensity_seg = ctk.CTkSegmentedButton(
        frame,
        values=["easy", "medium", "hard"],   # ONLY ONE CAN BE SELECTED
        font=("Arial", 16),
        height=45
    )
    intensity_seg.set("easy")               # default
    intensity_seg.pack(pady=5)

    # ------------ EQUIPMENT ------------
    eq_label = ctk.CTkLabel(frame, text="EQUIPMENT:", font=("Arial", 20))
    eq_label.pack(pady=(20, 0))

    eq_seg = ctk.CTkSegmentedButton(
        frame,
        values=["yes", "no"],          # ONLY ONE CAN BE SELECTED
        font=("Arial", 16),
        height=45
    )
    eq_seg.set("no")                  # default
    eq_seg.pack(pady=5)

    # ------------ NEXT BUTTON ------------
    def save_and_next():
        Shared.clicked1 = duration_seg.get()
        Shared.clicked2 = intensity_seg.get()
        Shared.clicked3 = eq_seg.get()

        print("--- USER SELECTED ---")
        print("Duration:", Shared.clicked1)
        print("Intensity:", Shared.clicked2)
        print("Equipment:", Shared.clicked3)

        win.destroy()  # replace with open_work()

    next_button = ctk.CTkButton()
        
    next_button.pack(pady=30)

    win.mainloop()

open_selection()