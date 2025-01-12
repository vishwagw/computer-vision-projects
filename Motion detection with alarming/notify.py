# for send notification to a authorised e mail address:
# import libs:
import smtplib
import numpy as np
import cv2
import imutils
# emailing:
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#details about email receiver:
sender_email = 'sender/your email'
sender_password = 'your email password'
recipient_email = 'recipient email address'
subject = 'URGENT ACTIONS REQUIRED!' 
body = 'A Motion activity has been detected in your place/home/shop..!'

#function for sending emails:
def send_notify(frame1, frame2, frame3, frame4, frame5):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    frames = [frame1, frame2, frame3, frame4, frame5]
    for i, frame in enumerate(frames):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        _, frame_jpeg = cv2.imencode('.jpg', frame_rgb)
        image = MIMEImage(frame_jpeg.tobytes())
        image.add_header('Content-Disposition', 'attachment', filename=f'frame{i+1}.jpg')
        msg.attach(image)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
    print('Email sent successfully.')

