import customtkinter as ctk
from tkinter import messagebox
from models import patient
from gui.home import open_home_screen
from gui.home import _current_role as current_role

def open_patient_form():
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Patient Management")

    ctk.CTkButton(app, text="← Back", width=100, command=lambda: [app.destroy(), open_home_screen(current_role)]).pack(pady=5)

    entries = {}
    for label in ["Name", "Gender", "Phone", "Address"]:
        ctk.CTkLabel(app, text=label).pack()
        entries[label] = ctk.CTkEntry(app)
        entries[label].pack(pady=5)

    def submit():
        data = {k.lower(): v.get().strip() for k, v in entries.items()}
        if data["name"] and data["phone"]:
            patient.add_patient(**data)
            messagebox.showinfo("Success", "Patient added.")
            app.destroy()
            open_home_screen(current_role)
        else:
            messagebox.showwarning("Missing Info", "Name and Phone are required.")

    ctk.CTkButton(app, text="Submit", command=submit).pack(pady=10)
    app.mainloop()
