import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def matplotlib_multi_pic2(img):
    # 如果总图片个数不超过10，用快速的方法
    for i in range(6):##将通道按照bgr的顺序组合,否则颜色失真
        b, g, r = cv.split(img[i])
        img[i] = cv.merge([r, g, b])
    plt.subplot(321), plt.imshow(img[0]), plt.title("origin1")
    plt.subplot(322), plt.imshow(img[1]), plt.title("origin2")
    plt.subplot(323), plt.imshow(img[2]), plt.title("add")
    plt.subplot(324), plt.imshow(img[3]), plt.title("substarct")
    plt.subplot(325), plt.imshow(img[4]), plt.title("mutilpate")
    plt.subplot(326), plt.imshow(img[5]), plt.title("divide")

    plt.show()
img1 = cv.imread('../image/pic66.jpg')
img2 = cv.imread('../image/pic2.jpg')
res1=cv.resize(img1,(320,320),interpolation=cv.INTER_CUBIC)
res2=cv.resize(img2,(320,320),interpolation=cv.INTER_CUBIC)##立方插值
imgadd = cv.addWeighted(res1,0.5,res2,0.5,0.5)##亮度
imgsubtracted=cv.subtract(res1,res2)
imgmultiply=cv.multiply(res1,res2)
imgdivide=cv.divide(res1,res2)
imgs=[res1,res2,imgadd,imgsubtracted,imgmultiply,imgdivide]##图片数组
matplotlib_multi_pic2(imgs)
# cv.imshow("origi1",res1)
# cv.imshow("origi2",res2)
# cv.imshow("add",imgadd)
# cv.imshow("substract",imgsubtracted)
# cv.imshow("multiply",imgmultiply)
# cv.imshow("divide",imgdivide)
# cv.waitKey(10000)