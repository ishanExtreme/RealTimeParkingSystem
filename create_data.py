import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob


def show_images(images, cmap=None):
    cols = 2 # Displaying the images side by side 
    rows = (len(images)+1)//cols # Deciding the number of rows (essentially the height)
    # of the images
    
    plt.figure(figsize=(15, 12)) # Creating the figure upon which the images shall be drawn
    
    # For the following loop, assume two images: image1 and image2
    for i, image in enumerate(images): # enumerate serves to attach a key to each image, 0:image1 and 1:image2
        plt.subplot(rows, cols, i+1) # creating 2 subplots upon the figure generated above. Upon these subplots, we will draw our images.

        # use gray scale color map if there is only one channel
        cmap = 'gray' if len(image.shape)==2 else cmap

        plt.imshow(image, cmap=cmap) # Draw the image
        plt.xticks([]) # Label the x-axis with Nothing (i.e. empty list denoted by [])
        plt.yticks([]) # Label the y-axis with Nothing (i.e. empty list denoted by [])
    plt.tight_layout(pad=0, h_pad=0, w_pad=0) # Finalizing the padding of the images in the layout
    plt.show() # Display the images.


def select_rgb_white_yellow(image): 
    # White and yellow masking combined
    # white color mask
    lower = np.uint8([120, 120, 120])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(image, lower, upper)
    # yellow color mask
    lower = np.uint8([190, 190,   0])
    upper = np.uint8([255, 255, 255])
    yellow_mask = cv2.inRange(image, lower, upper)
    # combine the mask
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked


def convert_gray_scale(image):
    # It is easier for CNNs to understand a single channel image rather than several channel images.
    # Hence we convert the 3 channel RGB images to single channel greyscale images
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# Loading the images to create the data for the CNN 
# glob.glob(PATH_TO_IMAGES) serves to load the path of the images and save those paths in the variable 'path'
# plt.imread() serves to read those images.
# [plt.imread()] serves to project the read images into a list which is then stored into the variable 'test_images'
test_images = [plt.imread(path) for path in glob.glob('understand_site/*.jpg')]



# Merging the white and the yellow masks
white_yellow_images = list(map(select_rgb_white_yellow, test_images))

# Converting the RGB images to single channel greyscale images
gray_images = list(map(convert_gray_scale, white_yellow_images))



# Uncomment this line during testing to determine if the greyscales are being converted fine enough
#show_images(gray_images)