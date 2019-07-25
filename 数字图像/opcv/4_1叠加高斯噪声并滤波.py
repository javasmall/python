from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

# 4-1
def gasuss_noise(image, mean=0, var=0.02):
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out


def shrink(img, size):
    h, w = img.shape[:2]
    return cv2.resize(img, (w//size, h//size))


img1 = cv2.imread('../image/pic1.jpg', 0)

img1 = shrink(img1, 4)
img2 = gasuss_noise(img1)
img3 = cv2.blur(img2, (5, 5))
img4 = cv2.medianBlur(img2, 3)


plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('gasuss noise image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img3, cmap='gray')
plt.title('mean filter')

plt.subplot(2, 2, 4)
plt.imshow(img4, cmap='gray')
plt.title('median filter')

plt.show()
