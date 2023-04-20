try:
    import cv2
except ImportError:
    print('opencv is not imported.')
import numpy as np
import os
import matplotlib.pyplot as plt

print(os.getcwd())
xml = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + xml)

for idx, vid in enumerate(os.listdir('./example_vids')):
    print(f'{idx} vid: {vid}')
    vid_path = os.path.join('example_vids', vid)
    cap = cv2.VideoCapture(os.path.join(os.getcwd(), vid_path))

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)

        print(f'number of face detected: {len(faces)}')

        if len(faces):
            for (x, y, w, h) in faces:
                # face_img = frame[y:y+h, x:x+w]
                #
                # face_img = cv2.resize(face_img, dsize=(0,0), fx=0.04, fy=0.04)
                # face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
                # frame[y:y+h, x:x+w] = face_img

                cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi = gray[y:y + h, x:x + w]
                # applying a gaussian blur over this new rectangle area
                roi = cv2.GaussianBlur(roi, (23, 23), 30)
                # impose this blurred image on original image to get final image
                gray[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

        plt.imshow(gray, cmap="gray")
        plt.axis('off')
        plt.style.use('seaborn')
        plt.show()
