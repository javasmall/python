from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data, io, filters, color,exposure

img1 = io.imread('../image/pic2.jpg', as_gray=True)
img2=filters.sobel_v(img1)
img3=filters.prewitt_v(img1)
img4=filters.laplace(img1)

plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('sobel image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img3, cmap='gray')
plt.title('prewitt image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(img4, cmap='gray')
plt.title('laplace image')
plt.axis('off')

plt.show()
