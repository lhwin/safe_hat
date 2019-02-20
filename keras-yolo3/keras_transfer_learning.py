from keras.applications.inception_v3 import InceptionV3
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import SGD
import data_sets
from sklearn.model_selection import train_test_split
class Classification(object):
    def __init__(self,train_path,image_size,classes):
        self.train_path = 'D:\\project_file\\train_data\\smoke_car\\trian\\'
        self.image_size = 224
        self.classes = ['no_hat', 'hat']
        self.X,self.Y = data_sets.load_train(self.train_path, self.image_size, self.classes)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=0.2, random_state=20)
    def train(self):
        base_model = VGG16(weights='imagenet')
        base_model = InceptionV3(weights='imagenet', include_top=False)
        x = base_model.output
        x = Dense(1024, activation='relu')(x)
        predictions = Dense(2, activation='softmax')(x)

        model = Model(inputs=base_model.input, outputs=predictions)

        model = Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])
    model.fit(self.X_train, self.y_train, epochs=50, batch_size=25)
    score ,acc = model.evaluate(self.X_test, self.y_test, batch_size=25)

    model.save('classifymodel.h5')
    def detection(self):
