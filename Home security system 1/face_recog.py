from deepface import DeepFace

# verifyign a face:
face_res = DeepFace.verify('image1.jpg', 'image2.jpg')
print(face_res)

