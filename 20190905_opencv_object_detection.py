# 因家中電腦函式庫路徑較亂，新增此函式庫路徑
import sys
sys.path.append("C:\\Users\\su\\PycharmProjects\\demo.py\\venv\\Lib\\site-packages")

import cv2
import numpy as np

# 讀取影片特定幀數
video = cv2.VideoCapture("homework3.mp4")
while True:
	b, v = video.read()
	if b == True:
		# 模糊化
		mdb = cv2.blur(v,(15,15))
		# cv2.imshow("Image 1", mdb)
		# 二值化
		thr = cv2.adaptiveThreshold(mdb[:, :, 2], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 53, 20)
		# cv2.imshow("Image 2", thr)
		# 模糊化
		blr=cv2.blur(thr,(10,10))
		# cv2.imshow("Image 3", blr)
		# 二值化
		thr2 = cv2.adaptiveThreshold(blr, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 53, 20)
		# cv2.imshow("Image 4", thr2)
		# 模糊化
		blr3=cv2.blur(thr2,(10,10))
		# cv2.imshow("Image 5", blr3)
		# 各像素二進位後做NOT運算
		notblr=cv2.bitwise_not(blr3)
		# cv2.imshow("Image 6", notblr)

		# 取得輪廓
		p, d = cv2.findContours(notblr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		# 繪製輪廓
		a = np.full(notblr.shape, 255,np.uint8)
		a = cv2.cvtColor(a, cv2.COLOR_GRAY2BGR)
		cv2.drawContours(a,p,-1,(0, 0, 255),1)
		# cv2.imshow("Image 7", a)

		# 繪製矩形
		for c in p:
			x, y, w, h = cv2.boundingRect(c)
			if int(w * h) > 2304:
				cv2.rectangle(v, (x, y), (x + w,y + h), (0, 0, 255), 3)
		cv2.imshow("Image Result", v)
		if cv2.waitKey(1000//34) == 13:
			break
	else:
		break

