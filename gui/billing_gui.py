import customtkinter as ctk
from tkinter import messagebox
from models import billing
from gui.home import open_home_screen, _current_role

def open_billing_form():
    app = ctk.CTk()
    app.geometry("600x600")
    app.title("Billing Management")

    ctk.CTkButton(app, text="← Back", command=lambda: [app.destroy(), open_home_screen(_current_role)]).pack(pady=5)
    ctk.CTkLabel(app, text="Generate New Bill", font=ctk.CTkFont(size=16)).pack(pady=10)

    entries = {}
    for ph in ["Patient Name", "Room Charges", "Doctor Fee", "Other Charges", "Item 1 Description", "Item 1 Amount", "Item 2 Description", "Item 2 Amount"]:
        entries[ph] = ctk.CTkEntry(app, placeholder_text=ph)
        entries[ph].pack(pady=5)

    def submit_bill():
        try:
            vals = {k: entries[k].get().strip() for k in entries}
            patient = vals["Patient Name"]
            if not patient:
                raise ValueError("Patient name required.")
            room = float(vals["Room Charges"] or 0)
            doc_fee = float(vals["Doctor Fee"] or 0)
            other = float(vals["Other Charges"] or 0)
            items = []
            if vals["Item 1 Description"]:
                items.append({"item": vals["Item 1 Description"], "amount": float(vals["Item 1 Amount"] or 0)})
            if vals["Item 2 Description"]:
                items.append({"item": vals["Item 2 Description"], "amount": float(vals["Item 2 Amount"] or 0)})

            billing.generate_bill(patient, items, room, doc_fee, other)
            messagebox.showinfo("Success", "Bill generated.")
            app.destroy()
            open_home_screen(_current_role)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ctk.CTkButton(app, text="Generate Bill", command=submit_bill).pack(pady=10)
    ctk.CTkLabel(app, text="All Bills", font=ctk.CTkFont(size=14)).pack(pady=10)
    tb = ctk.CTkTextbox(app, width=500, height=200)
    tb.pack()
    for b in billing.get_all_bills():
        tb.insert("end", f"{b['patient_name']} | ₹{b['total']} | {b['status']} | {b['generated_on']}\n")

    paid_entry = ctk.CTkEntry(app, placeholder_text="Patient Name to Mark Paid")
    paid_entry.pack(pady=5)

    def mark_paid():
        name = paid_entry.get().strip()
        if name:
            result = billing.mark_bill_paid(name)
            if result.modified_count:
                messagebox.showinfo("Done", f"'{name}' paid.")
                app.destroy()
                open_home_screen(_current_role)
            else:
                messagebox.showwarning("Not Found", f"No unpaid bill for '{name}'.")
        else:
            messagebox.showerror("Missing", "Name required.")

    ctk.CTkButton(app, text="Mark as Paid", command=mark_paid).pack(pady=10)
    app.mainloop()
