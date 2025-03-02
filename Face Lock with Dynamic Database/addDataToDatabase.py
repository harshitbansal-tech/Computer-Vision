import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("doctorfacerecognition-firebase-adminsdk-afnvm-58ce74cfdf.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://doctorfacerecognition-default-rtdb.firebaseio.com/"
})

ref = db.reference('Doctors')

data = {
    '101': {
        "name": "Doctor1",
        "specialization": "A",
        "location": "H",
        "sub-location": "K-3"
    },
    '102': {
        "name": "Doctor2",
        "specialization": "Q",
        "location": "C",
        "sub-location": "A-1"
    },
    '103': {
        "name": "Doctor3",
        "specialization": "B",
        "location": "E",
        "sub-location": "B-4"
    }

}

for key,value in data.items():
    ref.child(key).set(value)