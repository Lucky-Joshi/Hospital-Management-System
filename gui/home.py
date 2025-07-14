import customtkinter as ctk
from auth.login import login_screen
from gui.patient_gui import open_patient_form
from gui.doctor_gui import open_doctor_form
from gui.appointment_gui import open_appointment_form
from gui.admission_gui import open_admission_form
from gui.billing_gui import open_billing_form

_current_role = None  # to store current user role

def open_home_screen(role="receptionist"):
    global _current_role
    _current_role = role  # update current role

    app = ctk.CTk()
    app.geometry("400x500")
    app.title("🏥 Hospital Dashboard")

    ctk.CTkLabel(app, text=f"Dashboard ({role.capitalize()})", font=ctk.CTkFont(size=18)).pack(pady=20)

    modules = [
        ("🧍 Patients", open_patient_form),
        ("📅 Appointments", open_appointment_form),
        ("🛏️ Admissions", open_admission_form)
    ]

    if role == "admin":
        modules.insert(1, ("👨‍⚕️ Doctors", open_doctor_form))
        modules.append(("💳 Billing", open_billing_form))

    for label, func in modules:
        ctk.CTkButton(app, text=label, width=200,
                      command=lambda f=func: [app.destroy(), f()]).pack(pady=8)

    def logout():
        app.destroy()
        login_screen()

    ctk.CTkButton(app, text="🚪 Logout", fg_color="red", command=logout).pack(pady=30)
    app.mainloop()
