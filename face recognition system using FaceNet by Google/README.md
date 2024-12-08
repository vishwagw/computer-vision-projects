# automated attendance and welcome system for events

1. the system use computer vision for facial recognition
2. machine learning for attendance management
3. data base for guest details

# the python libraries for facial recognition:
1. face_recognition - pip install face_recognition (require dlib to be intalled in the computer.)
2. facenet - pip install facenet - (advanced suite)
3. openface - pip install openface

# Encoding : 
the process of using a neural network to produce a set of numbers that represent a face. the numbers are called face encodings.The neural network is trained to automatically identify faces and compute numbers based on the differences and similarities between them

There are two types of face recognition models
1. face verification: recognizin a given face by mapping it one=to-one against a known identitiy. 
2. Face identification: A one-to-many mapping for a given face against a database of known faces.

# face net:
face net is introduced by a team of google engineers in 2015. it is a deep learning model developed by Google that maps faces into a 128-dimensional Euclidean space. These embeddings represent the essential features of a face, making it easy to compare and recognize faces with high accuracy. Unlike traditional face recognition methods, FaceNet focuses on embedding learning, which makes it highly effective and scalable. 

to download the pre-trained facenet model use following link:
https://drive.google.com/open?id=1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn

then place it inside the pre_trained_model folder.

requirements:
- python 3
- tensorflow 
- keras
- numpy
- opencv
- scikit-learn



