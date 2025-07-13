from db import db
from datetime import datetime

def generate_bill(patient_name, items, room_charges=0, doctor_fee=0, other_charges=0):
    total_amount = sum(item['amount'] for item in items) + room_charges + doctor_fee + other_charges

    bill = {
        "patient_name": patient_name,
        "items": items,  # Example: [{'item': 'X-Ray', 'amount': 500}]
        "room_charges": room_charges,
        "doctor_fee": doctor_fee,
        "other_charges": other_charges,
        "total": total_amount,
        "status": "Unpaid",
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    return db['bills'].insert_one(bill)

def mark_bill_paid(patient_name):
    return db['bills'].update_one(
        {"patient_name": patient_name, "status": "Unpaid"},
        {"$set": {"status": "Paid", "paid_on": datetime.now().strftime("%Y-%m-%d %H:%M")}}
    )

def get_patient_bills(patient_name):
    return list(db['bills'].find({"patient_name": patient_name}, {"_id": 0}))

def get_all_bills():
    return list(db['bills'].find({}, {"_id": 0}))
