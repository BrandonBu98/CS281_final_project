# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import glob
import re
import os

def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]

def transform_video_to_image(video_file_path, img_path):
    video_capture = cv2.VideoCapture(video_file_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    count = 0
    while (True):
        ret, frame = video_capture.read()

        if ret:
            cv2.imwrite(img_path + '%d.png' % count, frame)
            count += 1
        else:
            break
    video_capture.release()
    print('save image succees, total of %d' % count)
    return fps


image_folder = './eeaaolol_output'
img_array = []
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
sorted_images = sorted(images, key=natural_sort_key)

for filename in sorted_images:
    img = cv2.imread(os.path.join(image_folder, filename))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
