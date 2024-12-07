import cv2

# reading the image :
input_img = cv2.imread('./input1.png')

# extract the height and width
h, w = input_img.shape[:2]

# display output:
print("Height = {}, Width = {}".format(h,w))

output = input_img.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900),(600,400), (255, 0, 0), 2)
