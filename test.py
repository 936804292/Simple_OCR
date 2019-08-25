import pytesseract
from PIL import Image
import cv2 as cv

def Test(*args):
    print(args)

#git push origin master
img = cv.imread("./test.jpg")
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# thresh = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
th = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,5)
# 均值滤波
img_mean = cv.blur(img, (5,5))

# 高斯滤波
img_Guassian = cv.GaussianBlur(img,(5,5),0)

# 中值滤波
img_median = cv.medianBlur(img, 5)

# 双边滤波
img_bilater = cv.bilateralFilter(img,9,75,75)

code = pytesseract.image_to_string(th)
_mean = pytesseract.image_to_string(img_bilater)
gray_s = pytesseract.image_to_string(img_Guassian)

#cv.imshow("_mean",img_mean)
cv.imshow("gray_s",img_Guassian)
print(gray_s)
#print(_mean)
Test("1",2,"qwe")
cv.waitKey(0)