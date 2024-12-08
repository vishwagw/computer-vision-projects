# libs :
import numpy as np
import cv2
import tensorflow as tf
from keras.models import load_model


# loading the pre-trained model:
model = load_model('./pre_trained_model/model/facenet_keras.h5')
print("Model Loaded Successfully")

# pre-process the image before use
def preprocess(image_path):
    image_path = './test_image/pexels-alipazani-2613260.jpg'
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to RGB (FaceNet expects RGB images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize the image to 160x160 pixels
    img = cv2.resize(img, (160, 160))

    # Normalize the pixel values
    img = img.astype('float32') / 255.0

    # Expand dimensions to match the input shape of FaceNet (1, 160, 160, 3)
    img = np.expand_dims(img, axis=0)

    return img

# embedding:
def get_face_embedding(model, image_path):
     # Preprocess the image
    img = preprocess(image_path)

    # Generate the embedding
    embedding = model.predict(img)

    return embedding


# compating th faces by using embeddings:
from numpy import linalg as LA
def compare_faces(embedding1, embedding2, threshold=0.5):
    # Compute the Euclidean distance between the embeddings
    distance = LA.norm(embedding1 - embedding2)

    # Compare the distance to the threshold
    if distance < threshold:
        print("Face Matched.")
    else:
        print("Faces are different.")

    return distance

# test system:
# Load the FaceNet model
model = load_model('facenet_keras.h5')

# Get embeddings for two images
embedding1 = get_face_embedding(model, 'face1.jpg')
embedding2 = get_face_embedding(model, 'face2.jpg')

# Compare the two faces
distance = compare_faces(embedding1, embedding2)

print(f"Euclidean Distance: {distance}")



