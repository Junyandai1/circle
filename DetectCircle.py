import cv2
import numpy as np

# read image
image = cv2.imread('/Users/daijunyan/Desktop/WechatIMG366.jpg')

# convert to gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(gray, 
                           cv2.HOUGH_GRADIENT, 
                           dp=1, 
                           minDist=100, 
                           param1=100, 
                           param2=100, 
                           minRadius=100, 
                           maxRadius=600)

# overlay circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

# save image
cv2.imwrite('/Users/daijunyan/Desktop/WechatIMG366.jpg', image)
