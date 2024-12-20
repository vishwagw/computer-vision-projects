# libs :
import numpy as np
import cv2
from retinaface import RetinaFace

# building the function for prcessing faces for detection:
def face_processing(frame):
    faces = RetinaFace.detect_faces(frame)
    if faces:
        for key, face in faces.items():
            facial_area = face['facial_area']
            x1, y1, x2, y2 = facial_area
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Annotate with confidence score
            confidence = face.get('score', 0)
            cv2.putText(
                frame,
                f"Conf: {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )
    return faces

# building the main function:
# Captures video from a webcam, detects faces in real-time, and displays the output.
def detect_main():

    v_cap = cv2.VideoCapture(0) # 0 - default video config.
    if not v_cap.isOpened():
        print("Error: Could not open video capture device.")
        return
    
    while True:
        ret, frame = v_cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

    # Convert BGR to RGB for RetinaFace processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        annotated_frame = face_processing(rgb_frame)

    # Convert RGB back to BGR for OpenCV display
        bgr_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
        
        cv2.imshow("Face Detection (Press 'q' to quit)", bgr_frame)
        
        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    v_cap.release()
    cv2.destroyAllWindows()

# intitialize the function:
if __name__ == "__main__":
    detect_main()


    
    

    