import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def equalHist_demo(image):
    '''全局直方图的图像增强'''
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)#图像增强必须要转灰度图
    dst=cv.equalizeHist(gray) #全局直方图，整体进行图像增强，可能会坏事，不够灵活
    cv.imshow('equalizeHist',dst)

def clahe_demo(image):
    '''局部直方图的图像增强'''
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 图像增强必须要转灰度图
    gray=image
    clahe= cv.createCLAHE(clipLimit=4.0,tileGridSize=(5,5)) #定义CLAHE
    dst=clahe.apply(gray)
    cv.imshow('CLAHE', dst)
    return  dst


src=cv.imread('../image/pic.jpg')
src=cv.resize(src,(300,300))
src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow('src',src)
# equalHist_demo(src)
dst=clahe_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
plt.hist(src.ravel(), 256)
plt.ylim(0,2000)
plt.show()
plt.hist(dst.ravel(), 256)
plt.ylim(0,2000)
plt.show()