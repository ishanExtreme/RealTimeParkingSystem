import os
import numpy as np
from PIL import Image
from keras.applications.imagenet_utils import preprocess_input
from keras.models import load_model
from keras.preprocessing import image
import cv2
import matplotlib.pyplot as plt
import pickle
#from prediction import empty_slots
#from edge_detection import test_images, show_images
file1 = open("name.txt","r+")
name = file1.read()
file1.close()
file2 = open("number_plate.txt","r+")
numberPlate = file2.read()
file2.close()

with open('free_spots.pickle', 'rb') as fp:
    empty_slots = pickle.load(fp)
a=len(empty_slots)
file1 = open("empty_slots.txt","w") 
file1.write(str(a)) 
file1.close()

def book_slots(image, name,numberPlate):
    overlay = np.copy(image)
    free_slot = empty_slots[0]
    (x1, y1, x2, y2) = free_slot
    (x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
    cv2.rectangle(overlay, (int(x1),int(y1)), (int(x2),int(y2)), [0, 255, 0], -1)
    cv2.putText(overlay, name, (30, 95), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
    cv2.putText(overlay, numberPlate, (30, 195), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
    #cv2.imwrite( str(image) + ".jpg" , overlay)
    plt.imshow(overlay)
    plt.show()
    del empty_slots[0]
    return image

def capture_screen(name,numberPlate):
    frame = 0
    cap = cv2.VideoCapture("parking_video.mp4")
    while True:
        success, image = cap.read()
        if(frame == 100):
            break
        frame = frame + 1
    book_slots(image, name,numberPlate)
    with open('free_spots.pickle', 'wb') as handle:
        pickle.dump(empty_slots, handle, protocol=pickle.HIGHEST_PROTOCOL)



capture_screen(name,numberPlate)
