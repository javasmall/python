# 5-5
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color, exposure
from scipy.signal import convolve2d as conv2

img1 = io.imread('../image/pic2.jpg', as_gray=True)
img2 = filters.laplace(img1)
img3=filters.prewitt(img1)
img4=filters.roberts(img1)
img5=filters.sobel(img1)
img6=filters.scharr(img1)

plt.figure('show image')
plt.subplot(2, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title('operator1 image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(img3, cmap='gray')
plt.title('operator2 image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img4, cmap='gray')
plt.title('operator3 image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(img5, cmap='gray')
plt.title('operator4 image')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(img5, cmap='gray')
plt.title('operator5 image')
plt.axis('off')

plt.show()
