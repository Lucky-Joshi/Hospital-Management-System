from db import db

def add_doctor(name, specialty, phone, department):
    doctor = {
        "name": name,
        "specialty": specialty,
        "phone": phone,
        "department": department
    }
    return db['doctors'].insert_one(doctor)

def get_all_doctors():
    return list(db['doctors'].find({}, {"_id": 0}))

def get_doctor_by_name(name):
    return db['doctors'].find_one({"name": name}, {"_id": 0})

def update_doctor(name, updates: dict):
    return db['doctors'].update_one({"name": name}, {"$set": updates})

def delete_doctor(name):
    return db['doctors'].delete_one({"name": name})
