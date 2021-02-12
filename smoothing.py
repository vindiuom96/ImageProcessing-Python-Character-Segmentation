from os import listdir
import os, os.path
import numpy
import cv2


# image path and valid extensions
imageDir = 'C:/Users/acer/Downloads/Final year Project/DataSet/input3'  # specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

# create a list all files in directory and
# append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))
d=0
# loop through image_path_list to open each image
for imagePath in image_path_list:
    img = cv2.imread(imagePath,0)
    cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, img)
    #cv2.bitwise_not(img, img)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, blur)
    cv2.imwrite("output3/output_%d.png"%d, blur)
    d+=1
    key = cv2.waitKey(0)
    if key == 27:  # escape
        break

# close any open windows
cv2.destroyAllWindows()