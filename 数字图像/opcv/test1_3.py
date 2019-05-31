import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
fn = "../image/pic2.jpg"
print (u'显示原图')
img = cv.imread(fn)
imgdark=cv.resize(img,(300,300))
imgorigil=cv.resize(img,(300,300))
imglight=cv.resize(img,(300,300))
imgfupian=cv.resize(img,(300,300))
print (u'正在处理中')
def matplotlib_multi_pic2(img):
    # 如果总图片个数不超过10，用快速的方法
    for i in range(4):##将通道按照bgr的顺序组合,否则颜色失真
        b, g, r = cv.split(img[i])
        img[i] = cv.merge([r, g, b])
    plt.subplot(221), plt.imshow(img[0]), plt.title("origin")
    plt.subplot(222), plt.imshow(img[1]), plt.title("dark")
    plt.subplot(223), plt.imshow(img[2]), plt.title("light")
    plt.subplot(224), plt.imshow(img[3]), plt.title("fupian")
    plt.show()

def fupianimg(img):
    w = img.shape[1]
    h = img.shape[0]

    # 生成负片
    b, g, r = cv.split(img)
    b = 255 - b
    g = 255 - g
    r = 255 - r  # 直接通过索引改变色彩分量
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r

def changeimg(img,value):##变暗
    w = img.shape[1]
    h = img.shape[0]
    # 全部变暗
    for xi in range(0,w):
        for xj in range(0,h):
            #将像素值整体减少，设为原像素值的(1+value)
            img[xj,xi,0]=int(img[xj,xi,0]*value)
            img[xj,xi,1]=int(img[xj,xi,1]*value)
            img[xj,xi,2]=int(img[xj,xi,2]*value)
changeimg(imgdark,0.4)##变暗
imglight=cv.addWeighted(imglight,0.8,imglight,0.8,0.5)##变亮
fupianimg(imgfupian)
imgs=[imgorigil,imgdark,imglight,imgfupian]
matplotlib_multi_pic2(imgs)
# cv.imshow('original',imgorigil)
# cv.imshow('dark', imgdark)
# cv.imshow('light',imglight)
# cv.imshow('fupian',imgfupian)
# cv.waitKey()
# cv.destroyAllWindows()
