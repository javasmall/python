from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np
# 3-2
img = Image.open('../image/pic1.jpg')
img1 = np.array(img.convert('L')).flatten()
img2 = np.array(img.convert('L').point(lambda p: p * 0.5)).flatten()

plt.figure('show image')
plt.subplot(1, 2, 1)
plt.hist(img1, bins=256, normed=1, color='blue', alpha=0.75)
plt.title('original image')

plt.subplot(1, 2, 2)
plt.hist(img2, bins=256, normed=1, color='blue', alpha=0.75)
plt.title('darker image')

plt.show()
