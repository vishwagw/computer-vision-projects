from deepface import DeepFace
import cv2

verification = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
