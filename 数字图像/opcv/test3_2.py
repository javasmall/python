#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

def Contrast_and_Brightness(alpha, beta, img):##变亮
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst

src = cv2.imread('../image/pic.jpg',0)
img=cv2.resize(src,(300,300))
cv2.imshow("img", img)

imgliang=Contrast_and_Brightness(0.6,5,img)
cv2.imshow("an",imgliang)
cv2.waitKey(4000)
cv2.destroyAllWindows()
plt.hist(img.ravel(), 256)
plt.ylim((0,1000))
plt.show()
plt.hist(imgliang.ravel(), 256)
plt.ylim(0,1000)
plt.show()
cv2.waitKey(10000)