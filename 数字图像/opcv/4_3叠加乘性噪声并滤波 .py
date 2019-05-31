from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random
import copy

# 4-3
def shrink(img, size):
    h, w = img.shape[:2]
    return cv2.resize(img, (w//size, h//size))

img1 = cv2.imread('../image/pic1.jpg', cv2.IMREAD_UNCHANGED)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = copy.deepcopy(img1)
rows, cols, chn = img2.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img2[x, y, :] = 255
img3 = cv2.blur(img2, (5, 5))
img4 = cv2.medianBlur(img2, 3)

plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('multiply noise image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img3, cmap='gray')
plt.title('mean filter')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(img4, cmap='gray')
plt.title('median filter')
plt.axis('off')

plt.show()
