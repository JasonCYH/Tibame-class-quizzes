import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
load = input("請輸入圖片檔名：")
img = cv2.imread(load, 1)
# cv2.imshow("test", img)
# img.shape[0] = 377
# img.shape[1] = 761
text = input("請輸入浮水印內容：")
size = input("請輸入浮水印尺寸(px)：")
imgpil = Image.fromarray(img)
font = ImageFont.truetype("font/msjhbd.ttc", int(size))
ImageDraw.Draw(imgpil).text((380, 20), text, (0, 0, 0), font)
img = np.array(imgpil)
cv2.imshow("Image M", img)
cv2.waitKey(0)
cv2.destroyAllWindows()