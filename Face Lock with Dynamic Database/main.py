import pickle
import numpy as np
import cv2
import os

import face_recognition

capture_camera = cv2.VideoCapture(0)
capture_camera.set(3, 1280)
capture_camera.set(4, 720)

folder = 'resources'
modePath = os.listdir(folder)
imageMode = []
for path in modePath:
    imageMode.append(cv2.imread(os.path.join(folder,path)))

file = open('DocImageData.p', 'rb')
encode_id = pickle.load(file)
file.close()
encode_list, doc_id = encode_id

while True:
    success, img = capture_camera.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    face_cam = face_recognition.face_locations(imgS)
    encode_face = face_recognition.face_encodings(imgS, face_cam)

    for encode_face_data, face_loc in zip(encode_face, face_cam):
        matches = face_recognition.compare_faces(encode_list, encode_face_data)
        face_distance = face_recognition.face_distance(encode_list, encode_face_data)
        print(matches, "matches")
        print(face_distance, "face_distance")
        matchIndex = np.argmin(face_distance)
        print(matchIndex)
        if matches[matchIndex]:
            print('Known Face Detected')
            #print(doc_id[matchIndex])

    cv2.imshow("Doctor Recognition", img)
    cv2.waitKey(0)
