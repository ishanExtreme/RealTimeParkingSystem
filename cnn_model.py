import numpy
import os
import cv2
import matplotlib.pyplot as plt
import glob
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras import backend as k
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping


def load_data():
    # glob.glob(/*.jpg) tends to include include all the files in the given directory that match with the given extension
    # 'for path in glob.glob()' tends to extract the path of each of these files
    # plt.imread(path) implies all the images in a particular directory are read into the program. This is handled by the glob.glob() thing
    # [] outside the entire line of code serves to encapsulate the entire matrices read into a list which is then assigned to the respective variable name
    train_data_occupied = [plt.imread(path) for path in glob.glob('cnn/train_cnn/occupied/*.jpg')]
    train_data_empty = [plt.imread(path) for path in glob.glob('cnn/train_cnn/empty/*.jpg')]
    test_data_occupied  = [plt.imread(path) for path in glob.glob('cnn/test_cnn/occupied/*.jpg')]
    test_data_empty  = [plt.imread(path) for path in glob.glob('cnn/test_cnn/empty/*.jpg')]
    return train_data_occupied, train_data_empty, test_data_occupied, test_data_empty




train_data_occupied, train_data_empty, test_data_occupied, test_data_empty = load_data()
img_width, img_height = 48, 48 # The CNN will clearly understand light weight images. Hence choosing 48 * 48 pixels

nb_train_samples = len(train_data_occupied) + len(train_data_empty) # The number of images loaded into the training purpose of the model
nb_validation_samples = len(test_data_occupied) + len(test_data_empty) # The number of images loaded into the testing purpose of the model
batch_size = 32 # Batch size determines the number of images sent into the model at a single given time. It's usually a power of 2.
epochs = 15 # The number of iterations on which to train the model
num_classes = 2 # To classify as empty/filled
# The above ones are all general values that usually let the model fit better


########################################################

# We have used transfer learning on the famous VGG16 model, freezing the last few layers 

model = applications.VGG16(weights = "imagenet", include_top=False, input_shape = (img_width, img_height, 3))
for layer in model.layers[:10]:
    layer.trainable = False

x = model.output
x = Flatten()(x)
# # x = Dense(512, activation="relu")(x)
# # x = Dropout(0.5)(x)
# # x = Dense(256, activation="relu")(x)
# # x = Dropout(0.5)(x)
predictions = Dense(num_classes, activation="softmax")(x)

model_final = Model(input = model.input, output = predictions)

model_final.compile(loss = "categorical_crossentropy", 
                    optimizer = optimizers.SGD(lr=0.0001, momentum=0.9), 
                    metrics=["accuracy"]) 



# # Initiate the train and test generators with data augumentation
# The number of training samples is pretty small, so we need to create some more image data by:
# 1. Rescaling
# 2. Flipping 
# 3. Cropping/ zooming etc.
train_datagen = ImageDataGenerator(
rescale = 1./255,
horizontal_flip = True,
fill_mode = "nearest",
zoom_range = 0.1,
width_shift_range = 0.1,
height_shift_range=0.1,
rotation_range=5)

test_datagen = ImageDataGenerator(
rescale = 1./255,
horizontal_flip = True,
fill_mode = "nearest",
zoom_range = 0.1,
width_shift_range = 0.1,
height_shift_range=0.1,
rotation_range=5)

# The below two functions serve to pick up the images from the given directories, and apply the data generator 
# created above
# flow_from_directory(): as the function suggests, flows the images from the directory to the program.
train_generator = train_datagen.flow_from_directory(
"cnn/train_cnn",
target_size = (img_height, img_width),
batch_size = batch_size,
class_mode = "categorical")

validation_generator = test_datagen.flow_from_directory(
"cnn/test_cnn",
target_size = (img_height, img_width),
class_mode = "categorical")



# # Save the model according to the conditions
checkpoint = ModelCheckpoint("car1.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
early = EarlyStopping(monitor='val_acc', min_delta=0, patience=10, verbose=1, mode='auto')



# ### Start training!

history_object = model_final.fit_generator(
train_generator,
steps_per_epoch = nb_train_samples,
epochs = epochs,
validation_data = validation_generator,
validation_steps = nb_validation_samples,
callbacks = [checkpoint, early])



