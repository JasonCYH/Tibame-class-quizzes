import time
import colorama as col
import os
a = "  "
b = 1
col.init(True)
while True:
	if b > 6:
		print(a*2,col.Back.GREEN+a,end = "")	
	elif b >5:
		print(a,col.Back.YELLOW+a,end = "")
	elif b >= 0:
		print(col.Back.RED+a,end = "")
	b = b % 10
	print("\n"+str(b))
	b += 1
	time.sleep(1)
	os.system("cls")
