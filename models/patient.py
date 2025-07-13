from db import db

def add_patient(name, gender, phone, address):
    patient = {
        "name": name,
        "gender": gender,
        "phone": phone,
        "address": address
    }
    return db['patients'].insert_one(patient)

def get_all_patients():
    return list(db['patients'].find({}, {"_id": 0}))
