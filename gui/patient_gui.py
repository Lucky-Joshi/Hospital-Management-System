import customtkinter as ctk
from tkinter import messagebox
from models import patient

def open_patient_form():
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Patient Management")

    ctk.CTkLabel(app, text="Name").pack()
    name_entry = ctk.CTkEntry(app)
    name_entry.pack()

    ctk.CTkLabel(app, text="Gender").pack()
    gender_entry = ctk.CTkEntry(app)
    gender_entry.pack()

    ctk.CTkLabel(app, text="Phone").pack()
    phone_entry = ctk.CTkEntry(app)
    phone_entry.pack()

    ctk.CTkLabel(app, text="Address").pack()
    address_entry = ctk.CTkEntry(app)
    address_entry.pack()

    def submit():
        name = name_entry.get()
        gender = gender_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        if name and phone:
            patient.add_patient(name, gender, phone, address)
            messagebox.showinfo("Success", "Patient added successfully.")
            app.destroy()
        else:
            messagebox.showwarning("Missing Info", "Name and Phone are required.")

    ctk.CTkButton(app, text="Submit", command=submit).pack(pady=10)

    app.mainloop()
