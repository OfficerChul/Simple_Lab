from mtcnn import MTCNN
import cv2
import time
import os
from datetime import timedelta

tic = time.time()

example_folder_path = os.path.join(os.getcwd(), 'example_vid')

video_name = '20200901_120617.MOV'
video_path = os.path.join(example_folder_path, video_name)
print(video_path)
cap = cv2.VideoCapture(video_path)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

fps = cap.get(cv2.CAP_PROP_FPS)
new_vid_name = 'MC20200901_120617.MOV'
out = cv2.VideoWriter(new_vid_name, fourcc, 30, (1920, 1080))

orig_vid_size = os.stat(video_path).st_size
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'total frame: {total}')

detector = MTCNN()

count = 0
while True:
    tic2 = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    print(f'count: {count}/{total}')
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = MTCNN().detect_faces(frame)
    for face in faces:
        score = face['confidence']
        if score > 0.9:
            x, y, w, h = face['box']
            roi = frame[y:y+h, x:x+w]
            roi = cv2.GaussianBlur(roi, (17, 17), 100)
            # cv2.rectangle(frame, (x, w), (y, h), (255, 255, 255), 10)
            frame[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

            out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elapsed2 = time.time() - tic2
    formatted_elapsed2 = str(timedelta(seconds=elapsed2))
    print(f'count: {count}/{total}, elapsed time(%hh:%mm:%ss.xxx): {formatted_elapsed2}')

elapsed = time.time() - tic
formatted_elapsed = str(timedelta(seconds=elapsed))
print(f'Total Elapsed Time(%hh:%mm:%ss.xxx): {formatted_elapsed}')
print(f'The video size decreased from {orig_vid_size} to {os.stat(new_vid_name).st_size}')