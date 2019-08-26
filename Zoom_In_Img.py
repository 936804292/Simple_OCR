import cv2 as cv
import numpy as np

def GetZoomIn(srcImg,multp):
    imgs = cv.imread(srcImg,1)
    imgInfos = imgs.shape
    height = imgInfos[0]
    width = imgInfos[1]
    destHeight = int(height/multp)
    destWidth = int(width/multp)
    # uint8:limit 0-255
    destImage = np.zeros((destHeight,destWidth,3),np.uint8)

    for i in range(0,destHeight):
        for j in range(0,destWidth):
            # Calculate:newX = srcX*(src.Height/destHeight)<---->zoom in
            iNew = int(i*(height*1.0/destHeight))
            jNew = int(j*(width*1.0/destWidth))
            destImage[i,j] = imgs[iNew,jNew]
    return destImage


cv.imshow('dest',GetZoomIn('nina.png',2))
cv.imshow('src',GetZoomIn('nina.png',1))
cv.waitKey(0)