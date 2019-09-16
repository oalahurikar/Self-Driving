import os
import csv

samples = []
with open('C:\\Users\\olahurikar\\Desktop\\Training Data\\Data_Final\\driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

from sklearn.model_selection import train_test_split

train_samples, validation_samples = train_test_split(samples, test_size=0.2)

import cv2
import numpy as np
import sklearn
from sklearn.utils import shuffle

def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1:  # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset + batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                center_angle = float(batch_sample[3])
                # create adjusted steering measurements for the side camera images
                correction = 0.4  # this is a parameter to tune
                steering_left = center_angle + correction
                steering_right = center_angle - correction
                angles.extend((center_angle, steering_left, steering_right))

                for i in range(3):
                    # filenames.append(os.path.basename(batch_sample[i]))
                    path = 'C:\\Users\\olahurikar\\Desktop\\Training Data\\Data_Final\\IMG\\'
                    images.append((cv2.imread(path + os.path.basename(batch_sample[i]))))

            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)


# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)

from keras.models import Sequential
from keras.layers import Input, Activation, Flatten, Dropout, Dense, Lambda, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import Adam

model = Sequential()
model.add(Cropping2D(cropping=((70, 25), (0, 0)),
                     dim_ordering="tf",
                     input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: x / 255 - 0.5))
# First Convolution Layer kernel size 5x5
model.add(Convolution2D(24, kernel_size=(5, 5), subsample=(2, 2), activation="relu", border_mode="same"))
model.add(Convolution2D(36, kernel_size=(5, 5), subsample=(2, 2), activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Convolution2D(48, kernel_size=(5, 5), subsample=(2, 2), activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.35))
# Karnel size 3x3
model.add(Convolution2D(64, kernel_size=(3, 3), activation="relu", border_mode="same"))
model.add(Convolution2D(64, kernel_size=(3, 3), activation="relu", border_mode="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
# Fully connected layer
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.35))
model.add(Dense(50))
model.add(Dropout(0.5))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

# adam = Adam(lr=0.01)
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

from keras.models import Model
import matplotlib.pyplot as plt

# Model fitting
history_object = model.fit_generator(train_generator,

                                     samples_per_epoch=len(train_samples),
                                     validation_data=validation_generator,
                                     nb_val_samples=len(validation_samples),
                                     nb_epoch=3,
                                     verbose=1)
### print the keys contained in the history object
print(history_object.history.keys())

### plot the training and validation loss for each epoch
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.show()
# Print out summary of the model
model.summary()
model.save('model_final.h5')
print("Model Saved")
