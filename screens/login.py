import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from db_connection import get_connection
import os
from tkinter import Canvas

def open_login():
    from screens.signup import open_signup
    from screens.option import open_option
    

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    win = ctk.CTk()
    win.title("Login")
    win.geometry("1200x800")
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


    frame = ctk.CTkFrame(win, corner_radius=15, fg_color="#1f2a38", width=500, height=320)
    frame.place(x=370, y=180)
    frame.pack_propagate(False)

    login_label = ctk.CTkLabel(frame, text="LOGIN", font=("Arial Rounded MT Bold", 32), text_color="white")
    username_label = ctk.CTkLabel(frame, text="Username:", font=("Arial", 20), text_color="white")
    txt_uname = ctk.CTkEntry(frame, placeholder_text="Enter username", font=("Arial", 18), width=250, height=40, fg_color="#7C8C90", text_color="black")

    password_label = ctk.CTkLabel(frame, text="Password:", font=("Arial", 20), text_color="white")
    txt_pass = ctk.CTkEntry(frame, placeholder_text="Enter password", show="*", font=("Arial", 18), width=250, height=40, fg_color="#7C8C90", text_color="black")

    def login():
        username = txt_uname.get()
        password = txt_pass.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
                result = cursor.fetchone()
            except Exception as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                result = None
            finally:
                cursor.close()
                conn.close()

            if not result:
                messagebox.showerror("Error", "Invalid username or password!")
                txt_pass.delete(0, 'end')
            else:
                from screens.shared_data import SharedData
                SharedData.username = username
 
                win.destroy()
                open_option(username)
                
        else:
            messagebox.showerror("Connection Error", "Database connection failed.")

    login_button = ctk.CTkButton(frame, text="LOGIN", font=("Arial Bold", 20),
                                 width=150, height=45, 
                                 text_color="white",fg_color="#4a90e2", hover_color="#357ABD",
                                 command=lambda:[login()])

    signup_button = ctk.CTkButton(frame, text="SIGN UP", font=("Arial Bold", 20),
                                  width=150, height=45, 
                                  text_color="white",fg_color="#4a90e2", hover_color="#357ABD",
                                  command=lambda: [win.destroy(), open_signup()])

    login_label.place(x=180, y=30)
    username_label.place(x=60, y=100)
    txt_uname.place(x=200, y=95)
    password_label.place(x=60, y=170)
    txt_pass.place(x=200, y=165)
    login_button.place(x=270, y=250)
    signup_button.place(x=100, y=250)

    win.mainloop()