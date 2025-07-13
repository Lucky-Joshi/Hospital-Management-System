import customtkinter as ctk
from tkinter import messagebox
from models import user
from gui.home import open_home_screen

def login_screen():
    app = ctk.CTk()
    app.geometry("300x300")
    app.title("Login")

    ctk.CTkLabel(app, text="User Login", font=ctk.CTkFont(size=16)).pack(pady=15)

    username_entry = ctk.CTkEntry(app, placeholder_text="Username")
    password_entry = ctk.CTkEntry(app, placeholder_text="Password", show="*")
    username_entry.pack(pady=10)
    password_entry.pack(pady=10)

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        user_data = user.validate_user(username, password)
        if user_data:
            messagebox.showinfo("Welcome", f"Logged in as {user_data['role'].capitalize()}")
            app.destroy()
            open_home_screen(user_data['role'])
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    ctk.CTkButton(app, text="Login", command=handle_login).pack(pady=15)

    def open_signup():
        import auth.signup  # 🔁 local import to avoid circular dependency
        app.destroy()
        auth.signup.signup_screen()

    ctk.CTkButton(app, text="Create Account", command=open_signup).pack()
    app.mainloop()
