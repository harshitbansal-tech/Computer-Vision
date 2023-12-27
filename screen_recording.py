import cv2
import numpy as np
import pyautogui as py

resolution = py.size()

file_store = input("Enter the File Name and Path : ")

fps = 60.0
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(file_store, fourcc, fps, resolution)

cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording", (600, 400))

while True :
    img = py.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording", f)
    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()