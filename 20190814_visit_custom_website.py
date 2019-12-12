# 導入sys及os library
import sys
import os

# command-line中，要用預設瀏覽器開啟網址，要輸入：start 網址，所以用sys.argv來將別人打的網址輸入到此程式中
# 又因cmd中對於空格要求嚴格，為了避免系統錯誤，將輸入到的長度訂在2個資料，而第二個資料就是網址，所以將其接回並用system方法輸出到cmd
if len(sys.argv) ==2:
	os.system("start "+sys.argv[1])
else:
	print("請輸入網址!")