import customtkinter as ctk
from tkinter import messagebox
from models import admission
from gui.home import open_home_screen, _current_role

def open_admission_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Admissions")

    ctk.CTkButton(app, text="← Back", command=lambda: [app.destroy(), open_home_screen(_current_role)]).pack(pady=5)
    ctk.CTkLabel(app, text="Admit Patient", font=ctk.CTkFont(size=16)).pack(pady=10)

    entries = {}
    for ph in ["Patient Name", "Room Number", "Room Type", "Reason for Admission"]:
        entries[ph] = ctk.CTkEntry(app, placeholder_text=ph)
        entries[ph].pack(pady=5)

    def admit():
        name = entries["Patient Name"].get().strip()
        room = entries["Room Number"].get().strip()
        rtype = entries["Room Type"].get().strip()
        reason = entries["Reason for Admission"].get().strip()

        if not name or not room:
            messagebox.showerror("Missing", "Name and Room Number required.")
            return
        admission.admit_patient(name, room, rtype, reason)
        messagebox.showinfo("Success", f"{name} admitted.")
        app.destroy()
        open_home_screen(_current_role)

    ctk.CTkButton(app, text="Admit Patient", command=admit).pack(pady=10)
    ctk.CTkLabel(app, text="Currently Admitted Patients").pack(pady=5)
    tb = ctk.CTkTextbox(app, width=450, height=180)
    tb.pack()
    for a in admission.get_active_admissions():
        tb.insert("end", f"{a['patient_name']} | Room {a['room_number']} | {a['room_type']} | {a['admission_date']}\n")

    discharge_entry = ctk.CTkEntry(app, placeholder_text="Enter Patient Name to Discharge")
    discharge_entry.pack(pady=5)

    def discharge():
        name = discharge_entry.get().strip()
        if name:
            result = admission.discharge_patient(name)
            if result.modified_count:
                messagebox.showinfo("Discharged", f"{name} has been discharged.")
                app.destroy()
                open_home_screen(_current_role)
            else:
                messagebox.showwarning("Not Found", f"No active admission for '{name}'.")
        else:
            messagebox.showerror("Missing", "Patient name required.")

    ctk.CTkButton(app, text="Discharge", command=discharge).pack(pady=10)
    app.mainloop()
