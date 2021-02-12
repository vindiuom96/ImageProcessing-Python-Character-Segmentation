import cv2
import thinning

img = cv2.imread("./input1.JPG")
constant = cv2.copyMakeBorder(img, 2, 2, 2, 2,
                              cv2.BORDER_CONSTANT)  # adding 1 pixel thick border since image touches the existing
# boundary
img_gray = cv2.cvtColor(constant, cv2.COLOR_BGR2GRAY)
thinned = thinning.guo_hall_thinning(img_gray)
cv2.imwrite("skelta/thinned2.png", thinned)

# this is the most suitable code for the project
