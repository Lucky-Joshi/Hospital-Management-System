import customtkinter as ctk
from tkinter import messagebox
from models import doctor

def open_doctor_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Doctor Management")

    from gui.home import open_home_screen
    def go_back():
        app.destroy()
        open_home_screen()

    # Top Bar
    ctk.CTkButton(app, text="← Back", width=100, command=go_back).pack(pady=5)
    ctk.CTkLabel(app, text="Add New Doctor", font=ctk.CTkFont(size=16)).pack(pady=10)

    # Input Fields
    name_entry = ctk.CTkEntry(app, placeholder_text="Name")
    name_entry.pack(pady=5)

    specialty_entry = ctk.CTkEntry(app, placeholder_text="Specialty")
    specialty_entry.pack(pady=5)

    phone_entry = ctk.CTkEntry(app, placeholder_text="Phone")
    phone_entry.pack(pady=5)

    department_entry = ctk.CTkEntry(app, placeholder_text="Department")
    department_entry.pack(pady=5)

    def submit_doctor():
        name = name_entry.get().strip()
        specialty = specialty_entry.get().strip()
        phone = phone_entry.get().strip()
        department = department_entry.get().strip()

        if name and specialty and phone:
            doctor.add_doctor(name, specialty, phone, department)
            messagebox.showinfo("Success", f"Doctor '{name}' added.")
            app.destroy()
            open_doctor_form()  # refresh
        else:
            messagebox.showerror("Error", "Name, Specialty, and Phone are required.")

    ctk.CTkButton(app, text="Add Doctor", command=submit_doctor).pack(pady=10)

    # Divider
    ctk.CTkLabel(app, text="All Doctors", font=ctk.CTkFont(size=14)).pack(pady=10)

    # Display All Doctors
    doc_listbox = ctk.CTkTextbox(app, width=400, height=200)
    doc_listbox.pack(pady=10)

    all_doctors = doctor.get_all_doctors()
    if all_doctors:
        for d in all_doctors:
            doc_info = f"🧑‍⚕️ {d['name']} | {d['specialty']} | {d['phone']} | {d['department']}\n"
            doc_listbox.insert("end", doc_info)
    else:
        doc_listbox.insert("end", "No doctors found.")

    app.mainloop()
