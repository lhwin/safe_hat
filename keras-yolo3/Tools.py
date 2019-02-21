#author = "Lee Hir"
import numpy as np
import cv2
from keras.models import load_model
classes=['bicycle','motor']
def predict(img, target_size=(224,224),classes=['bicycle','motor']):
    img = cv2.resize(img,target_size)
    img = np.multiply(img,1.0/255)
    x = np.expand_dims(img, axis=0)
    model = load_model('classifymodel.h5')
    preds = model.predict(x)[0]
    pred_indices = np.argmax(preds)
    pred = classes[pred_indices]
    score = round(preds[pred_indices],2)
    return pred,score

def crop_image(image,box):
    src = image[int(box[1]):int(box[3]),int(box[0]):int(box[2])]
    return src
