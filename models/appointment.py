from db import db
from datetime import datetime

def book_appointment(patient_name, doctor_name, date, time, reason):
    appointment = {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "date": date,
        "time": time,
        "reason": reason,
        "status": "Scheduled",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    return db['appointments'].insert_one(appointment)

def update_appointment_status(patient_name, new_status):
    return db['appointments'].update_one(
        {"patient_name": patient_name, "status": "Scheduled"},
        {"$set": {"status": new_status, "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")}}
    )

def get_all_appointments():
    return list(db['appointments'].find({}, {"_id": 0}))

def get_appointments_by_doctor(doctor_name):
    return list(db['appointments'].find({"doctor_name": doctor_name}, {"_id": 0}))

def cancel_appointment(patient_name):
    return db['appointments'].delete_one({"patient_name": patient_name, "status": "Scheduled"})
