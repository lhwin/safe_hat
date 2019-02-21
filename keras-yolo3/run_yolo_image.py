import os
from yolo_detect.detect_image import detect_image
from yolo_detect.yolo import YOLO

current_path = os.path.dirname(os.path.abspath(__file__))
path_suffix = '/apps'
if current_path.endswith(path_suffix):
    parent_path = current_path.rsplit(path_suffix, 1)[0]
    os.chdir(parent_path)


if __name__ == '__main__':

    """
    Image detection mode, disregard any remaining command line arguments
    """
    print("Image detection mode")
    # input_img_path = input('Input image filename:')
    # output_img_path = input('Output image filename:')
    input_img_path = 'F:\\pic\\motor\\page1_2.jpg'
    output_img_path = 'F:\\pic\\fc1af672ab.jpg'

    detect_image(YOLO(), input_img_path, output_img_path)
