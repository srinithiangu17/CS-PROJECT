#selection.py

from tkinter.ttk import Label
from tkinter import Canvas
from PIL import Image, ImageTk
import customtkinter as ctk


class Shared:
    clicked1 = None   
    clicked2 = None   
    clicked3 = None   
def open_selection():
    from workout import open_work
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.geometry("1200x800")
    win.title("Workout Assitant - Preferences")


    frame = ctk.CTkFrame(win, width=600, height=480, corner_radius=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    
    title = ctk.CTkLabel(
        frame,
        text="SELECT YOUR PREFERENCES",
        font=("Arial Rounded MT Bold", 28)
    )
    title.pack(pady=20)


    duration_label = ctk.CTkLabel(frame, text="DURATION:", font=("Arial", 20))
    duration_label.pack(pady=(10, 0))

    duration_seg = ctk.CTkSegmentedButton(
        frame,
        values=["30", "45", "60"],    
        font=("Arial", 16),
        height=45
    )
    duration_seg.set("30")          
    duration_seg.pack(pady=5)


    intensity_label = ctk.CTkLabel(frame, text="INTENSITY:", font=("Arial", 20))
    intensity_label.pack(pady=(20, 0))

    intensity_seg = ctk.CTkSegmentedButton(
        frame,
        values=["easy", "medium", "hard"],  
        font=("Arial", 16),
        height=45
    )
    intensity_seg.set("easy")           
    intensity_seg.pack(pady=5)


    eq_label = ctk.CTkLabel(frame, text="EQUIPMENT:", font=("Arial", 20))
    eq_label.pack(pady=(20, 0))

    eq_seg = ctk.CTkSegmentedButton(
        frame,
        values=["yes", "no"],          
        font=("Arial", 16),
        height=45
    )
    eq_seg.set("no")               
    eq_seg.pack(pady=5)
    def save_and_next():
        Shared.clicked1 = duration_seg.get()
        Shared.clicked2 = intensity_seg.get()
        Shared.clicked3 = eq_seg.get()

        win.destroy()  

    next_button = ctk.CTkButton(frame, text="NEXT", fg_color="#4a90e2",
        hover_color="#357ABD",command=lambda:[save_and_next(),win.destroy(),open_work()])
        
    next_button.pack(pady=30)

    win.mainloop()

open_selection()