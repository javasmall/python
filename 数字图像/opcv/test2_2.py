import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("../image/pic1.jpg", 0)
img = cv.resize(img, (328,328))
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
#mode = imgInfo[2]

trans_img = cv.transpose( img )
xuanzhuan = cv.flip(trans_img, -1)##方向旋转

##原图的傅里叶变换

img = cv.imread('../image/pic1.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('original F'), plt.xticks([]), plt.yticks([])
#plt.show()

##平移的傅里叶变换

f = np.fft.fft2(xuanzhuan)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(223),plt.imshow(xuanzhuan, cmap = 'gray')
plt.title('xuanzhuan'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('xuanzhuan F'), plt.xticks([]), plt.yticks([])
plt.show()


