from mtcnn import MTCNN
import cv2

detector = MTCNN(batch_size=16)

img = cv2.imread('./img.jpg')
detections = detector.detect_faces(img)

for detection in detections:
    score = detection["confidence"]
    if score > 0.90:
        x, y, w, h = detection["box"]
        detected_face = img[int(y):int(y + h), int(x):int(x + w)]
        roi = img[y:y + h, x:x + w]

        # apply gaussian blur to face rectangle
        roi = cv2.GaussianBlur(roi, (17, 17), 30)
