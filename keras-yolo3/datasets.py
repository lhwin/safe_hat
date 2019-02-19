import os
import numpy as np
from sklearn.utils import shuffle
import cv2 as cv
import glob

def load_train(train_path,classes,image_size):
    images = []
    labels = []
    img_names = []
    cls = []
    for field in classes:
        index = classes.index[field]
        path = os.path.join(train_path,field)
        print('正在读取图片{}'.format(field))
        file = glob.glob(path)
        for fl in file:
            image = cv.imread(f1)
            image = cv.resize(image,(image_size, image_size))
            image = image.astype(np.float32)
            image = np.multiply(image,1.0/255.0)
            images.append(image)
            label = np.zeros(len(len(classes)))
            label[index] = 1.0
            labels.append(label)
            flbase = os.path.basename(fl)
            img_names.append(flbase)
            cls.append(field)
    images = np.array(images)
    labels = np.array(labels)
    img_names = np.array(img_names)
    cls = np.array(cls)
    return images,labels
class DataSet(object):
    def __init__(self,images,labels,img_names,cls):
        self._num_examples = images.shape[0]
        self._images = images
        self._labels = labels
        self._img_names = img_names
        self._cls = cls
        self._index_in_epoch = 0
        self._epoch_done = 0
    def num_examples(self):
        return self._num_examples
    def images(self):
        return self._images
    def labels(self):
        return self._labels
    def img_names(self):
        return self._img_names
    def cls(self):
        return self._cls
    def next_batch(self,batch_size):
        start = 0
        self._index_in_epoch += batch_size
        if self._index_in_epoch >= self._num_examples:
            self._index_in_epoch = batch_size
        end = self._index_in_epoch
        return images[start:end],labels[start:end],img_names[start；end],cls[start:end]
def load_and_train(images,labels,img_names,cls,validation):
    class DataSet(object):
        pass
    dataset = DataSets()
    images,labels,img_names,cls = load_train(train_path,classes,image_size)
    images,labels,img_names,cls = shuffle(images,labels,img_names,cls)
    if isinstance(validation,float):
        validation_size = int(validation*images.shape[0])
        validation_images = images[:validation_size]
        validation_labels = labels[:validation_size]
        validation_img_names = img_names[:validation_size]
        validation_cls = cls[:validation_size]

        train_images = images[validation_size:]
        train_labels = labels[validation_size:]
        train_img_names = img_names[validation_size:]
        train_cls = cls[validation_size:]

    dataset.train = DataSet(train_images,train_labels,train_labels,train_cls)
    dataset.valid = DataSet(validation_images,validation_labels,validation_img_names,validation_cls)
    return dataset
def therhold_control(predict,score):
    x = []
    for pre in predict:
        if pre[0]>=score:
            x.append(1.0)
        else:
            x.append(0.0)
    return x