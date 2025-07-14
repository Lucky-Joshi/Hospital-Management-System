import customtkinter as ctk
from tkinter import messagebox
from models import admission

def open_admission_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Admissions")

    from gui.home import open_home_screen
    def back(): app.destroy(); open_home_screen()
    ctk.CTkButton(app, text="← Back", command=back).pack(pady=5)

    ctk.CTkLabel(app, text="Admit Patient", font=ctk.CTkFont(size=16)).pack(pady=10)

    name_entry = ctk.CTkEntry(app, placeholder_text="Patient Name")
    room_entry = ctk.CTkEntry(app, placeholder_text="Room Number")
    type_entry = ctk.CTkEntry(app, placeholder_text="Room Type")
    reason_entry = ctk.CTkEntry(app, placeholder_text="Reason for Admission")

    for e in [name_entry, room_entry, type_entry, reason_entry]:
        e.pack(pady=5)

    def admit():
        name = name_entry.get()
        room = room_entry.get()
        rtype = type_entry.get()
        reason = reason_entry.get()
        if not name or not room:
            messagebox.showerror("Missing", "Patient Name and Room Number are required.")
            return
        admission.admit_patient(name, room, rtype, reason)
        messagebox.showinfo("Success", f"{name} admitted.")
        app.destroy(); open_admission_form()

    ctk.CTkButton(app, text="Admit Patient", command=admit).pack(pady=10)

    ctk.CTkLabel(app, text="Currently Admitted Patients").pack(pady=5)
    admit_box = ctk.CTkTextbox(app, width=450, height=180)
    admit_box.pack()

    for a in admission.get_active_admissions():
        line = f"🛏 {a['patient_name']} | Room {a['room_number']} | {a['room_type']} | {a['admission_date']}\n"
        admit_box.insert("end", line)

    # Discharge
    ctk.CTkLabel(app, text="Discharge Patient").pack(pady=5)
    discharge_entry = ctk.CTkEntry(app, placeholder_text="Enter Patient Name")
    discharge_entry.pack(pady=5)

    def discharge():
        name = discharge_entry.get().strip()
        if name:
            result = admission.discharge_patient(name)
            if result.modified_count:
                messagebox.showinfo("Discharged", f"{name} has been discharged.")
                app.destroy(); open_admission_form()
            else:
                messagebox.showwarning("Not Found", f"No active admission for '{name}'.")
        else:
            messagebox.showerror("Missing", "Patient name required.")

    ctk.CTkButton(app, text="Discharge", command=discharge).pack(pady=10)

    app.mainloop()
