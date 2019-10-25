
import matplotlib.pyplot as plt
import cv2
import os, glob
import numpy as np
# Somehow this shows unresolved imports but that's not a big problem
from GuiForFrame import counter,counter_2
frame1 = counter.get()
frame2 = counter_2.get()



video = 'parking_video.mp4'
cap = cv2.VideoCapture(video)
  
# Used as counter variable 
count = 0
  
# checks whether frames were extracted 
success = 1
  
while success: 
    success, image = cap.read()  # Bypassing the first few frames as they would definitely be bad
    if(count == frame1 or count == frame2):
        if(count == frame1):
            cv2.imwrite("understand_site/understand_site_train.jpg", image) 
        else:
            cv2.imwrite("understand_site/understand_site_test.jpg", image) 
    count += 1

