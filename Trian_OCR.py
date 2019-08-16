import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract

def recognize_text( img ):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary-image", open_out)
    cv.bitwise_not(open_out, open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print("识别结果: %s"%text)

def main():
    img = cv.imread("ocr_demo.png")
    cv.namedWindow("Show", cv.WINDOW_AUTOSIZE)
    cv.imshow("Show", img)
    recognize_text(img)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()