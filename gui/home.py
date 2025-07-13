import customtkinter as ctk
from gui.patient_gui import open_patient_form
from gui.doctor_gui import open_doctor_form
from gui.appointment_gui import open_appointment_form
from gui.admission_gui import open_admission_form
from gui.billing_gui import open_billing_form

def open_home_screen(role="receptionist"):
    app = ctk.CTk()
    app.geometry("400x500")
    app.title("🏥 Hospital Dashboard")

    ctk.CTkLabel(app, text=f"Hospital Dashboard ({role.capitalize()})", font=ctk.CTkFont(size=18)).pack(pady=20)

    # Build module list based on role
    modules = [
        ("🧍 Patients", open_patient_form),
        ("📅 Appointments", open_appointment_form),
        ("🛏️ Admissions", open_admission_form)
    ]

    if role == "admin":
        modules.insert(1, ("👨‍⚕️ Doctors", open_doctor_form))
        modules.append(("💳 Billing", open_billing_form))

    # Create navigation buttons
    for label, func in modules:
        ctk.CTkButton(app, text=label, width=200, command=lambda f=func: [app.destroy(), f()]).pack(pady=8)

    # Safe import to break circular dependency
    def logout():
        import auth.login
        app.destroy()
        auth.login.login_screen()

    ctk.CTkButton(app, text="🚪 Logout", fg_color="red", command=logout).pack(pady=30)
    app.mainloop()
