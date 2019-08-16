# import cv2 as cv
# import os
#
# '''
# step:
# 1.图片处理 - 对图片进行降噪、二值化处理
# 2.切割图片 - 将图片切割成单个字符并保存
# 3.人工标注 - 对切割的字符图片进行人工标注，作为训练集
# 4.训练数据 - 用KNN算法训练数据
# 5.检测结果 - 用上一步的训练结果识别新的验证码
# '''
#
# PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
# img_path = os.path.join(PROJECT_ROOT,'code.jpeg')
# img = cv.imread(img_path)
# gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # 先转换为灰度图才能够使用图像阈值化
# #cv.adaptiveThreshold()  大于127=>0   小于127=>255
# ret, img_invert = cv.threshold(gray_img,127,255,cv.THRESH_BINARY_INV)



import cv2 as cv
from PIL import Image
import pytesseract #要配置tesseract-ocr 引擎的

def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))#去除线
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)# 黑色背景变为白色背景
    cv.imshow('open_out', open_out)

    textImage = Image.fromarray(open_out)#从np.array 转换成<class 'PIL.Image.Image'>，pytesseract需要接受此类型
    text = pytesseract.image_to_string(textImage)
    print("This OK:%s"%text)

if __name__ == '__main__':
    src = cv.imread("code.jpeg")
    cv.imshow("src", src)
    recognize_text()
    cv.waitKey(0)
    cv.destroyAllWindows()

