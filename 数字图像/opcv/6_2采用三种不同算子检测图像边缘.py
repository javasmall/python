# 6-1
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color, exposure,feature
from scipy.signal import convolve2d as conv2


img1 = io.imread('../image/pic4.jpg', as_gray=True)
img2=filters.prewitt(img1)
img3=filters.scharr(img1)
img4=feature.canny(img1)

plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('prewitt image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img3, cmap='gray')
plt.title('zerocross image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(img4, cmap='gray')
plt.title('canny image')
plt.axis('off')

plt.show()
