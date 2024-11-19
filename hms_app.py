from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


app = Flask(__name__)

patients_data = []
doctors_data = []
caregivers_data = []
staff_data = []
pharmacists_data = []

def find_patient_by_id(patient_id):
    for patient in patients_data:
        if patient['id'] == patient_id:
            return patient
    return None

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/register_patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    patient_id = len(patients_data) + 1  
    patient = {
        'id': patient_id,
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'address': data['address'],
        'contact_number': data['contact_number'],
        'admission_status': False  
    }
    patients_data.append(patient)
    return jsonify({"message": "Patient registered successfully", "patient_id": patient_id}), 201

@app.route('/admit_patient/<int:patient_id>', methods=['PUT'])
def admit_patient(patient_id):
    patient = find_patient_by_id(patient_id)
    if patient:
        patient['admission_status'] = True
        return jsonify({"message": f"Patient {patient['name']} admitted successfully"}), 200
    return jsonify({"message": "Patient not found"}), 404

@app.route('/discharge_patient/<int:patient_id>', methods=['PUT'])
def discharge_patient(patient_id):
    patient = find_patient_by_id(patient_id)
    if patient:
        patient['admission_status'] = False
        return jsonify({"message": f"Patient {patient['name']} discharged successfully"}), 200
    return jsonify({"message": "Patient not found"}), 404

@app.route('/get_patients', methods=['GET'])
def get_patients():
    # Return the list of all registered patients
    return jsonify(patients_data), 200

@app.route('/register_doctor', methods=['POST'])
def register_doctor():
    data = request.get_json()
    doctor_id = len(doctors_data) + 1 
    doctor = {
        'id': doctor_id,
        'name': data['name'],
        'specialization': data['specialization'],
        'contact_number': data['contact_number'],
        'is_admin': data.get('is_admin', False)
    }
    if doctor['is_admin']:
        return jsonify({"message": "Only admin can register doctors."}), 403
    doctors_data.append(doctor)
    return jsonify({"message": "Doctor registered successfully", "doctor_id": doctor_id}), 201

@app.route('/add_caregiver', methods=['POST'])
def add_caregiver():
    data = request.get_json()
    caregiver_id = len(caregivers_data) + 1  
    caregiver = {
        'id': caregiver_id,
        'name': data['name'],
        'role': data['role'],
        'contact_number': data['contact_number']
    }
    caregivers_data.append(caregiver)
    return jsonify({"message": "Caregiver added successfully", "caregiver_id": caregiver_id}), 201

@app.route('/add_staff', methods=['POST'])
def add_staff():
    data = request.get_json()
    staff_id = len(staff_data) + 1  
    staff_member = {
        'id': staff_id,
        'name': data['name'],
        'role': data['role'],
        'contact_number': data['contact_number']
    }
    staff_data.append(staff_member)
    return jsonify({"message": "Staff added successfully", "staff_id": staff_id}), 201

@app.route('/add_pharmacist', methods=['POST'])
def add_pharmacist():
    data = request.get_json()
    pharmacist_id = len(pharmacists_data) + 1  
    pharmacist = {
        'id': pharmacist_id,
        'name': data['name'],
        'license_number': data['license_number'],
        'contact_number': data['contact_number']
    }
    pharmacists_data.append(pharmacist)
    return jsonify({"message": "Pharmacist added successfully", "pharmacist_id": pharmacist_id}), 201

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




# Data storage (as before)


# Define your routes here as before...



