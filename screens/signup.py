import customtkinter as ctk
from tkinter import messagebox, StringVar
import mysql.connector
from PIL import Image
from db_connection import get_connection
import os
from tkinter import Canvas

def open_signup():
    from screens.login import open_login
    from screens.option import open_option

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.title("Sign Up")
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


    frame = ctk.CTkFrame(win, width=600, height=490, fg_color="#1f2a38", corner_radius=20)
    frame.place(x=300, y=100)
    frame.pack_propagate(False)

    signup_label = ctk.CTkLabel(frame, text="SIGN UP", font=("Arial", 35, "bold"), text_color="white")
    signup_label.place(x=230, y=35)

    username_label = ctk.CTkLabel(frame, text="Username:", font=("Arial", 20), text_color="white")
    username_label.place(x=100, y=100)
    txt_uname = ctk.CTkEntry(frame, placeholder_text="Enter Username", font=("Arial", 18), width=250, height=40, fg_color="#7C8C90", text_color="black")
    txt_uname.place(x=220, y=100)

    email_label = ctk.CTkLabel(frame, text="Email:", font=("Arial", 20), text_color="white")
    email_label.place(x=100, y=160)
    txt_email = ctk.CTkEntry(frame, placeholder_text="Enter Email", show="*", font=("Arial", 18), width=250, height=40, fg_color="#7C8C90", text_color="black")
    txt_email.place(x=220, y=160)

    password_label = ctk.CTkLabel(frame, text="Password:", font=("Arial", 20), text_color="white")
    password_label.place(x=100, y=230)
    txt_pass = ctk.CTkEntry(frame, placeholder_text="Enter Password", show="*", font=("Arial", 18), width=250, height=40, fg_color="#7C8C90", text_color="black")
    txt_pass.place(x=220, y=230)

    gender_label = ctk.CTkLabel(frame, text="Gender:", font=("Arial", 20), text_color="white")
    gender_label.place(x=100, y=300)
    gender = StringVar(value="M")
    ctk.CTkRadioButton(frame, text="Male", variable=gender, value="M", font=("Arial", 18)).place(x=220, y=300)
    ctk.CTkRadioButton(frame, text="Female", variable=gender, value="F", font=("Arial", 18)).place(x=320, y=300)

    age_label = ctk.CTkLabel(frame, text="Age:", font=("Arial", 20), text_color="white")
    age_label.place(x=100, y=350)
    age_slider = ctk.CTkSlider(frame, from_=14, to=55, width=200)
    age_slider.place(x=220, y=360)
    age_value_label = ctk.CTkLabel(frame, text="14", font=("Arial", 18))
    age_value_label.place(x=440, y=350)
    age_slider.configure(command=lambda v: age_value_label.configure(text=str(int(v))))

    def signup():
        username = txt_uname.get()
        email = txt_email.get()
        password = txt_pass.get()
        age = int(age_slider.get())
        genderval = gender.get()

        if not (username and email and password):
            messagebox.showerror("Error", "Please fill all fields!")
            return

        conn = get_connection()
        if not conn:
            messagebox.showerror("Error", "Database connection failed!")
            return

        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, email, password, age, gender) VALUES (%s, %s, %s, %s, %s)",
                (username, email, password, age, genderval))
            conn.commit()
            messagebox.showinfo("Success", f"User {username} signed up successfully!")
            win.destroy()
            open_option()
        except mysql.connector.Error as err:
            if err.errno == 1062:
                messagebox.showerror("Error", "Username or email already exists!")
            else:
                messagebox.showerror("Error", f"Database error: {err}")
        finally:
            cursor.close()
            conn.close()

    ctk.CTkButton(frame, text="SIGN UP", font=("Arial", 20, "bold"),fg_color="#4a90e2", hover_color="#357ABD", width=150, height=45, command=signup).place(x=330, y=415)
    ctk.CTkButton(frame, text="BACK TO LOGIN", font=("Arial", 20, "bold"), width=200, height=45,fg_color="#4a90e2", hover_color="#357ABD",
                  command=lambda: [win.destroy(), open_login()]).place(x=110, y=415)

    win.mainloop()
