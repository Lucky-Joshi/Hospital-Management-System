from db import db
from datetime import datetime

def admit_patient(patient_name, room_number, room_type, reason):
    admission = {
        "patient_name": patient_name,
        "room_number": room_number,
        "room_type": room_type,
        "admission_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "reason": reason,
        "status": "Admitted"
    }
    return db['admissions'].insert_one(admission)

def discharge_patient(patient_name):
    return db['admissions'].update_one(
        {"patient_name": patient_name, "status": "Admitted"},
        {"$set": {"status": "Discharged", "discharge_date": datetime.now().strftime("%Y-%m-%d %H:%M")}}
    )

def get_active_admissions():
    return list(db['admissions'].find({"status": "Admitted"}, {"_id": 0}))

def get_all_admissions():
    return list(db['admissions'].find({}, {"_id": 0}))
