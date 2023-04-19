import os
import random
import shutil

# Change directory
os.chdir(r'/Users/kyochul_jang/Desktop/bk21/datasets/Target-B/val/total-images') 

# Set path
original = os.getcwd()
target = r'/Users/kyochul_jang/Desktop/bk21/datasets/Target-B/val/images'

# Set the number of images you want to copy
image_num = 290

images_list = random.sample(os.listdir(os.getcwd()), image_num)
for i in images_list:
    org_img_path = os.path.join(original, i)
    targ_img_path = os.path.join(target, i)
    shutil.copyfile(org_img_path, targ_img_path)

