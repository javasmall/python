from PIL import Image, ImageChops
import matplotlib.pyplot as plt

def test(img,num):
    w,h=img.size
    return img.resize((w//num,h//num),Image.NEAREST)

img1 = Image.open('../image/pic2.jpg')
img1 = test(img1,2)
img2 = test(img1,2)
img3 = test(img2,2)
img4 = test(img3,2)


plt.figure('show image')
plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title('2x image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img2)
plt.title('4x image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img3)
plt.title('8x image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(img4)
plt.title('16x image')
plt.axis('off')

plt.show()
