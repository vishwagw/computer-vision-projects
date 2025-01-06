# libs 
import numpy as np
import cv2
import imutils
import datetime
from matplotlib import pyplot as plt

# download the data set
# import it - dataset.xml file
# data set is a cascade file

weapon_detect = cv2.CascadeClassifier('./')
cam1 = cv2.VideoCapture(0)
#first frame:
first_frame = None
weapin_exist = False

# main loop function:
while True:
    ret, frame = cam1.read()
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = weapon_detect.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)
    
    if gun_exist:
        print("Guns detected")
        plt.imshow(frame)
        break
    else:
        cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()


