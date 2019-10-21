from PIL import Image
from PIL import ImageGrab
from PIL import Image
infile = 'bizhi.jpg'
outfile = '../img/bigimage/1.jpg'
img = Image.open(infile)



width = img.size[0]   # 获取宽度
height = img.size[1]   # 获取高度
img = img.resize((int(width*3), int(height*3)), Image.AFFINE)
img.save("love.jpg")

