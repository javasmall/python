import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("../image/pic1.jpg", 0)
img = cv.resize(img, (328,328))
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
#mode = imgInfo[2]

imgyidong = np.zeros(imgInfo, np.uint8)

for i in range( height ):
    for j in range( width - 100 ):
        imgyidong[i, j + 100] = img[i, j]
# cv.imshow('original',img)
# cv.imshow('yidong', imgyidong)
# cv.waitKey(1000)


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

f = np.fft.fft2(imgyidong)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(223),plt.imshow(imgyidong, cmap = 'gray')
plt.title('move'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('move F'), plt.xticks([]), plt.yticks([])
plt.show()


