import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("./input1.png")

h, w = image.shape[:2]
rotation_matrix = cv.getRotationMatrix2D((w/2,h/2), -180, 0.5)

rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))

plt.imshow(cv.cvtColor(rotated_image, cv.COLOR_BGR2RGB))
plt.title("Rotation")
plt.show()