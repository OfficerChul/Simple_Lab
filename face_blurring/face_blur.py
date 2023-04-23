import os.path

from skimage import data, io, filters
from retinaface import RetinaFace
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

import cv2
import time

tic = time.time()

example_folder_path = os.path.join(os.getcwd(), 'example_vid')

# for vid in os.listdir(ex_folder_path):
#     cap = cv2.VideoCapture(os.path.join(ex_folder_path, vid))


video_name = '20200901_120617.MOV'
video_path = os.path.join(example_folder_path, video_name)
print(video_path)
cap = cv2.VideoCapture(video_path)
# fourcc = cv2.VideoWriter_fourcc(*'h264')
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
cap.open(video_path)
print(cap.isOpened())
print(fps, fourcc)
new_vid_name = video_name + '2'
out = cv2.VideoWriter(new_vid_name, int(fourcc), fps, (1920, 1080))

orig_vid_size = os.stat(video_path).st_size
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'total frame: {total}')


count = 0
while True:
    tic2 = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    # print(f'count: {count}/{total}')
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = RetinaFace.detect_faces(frame)
    for face in faces.keys():
        face = faces[face]
        facial_area = face['facial_area']
        x = facial_area[0]
        y = facial_area[1]
        w = facial_area[2] - facial_area[0]
        h = facial_area[3] - facial_area[1]
        # cv2.rectangle(frame, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (255, 255, 255), 10)
        roi = frame[y:y + h, x:x + w]

        # apply gaussian blur to face rectangle
        roi = cv2.GaussianBlur(roi, (17, 17), 30)

        # add blurred face on original image to get final image
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

