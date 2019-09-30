# 6-2
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color, exposure, feature
from scipy.signal import convolve2d as conv2


img1 = io.imread('../image/pic66.jpg', as_gray=True)
thresh = filters.threshold_otsu(img1)
img2 = (img1 <= thresh)*1.0

plt.figure('show image')
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('translated image')
plt.axis('off')

plt.show()
