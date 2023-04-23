import cv2
import os
import subprocess
import time
from datetime import timedelta
import torch

tic = time.time()
in_dir_path = os.path.join(os.getcwd(), "../../../Project/YoloV5/action_image")
out_dir_path = os.path.join(os.getcwd(), '../../../Project/YoloV5/action_image_out')
crf = 30

count = 0
file_size = 0
root = r'L:\099-rawdata-RESTRICTED\22-07_AKASO_KSS_FWL_action'
out_root = r'C:\Users\simplelab-kyochul\Documents\FHD_FWL'
for FWL_action_camera_dir in os.listdir(root):

    if not FWL_action_camera_dir.startswith('.'):
        FWL_action_camera_path = os.path.join(root, FWL_action_camera_dir)

        out_FAC_path = os.path.join(out_root, FWL_action_camera_dir)
        os.mkdir(out_FAC_path)

        for actions_dir in os.listdir(FWL_action_camera_path):  # 01_Stamping
            actions = os.path.join(FWL_action_camera_path, actions_dir)
            if not actions_dir.startswith('.'):
                out_A_path = os.path.join(out_FAC_path, actions_dir)
                os.mkdir(out_A_path)

                for video in os.listdir(actions):
                    in_video_path = os.path.join(actions, video)

                    out_video_path = os.path.join(out_A_path, video)

                    file_size += os.stat(in_video_path).st_size

                    command = f'ffmpeg -i {in_video_path} -c:v h264_nvenc -crf {crf} -vf scale=1920x1080 -an {out_video_path}'
                    result = subprocess.run(command, shell=True)
                    count += 1

if torch.cuda.is_available():
    print("Cuda is available")

elapsed = time.time() - tic
formatted_elapsed = str(timedelta(seconds=elapsed))
print(f'Video_num: {count}')
print(f'in_video file_size in GigaByte: {file_size / 1024 ** 3}')
print(f'Elapsed Time(%hh:%mm:%ss.xxx): {formatted_elapsed}')

"""
for video_name in os.listdir(in_dir_path):
    count += 1
    in_video_path = os.path.join(in_dir_path, video_name)
    out_video_name = f'FHD_{video_name}'
    out_video_path = os.path.join(out_dir_path, out_video_name)

    file_size += os.stat(in_video_path).st_size

    command = f'ffmpeg -i {in_video_path} -c:v libx264 -crf {crf} -vf scale=1920x1080 -an {out_video_path}'
    result = subprocess.run(command, shell=True)

    # print(result)

if torch.cuda.is_available():
    print("Cuda is currently using")

elapsed = time.time() - tic
formatted_elapsed = str(timedelta(seconds=elapsed))
print(f'Video_num: {count}')
print(f'in_video file_size in GigaByte: {file_size / 1024 ** 3}')
print(f'Elapsed Time(%hh:%mm:%ss.xxx): {formatted_elapsed}')
"""