import customtkinter as ctk
from tkinter import messagebox
from models import appointment
from gui.home import open_home_screen, _current_role

def open_appointment_form():
    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Appointment Management")

    ctk.CTkButton(app, text="← Back", command=lambda: [app.destroy(), open_home_screen(_current_role)]).pack(pady=5)
    ctk.CTkLabel(app, text="Book Appointment", font=ctk.CTkFont(size=16)).pack(pady=10)

    entries = {}
    for ph in ["Patient Name", "Doctor Name", "Date (YYYY-MM-DD)", "Time (e.g., 10:00 AM)", "Reason"]:
        entries[ph] = ctk.CTkEntry(app, placeholder_text=ph)
        entries[ph].pack(pady=5)

    def book():
        vals = {k: v.get().strip() for k, v in entries.items()}
        if not all([vals["Patient Name"], vals["Doctor Name"], vals["Date (YYYY-MM-DD)"], vals["Time (e.g., 10:00 AM)"]]):
            messagebox.showerror("Missing", "All fields except Reason are required.")
            return
        appointment.book_appointment(vals["Patient Name"], vals["Doctor Name"],
                                     vals["Date (YYYY-MM-DD)"], vals["Time (e.g., 10:00 AM)"], vals["Reason"])
        messagebox.showinfo("Success", "Appointment booked.")
        app.destroy()
        open_home_screen(_current_role)

    ctk.CTkButton(app, text="Book Appointment", command=book).pack(pady=10)
    ctk.CTkLabel(app, text="All Appointments").pack(pady=5)
    tb = ctk.CTkTextbox(app, width=450, height=200)
    tb.pack()
    for a in appointment.get_all_appointments():
        tb.insert("end", f"{a['patient_name']} with {a['doctor_name']} on {a['date']} at {a['time']} ({a['status']})\n")
    app.mainloop()
