from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def PepperandSalt(src, percetage):
    NoiseImg = src
    NoiseNum = int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX = random.randint(0, src.shape[0]-1)
        randY = random.randint(0, src.shape[1]-1)
        if random.randint(0, 1) <= 0.5:
            NoiseImg[randX, randY] = 0
        else:
            NoiseImg[randX, randY] = 255
    return NoiseImg

def shrink(img, size):
    h, w = img.shape[:2]
    return cv2.resize(img, (w//size, h//size))
img1 = cv2.imread('../image/pic3.jpg', 0)
img2 = PepperandSalt(shrink(img1, 4), 0.02)
img3 = cv2.blur(img2, (5, 5))
img4 = cv2.medianBlur(img2, 3)

plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('pepper salt noise image')
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
