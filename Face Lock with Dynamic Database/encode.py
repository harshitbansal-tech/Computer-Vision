import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("doctorfacerecognition-firebase-adminsdk-afnvm-58ce74cfdf.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://doctorfacerecognition-default-rtdb.firebaseio.com/",
    'storageBucket': "doctorfacerecognition.appspot.com"
})

folder = 'images'
pathList = os.listdir(folder)
imageList = []
doc_id = []
for path in pathList:
    imageList.append(cv2.imread(os.path.join(folder,path)))
    doc_id.append(os.path.splitext(path)[0])

    fileName = f'{pathList}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(os.path.join(folder, path))
def encoding(imageList):
    list_doc_encode = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        list_doc_encode.append(encode)
    return list_doc_encode

encode_list = encoding(imageList)
id_encode = [encode_list, doc_id]

file = open("DocImageData.p", 'wb')
pickle.dump(id_encode, file)
file.close()