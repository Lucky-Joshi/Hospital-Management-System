import customtkinter as ctk
from tkinter import messagebox
from models import doctor
from gui.home import open_home_screen, _current_role

def open_doctor_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Doctor Management")

    ctk.CTkButton(app, text="← Back", width=100, command=lambda: [app.destroy(), open_home_screen(_current_role)]).pack(pady=5)
    ctk.CTkLabel(app, text="Add New Doctor", font=ctk.CTkFont(size=16)).pack(pady=10)

    entries = {}
    for label in ["Name", "Specialty", "Phone", "Department"]:
        entries[label] = ctk.CTkEntry(app, placeholder_text=label)
        entries[label].pack(pady=5)

    def submit():
        vals = {k.lower(): v.get().strip() for k, v in entries.items()}
        if vals["name"] and vals["specialty"] and vals["phone"]:
            doctor.add_doctor(**vals)
            messagebox.showinfo("Success", f"Doctor '{vals['name']}' added.")
            app.destroy()
            open_home_screen(_current_role)
        else:
            messagebox.showerror("Error", "Name, Specialty, and Phone are required.")

    ctk.CTkButton(app, text="Add Doctor", command=submit).pack(pady=10)

    ctk.CTkLabel(app, text="All Doctors", font=ctk.CTkFont(size=14)).pack(pady=10)
    tb = ctk.CTkTextbox(app, width=400, height=200)
    tb.pack(pady=10)

    for d in doctor.get_all_doctors():
        tb.insert("end", f"{d['name']} | {d['specialty']} | {d['phone']} | {d['department']}\n")

    app.mainloop()
