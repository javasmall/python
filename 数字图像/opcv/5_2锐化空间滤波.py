from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color, exposure
from scipy.signal import convolve2d as conv2

# 5-2
img1 = cv2.imread('../image/pic4.jpg',0)
psf=np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])/9
img2=conv2(img1,psf,'same')

plt.figure('show image')
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('laplace image')
plt.axis('off')

plt.show()
