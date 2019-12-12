import os
import sys
import codecs as code
os.system("cls")
print("工作路徑:" + os.getcwd())
print("""	(0) 離開程式
	(1) 列出檔案
	(2) 列出資料夾
	(3) 顯示檔案內容
	(4) 刪除檔案
	(5) 執行檔案
	(6) 進入資料夾
	(7) 刪除資料夾
	(8) 回上層資料夾""")
a = int(input("操作: "))
b = os.listdir("./")
while a != 0:
	os.system("cls")
	if a == 1:
		for c in b:
			if os.path.isfile("./"+c):
				print(c)
		print("")
	elif a == 2:
		for c in b:
			if os.path.isdir("./"+c):
				print(c)
		print("")
	elif a == 3:
		d = 0
		f = []
		for c in b:
			print(d,c)
			f.append(c)
			d += 1
		print("")
		g = int(input("請輸入檔案索引： "))
		h = code.open(f[g],"r","utf8")
		print("================檔案開始================")
		print(h.read())
		h.close()
		print("================檔案結束================")
	elif a == 4:
		d = 0
		f = []
		for c in b:
			if os.path.isfile("./"+c):
				print(d,c)
				f.append(c)
				d += 1
		print("")
		g = int(input("請輸入檔案索引： "))
		if os.path.exists(f[g]):
			os.remove(f[g])
	elif a == 5:
		d = 0
		f = []
		for c in b:
			if os.path.isfile("./"+c):
				print(d,c)
				f.append(c)
				d += 1
		print("")
		g = int(input("請輸入檔案索引： "))
		os.system("start "+f[g])

	elif a == 6:
		d = 0
		f = []
		for c in b:
			if os.path.isdir("./"+c):
				print(d,c)
				f.append(c)
				d += 1
		print("")
		g = int(input("請輸入檔案索引： "))
		if os.path.exists(f[g]):
			os.chdir("./"+f[g])
	elif a == 7:
		d = 0
		f = []
		for c in b:
			if os.path.isdir("./"+c):
				print(d,c)
				f.append(c)
				d += 1
		print("")
		g = int(input("請輸入檔案索引： "))
		if os.path.exists(f[g]):
			os.remove(f[g])
	elif a == 8:
		os.chdir("../")
	print("工作路徑:" + os.getcwd())
	print("""	(0) 離開程式
	(1) 列出檔案
	(2) 列出資料夾
	(3) 顯示檔案內容
	(4) 刪除檔案
	(5) 執行檔案
	(6) 進入資料夾
	(7) 刪除資料夾
	(8) 回上層資料夾""")
	a = int(input("操作: "))