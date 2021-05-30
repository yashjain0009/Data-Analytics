#use on google collabratory not working on pycharm unable to download dataset
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
fashion_mnist = keras.datasets.fashion_mnist  # load dataset
(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data()
train_images=train_images/255
test_images=test_images/255
class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
model=keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                        keras.layers.Dense(128,activation='relu'),keras.layers.Dense(10,activation='softmax')])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(train_images,train_labels,epochs=10)
test_loss,test_accuracy=model.evaluate(test_images,test_labels,verbose=1)
predictions = model.predict(test_images)