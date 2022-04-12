# 1.Detecting a face
# 2. Saving it (Numpy array)
# 3. Recognizing it the next time

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
face_data = []
datasetPath = "./data/"

fileName = input("Enter name of user: ")

skip = 0
face_section = []

# Capturing the video from primary camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        continue

    # Getting the faces
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    # Finding the largest face to save it
    faces = sorted(faces, key=lambda f: f[2] * f[3])

    for face in faces[-1:]:  # w-> Width, h->height
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the face
        offset = 10
        face_section = frame[max(0, y - offset): min(len(frame), y + h + offset),
                             max(0, x - offset): min(len(frame[0]), x + w + offset)]

        face_section = cv2.resize(face_section, (100, 100))

        skip += 1
        if skip % 10 == 0:
            # Every 10 frames
            face_data.append(face_section)
            cv2.imshow("Face Section", face_section)
            print(len(face_data))

    cv2.imshow("Video", frame)

    # Wait for user input
    keyPressed = cv2.waitKey(1) & 0xFF
    if keyPressed == ord('q'):
        break   # Break on pressing q

# flatten
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))

# Save locally
np.save(datasetPath + fileName + ".npy", face_data)

# Cleanup

cap.release()
cv2.destroyAllWindows()
