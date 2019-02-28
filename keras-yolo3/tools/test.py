#author = "Lee Hir"
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from keras.applications import *
import glob
from keras.models import load_model
import tensorflow as tf
import os

# 忽略硬件加速的警告信息
os.environ["CUDA_VISIBLE_DEVICES"] = '0' #use GPU with ID=0
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # maximun alloc gpu50% of MEM
config.gpu_options.allow_growth = True #allocate dynamically
sess = tf.Session(config = config)
# file_path = 'D:\\classify_pic\\test/'
# f_names = glob.glob(file_path + '*.jpg')

# img = []
# # 把图片读取出来放到列表中
# for i in range(len(f_names)):
#     images = image.load_img(f_names[i], target_size=(224, 224))
#     x = image.img_to_array(images)
#     x = np.expand_dims(x, axis=0)
#     img.append(x)
#     print('loading no.%s image' % i)
#
# # 把图片数组联合在一起
# x = np.concatenate([x for x in img])
def predict_cls(x):
    classes = ['hat', 'no_hat']
    model = load_model('tools/3_classifymodel.h5')
    y = model.predict(x)
    y = np.argmax(y,axis=-1)
    pred = [classes[i] for i in y]
    return pred