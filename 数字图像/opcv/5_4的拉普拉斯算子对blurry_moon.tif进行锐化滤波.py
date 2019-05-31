# 5-4
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color, exposure
from scipy.signal import convolve2d as conv2


def genlaplacian(n):
    matrix = np.ones((n, n), dtype=np.int)
    matrix[n//2][n//2] = 1-n*n
    return matrix

img1 = io.imread('../image/pic1.jpg', as_gray=True)
img2 = conv2(img1, genlaplacian(5)/25, 'same')
img3 = conv2(img1, genlaplacian(9)/81, 'same')
img4 = conv2(img1, genlaplacian(15)/225, 'same')
img5 = conv2(img1, genlaplacian(25)/625, 'same')

plt.figure('show image')
plt.subplot(2, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title('laplace 5x5 image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(img3, cmap='gray')
plt.title('laplace 9x9 image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img4, cmap='gray')
plt.title('laplace 15x15 image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(img5, cmap='gray')
plt.title('laplace 25x25 image')
plt.axis('off')

plt.show()
