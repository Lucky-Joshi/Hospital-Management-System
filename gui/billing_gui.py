import customtkinter as ctk
from tkinter import messagebox
from models import billing

def open_billing_form():
    app = ctk.CTk()
    app.geometry("600x600")
    app.title("Billing Management")

    from gui.home import open_home_screen
    def back(): app.destroy(); open_home_screen()

    ctk.CTkButton(app, text="← Back", command=back).pack(pady=5)

    ctk.CTkLabel(app, text="Generate New Bill", font=ctk.CTkFont(size=16)).pack(pady=10)

    patient_entry = ctk.CTkEntry(app, placeholder_text="Patient Name")
    patient_entry.pack(pady=5)

    room_charges_entry = ctk.CTkEntry(app, placeholder_text="Room Charges")
    room_charges_entry.pack(pady=5)

    doctor_fee_entry = ctk.CTkEntry(app, placeholder_text="Doctor Fee")
    doctor_fee_entry.pack(pady=5)

    other_charges_entry = ctk.CTkEntry(app, placeholder_text="Other Charges")
    other_charges_entry.pack(pady=5)

    item1_entry = ctk.CTkEntry(app, placeholder_text="Item 1 Description")
    item1_entry.pack(pady=5)

    item1_amount_entry = ctk.CTkEntry(app, placeholder_text="Item 1 Amount")
    item1_amount_entry.pack(pady=5)

    item2_entry = ctk.CTkEntry(app, placeholder_text="Item 2 Description")
    item2_entry.pack(pady=5)

    item2_amount_entry = ctk.CTkEntry(app, placeholder_text="Item 2 Amount")
    item2_amount_entry.pack(pady=5)

    def submit_bill():
        try:
            patient_name = patient_entry.get().strip()
            room_charges = float(room_charges_entry.get() or 0)
            doctor_fee = float(doctor_fee_entry.get() or 0)
            other_charges = float(other_charges_entry.get() or 0)

            item1 = item1_entry.get().strip()
            item1_amt = float(item1_amount_entry.get() or 0)
            item2 = item2_entry.get().strip()
            item2_amt = float(item2_amount_entry.get() or 0)

            items = []
            if item1:
                items.append({"item": item1, "amount": item1_amt})
            if item2:
                items.append({"item": item2, "amount": item2_amt})

            if not patient_name:
                raise ValueError("Patient name is required")

            billing.generate_bill(patient_name, items, room_charges, doctor_fee, other_charges)
            messagebox.showinfo("Success", "Bill generated.")
            app.destroy()
            open_billing_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ctk.CTkButton(app, text="Generate Bill", command=submit_bill).pack(pady=10)

    # Divider
    ctk.CTkLabel(app, text="All Bills", font=ctk.CTkFont(size=14)).pack(pady=10)

    bill_box = ctk.CTkTextbox(app, width=500, height=200)
    bill_box.pack()

    all_bills = billing.get_all_bills()
    if all_bills:
        for b in all_bills:
            line = f"🧾 {b['patient_name']} | ₹{b['total']} | {b['status']} | {b['generated_on']}\n"
            bill_box.insert("end", line)
    else:
        bill_box.insert("end", "No bills found.\n")

    # Mark bill paid
    ctk.CTkLabel(app, text="Mark Bill as Paid").pack(pady=5)
    paid_name_entry = ctk.CTkEntry(app, placeholder_text="Enter Patient Name")
    paid_name_entry.pack(pady=5)

    def mark_paid():
        name = paid_name_entry.get().strip()
        if name:
            result = billing.mark_bill_paid(name)
            if result.modified_count:
                messagebox.showinfo("Done", f"{name}'s bill marked as paid.")
                app.destroy()
                open_billing_form()
            else:
                messagebox.showwarning("Not Found", f"No unpaid bill for '{name}'.")
        else:
            messagebox.showerror("Error", "Patient name required.")

    ctk.CTkButton(app, text="Mark as Paid", command=mark_paid).pack(pady=10)

    app.mainloop()
