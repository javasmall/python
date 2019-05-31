import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread("../image/pic.jpg",0)##读取图片的灰度图
imgorigil=cv.imread("../image/pic.jpg",1)##原始图像
imgorigil=cv.resize(imgorigil,(200,255))##重置大小
img=cv.resize(img,(200,255))

new = cv.resize(img, (200,255), interpolation=cv.INTER_CUBIC)
another_new0 = cv.flip(new, 0)
another_new1 = cv.flip(new, 1)##方向旋转
another_new_1 = cv.flip(new, -1)

ret, binary = cv.threshold(new, 200, 255, cv.THRESH_BINARY)##二值化
print("threshold value %s"%ret)

imgs = np.hstack([new ,binary ])##灰度图而二值图合并
# 展示多个
cv.imshow("original",imgorigil)##显示原始图片
cv.imshow("green and binary", imgs)##显示灰度图和二值图
cv.waitKey(10000)


