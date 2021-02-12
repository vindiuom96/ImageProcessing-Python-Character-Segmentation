import os.path
import cv2

# image path and valid extensions
imageDir = 'C:/Users/acer/Documents/FYP/DataSet/input'  # specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]  # specify your valid extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

# create a list all files in directory and
# append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))
d = 0
# loop through image_path_list to open each image
for imagePath in image_path_list:
    img = cv2.imread(imagePath, 0)
    cv2.threshold(img, 225, 255, cv2.THRESH_BINARY, img)[1]
    cv2.bitwise_not(img, img)
    # cv2.imwrite("output_%d.png"%d,img)
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        # draw a green rectangle to visualize the bounding rect
        # cv2.rectangle(img, (x, y), (x + w, y + h), 255, 1)
        roi = img[y:y + h, x:x + w]
        # cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
        cv2.bitwise_not(roi, roi)
        roi = cv2.resize(roi, (50, 50), 0, 0, cv2.INTER_LINEAR)
        cv2.threshold(roi, 100, 255, cv2.THRESH_BINARY, roi)[1]
        cv2.imwrite('C:/Users/acer/Documents/FYP/DataSet/output/output_%d.jpg' % d, roi)
        d += 1
    print('number of contours:', len(contours))