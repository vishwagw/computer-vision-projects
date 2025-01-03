# import libs:
# main program :
import numpy as np
import threading
import cv2
import imutils
import mail
import winsound

# video input:
v_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#v_cap = cv2.VideoCapture(0)

v_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
v_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = v_cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

# alarm at start:
alarm = False
alarm_mode = False
alarm_counter = 0

# function for alarm:
def alarm_activate():
    global alarm
    while alarm_mode:
        print("ALARM")
        winsound.Beep(2500, 1000)

# loop function for detecting:
while True:
    _, frame = v_cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(start_frame, frame_bw)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 10000: # This is the sensitivity of the motion detection, you can change this value
            alarm_counter += 1
            if alarm_counter > 20:
                if not alarm:
                    alarm = True
                    threading.Thread(target=alarm_activate).start()
                    threading.Thread(target=mail.send_email, args=(frame, frame, frame, frame, frame)).start()
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)

    elif not alarm_mode and alarm:
        black_frame = np.zeros_like(frame)
        cv2.imshow("Cam", black_frame)
    else:
        cv2.imshow("Cam", frame)

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('t'):
        print("You have activated/deactivated the alarm!")
        alarm_mode = not alarm_mode
        alarm_counter = 0
    elif key_pressed == ord('q'):
        print("Quitting the program!")
        alarm_mode = False
        break

v_cap.release()
cv2.destroyAllWindows()



