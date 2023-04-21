from skimage import data, io, filters
from retinaface import RetinaFace
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

import cv2
import time

tic = time.time()

cap = cv2.VideoCapture('./example_vid/20200901_120617.MOV')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('output_video.avi', fourcc, 30, (1920, 1080))

total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'total frame: {total}')


count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    print(f'count: {count}/{total}')
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = RetinaFace.detect_faces(frame)
    for face in faces.keys():
        face = faces[face]
        facial_area = face['facial_area']

        cv2.rectangle(frame, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (255, 255, 255), 10)

    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

elapsed = time.time() - tic
formatted_elapsed = str(timedelta(seconds=elapsed))
print(f'Elapsed Time(%hh:%mm:%ss.xxx): {formatted_elapsed}')

