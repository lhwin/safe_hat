#author = "Lee Hir"
import os
import cv2
# from Tools import crop_image
import random
from PIL import Image
import numpy as np
import time
def listdir(path):
    list = os.listdir(path)
    return list
def rotate(read_path,save_path):
    im = Image.open(read_path)
    im_rot = im.rotate(270)
    im_rot.save(save_path,'jpeg')
def vid_to_pic(save_path,video_path):
    vc = cv2.VideoCapture(video_path)
    s = video_path.split('\\')[-1]
    c = 1
    # set interval
    t = 3
    rval = vc.isOpened()
    while rval:
        rval, frame = vc.read()
        if(c%t == 0):
            cv2.imwrite(save_path + s +str(c/t) + '.jpg',frame)
        c = c + 1
    vc.release()
def crop_image(image,box):
    src = image[int(box[0]):int(box[2]),int(box[1]):int(box[3])]
    return src
save_path = 'F:\\pic\\pictures\\80\\'
video_path = 'F:\\\pic\\6d43f157d308d62361204100de195db5.mp4'
if not os.path.exists(save_path):
    os.mkdir(save_path)
def rename(save_path,a):
    pic_l = listdir(save_path)
    s_p = save_path
    for i,y in enumerate(pic_l,start=a):
        if i < 10:
            str1 = '00'+str(i)
        elif i < 100 and i>=10:
            str1 = '0' + str(i)
        else:
            str1 = str(i)
        time1= time.time()
        os.rename(s_p + y,s_p+str1+'.jpg')

if __name__ == '__main__':
    # L = os.listdir('F:\\pic\\crop_img1\\')
    # for x in L:
    #     s_p ='F:\\pic\\crop_img1\\' + x
    #     boxs = [0.0,270.0,200.0,450.0]
    #     src1 = cv2.imread(s_p)
    #     x1 = cv2.resize(src=src1,dsize=(300,300))
    #     cv2.imwrite('F:\\pic\\resize\\'+str(time.time())+'.jpg',x1)
    # vid_to_pic(save_path,video_path)
    rename(save_path,947)