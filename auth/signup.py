import customtkinter as ctk
from tkinter import messagebox
from models import user

def signup_screen():
    app = ctk.CTk()
    app.geometry("350x350")
    app.title("Sign Up")

    ctk.CTkLabel(app, text="Create New Account", font=ctk.CTkFont(size=16)).pack(pady=15)

    username_entry = ctk.CTkEntry(app, placeholder_text="Username")
    password_entry = ctk.CTkEntry(app, placeholder_text="Password", show="*")

    role_var = ctk.StringVar(value="receptionist")
    ctk.CTkLabel(app, text="Role").pack()
    role_menu = ctk.CTkOptionMenu(app, variable=role_var, values=["admin", "receptionist"])

    username_entry.pack(pady=10)
    password_entry.pack(pady=10)
    role_menu.pack(pady=5)

    def handle_signup():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if user.create_user(username, password, role):
            messagebox.showinfo("Success", f"{role.capitalize()} account created.")
            import auth.login  # 🔁 moved inside to fix circular import
            app.destroy()
            auth.login.login_screen()
        else:
            messagebox.showerror("Error", "Username already exists.")

    ctk.CTkButton(app, text="Sign Up", command=handle_signup).pack(pady=15)

    def back_to_login():
        import auth.login  # 🔁 moved inside to fix circular import
        app.destroy()
        auth.login.login_screen()

    ctk.CTkButton(app, text="Back to Login", command=back_to_login).pack()
    app.mainloop()
