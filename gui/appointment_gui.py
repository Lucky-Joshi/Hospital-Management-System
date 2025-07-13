import customtkinter as ctk
from tkinter import messagebox
from models import appointment

def open_appointment_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Appointment Management")

    from gui.home import open_home_screen
    def back(): app.destroy(); open_home_screen()
    ctk.CTkButton(app, text="← Back", command=back).pack(pady=5)

    ctk.CTkLabel(app, text="Book Appointment", font=ctk.CTkFont(size=16)).pack(pady=10)

    patient_entry = ctk.CTkEntry(app, placeholder_text="Patient Name")
    doctor_entry = ctk.CTkEntry(app, placeholder_text="Doctor Name")
    date_entry = ctk.CTkEntry(app, placeholder_text="Date (YYYY-MM-DD)")
    time_entry = ctk.CTkEntry(app, placeholder_text="Time (e.g., 10:00 AM)")
    reason_entry = ctk.CTkEntry(app, placeholder_text="Reason")

    for e in [patient_entry, doctor_entry, date_entry, time_entry, reason_entry]:
        e.pack(pady=5)

    def book():
        p, d, date, time, reason = (
            patient_entry.get(), doctor_entry.get(), date_entry.get(), time_entry.get(), reason_entry.get()
        )
        if not all([p, d, date, time]):
            messagebox.showerror("Missing", "All fields except reason are required.")
            return
        appointment.book_appointment(p, d, date, time, reason)
        messagebox.showinfo("Success", "Appointment booked.")
        app.destroy(); open_appointment_form()

    ctk.CTkButton(app, text="Book Appointment", command=book).pack(pady=10)

    ctk.CTkLabel(app, text="All Appointments").pack(pady=5)
    appt_box = ctk.CTkTextbox(app, width=450, height=200)
    appt_box.pack()

    for a in appointment.get_all_appointments():
        line = f"📅 {a['patient_name']} with {a['doctor_name']} on {a['date']} at {a['time']} ({a['status']})\n"
        appt_box.insert("end", line)

    app.mainloop()
