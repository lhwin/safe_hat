import os
current_path = os.path.dirname(os.path.abspath(__file__))
path_suffix = 'apps'
if current_path.endswith(path_suffix):
    parent_path = current_path.rsplit(path_suffix, 1)[0]
    os.chdir(parent_path)

from yolov3 import YOLO
from detect_video import detect_video

if __name__ == '__main__':
    video_file_name = '11'
    video_path = 'F:\\vid\\input\\' + '%s.mp4' % video_file_name
    out_path = 'F:\\vid\\output\\'
    detect_video(YOLO(), video_path, out_path)
    