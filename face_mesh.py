import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
ptime = 0

mpDraw = mp.solutions.drawing_utils
mpFMesh = mp.solutions.face_mesh
faceMesh = mpFMesh.FaceMesh()
draw = mpDraw.DrawingSpec(thickness= 1, circle_radius=2)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFMesh.FACE_CONNECTIONS,
                                  draw, draw)
            for lm in enumerate(faceLms.landmark):
                ih,iw,ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print (id, x,y)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,
                3, (0,255,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)