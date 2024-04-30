import uuid 
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("dailype-task-firebase-adminsdk-8swwe-47cd916753.json")
firebase_admin.initialize_app(cred)
db= firestore.client()

managers = ['Ravi','Akash','Saket','Divya','Ramit']

for manager in managers:
    manager_id= str(uuid.uuid4())
    user_data={
        'manager name': manager,
        'manager_id': manager_id
    }
    db.collection('manager_credentials').document(manager_id).set(user_data)
    
