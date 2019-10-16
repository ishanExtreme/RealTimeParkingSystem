Project update log:


1. Begin by adding a mp4 video to the project. Anyone who leverages the project to a CCTV monitoring would replace this with real-time footage.

2. Begin by extracting two images from the video, that will help the model to train finding empty spots on the particular site. NOTE: the frames must be rendered from the video after some time interval so sufficient number of cars have changed position during that time. 
(understand_site.py)

3. From the images taken in step 2, import images one by one and create dataset for  training and testing the CNN.


4. To detect, images = [cv2.imwrite(path) for path in glob.glob()].
   shape[0] = rows, shape[1] = columns
   for i in range(0, rows):
    for j in range(0, columns):
        if(image[i][j] == 0):
            count = count + 1
        total_count = total_count + 1
    if(count/total_count > 0.85):
        cv2.imwrite('', image)

Huge shoutout to Priya Dwivedi (https://towardsdatascience.com/find-where-to-park-in-real-time-using-opencv-and-tensorflow-4307a4c3da03) from whose work
the current work is inspired.

and Nimish Mishra 2nd year IIIT Kalyani for making things smooth for us and helping in this project 

5. numpy, pandas, opencv, keras, pillow, matplotlib, glob, os, tkinter.

6. Three buttons: understand site, Create training data, predict (edge_detection.py + prediction.py).

7. Booking: book_spot.py 

understand_site -> create_data -> edge_detection -> cnn_model -> prediction -> book_spot 
