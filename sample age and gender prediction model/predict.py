# importing libraries
import cv2
import numpy as np

# loading pre-trained model
age_model = './models/age_net.caffemodel'
age_proto = './models/deploy_age.prototxt'
gender_model = './models/gender_net.caffemodel'
gender_proto = './models/deploy_gender.prototxt'

#mean values:
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# age and gender category classification:
age_categories = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
gender_categories = ['Male', 'Female']

# networks:
age_net = cv2.dnn.readNet(age_model, age_proto)
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

# detecting the faces:
# fo this we use Haar Cascades:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# now the model for prediction:
# input data can be used : real-time(webcame) or image file(saved)

# 1. for webcam
#cap = cv2.VideoCapture(0)
# 2. input from a video file
cap = cv2.VideoCapture('./input/video/855564-hd_1920_1080_24fps.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        # let's predict gender:
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        gender = gender_categories[gender_preds[0].argmax()]

        # let's predict age:
        age_net.setInput(blob)
        age_preds = age_net.forward()
        age = age_categories[age_preds[0].argmax()]

        # draw from the frame
        label = f"{gender}, {age}"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 250, 0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (250, 250, 250), 2)

    # Display the video frame:
    cv2.imshow('Age and Gender Recognition', frame)
    
    # break with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
