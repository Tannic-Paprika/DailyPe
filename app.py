import firebase_admin
from firebase_admin import credentials,firestore
from google.cloud.firestore_v1 import SERVER_TIMESTAMP
from flask import Flask, request, jsonify, render_template
import uuid

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("dailype-task-firebase-adminsdk-8swwe-47cd916753.json")
firebase_admin.initialize_app(cred)
db= firestore.client()

@app.route('/')
def index():
    return render_template('create_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    full_name = request.form.get('full_name')
    mob_num = request.form.get('mob_num')
    pan_num = request.form.get('pan_num')
    manager_id = request.form.get('manager_id')

    if not all([full_name, mob_num, pan_num]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    user_id= str(uuid.uuid4())
    mob_num= mob_num[-10:]
    pan_num= pan_num.upper()
    
    user_data = {
        'full_name': full_name,
        'mob_num': mob_num,
        'pan_num': pan_num,
        'manager_id': manager_id,
        'Created_at': SERVER_TIMESTAMP
    }
    
    db.collection('user_credentials').document(user_id).set(user_data)
    return jsonify({'message': 'User created successfully','user_id':user_id}), 201



if __name__ == '__main__':
    app.run(debug=True)