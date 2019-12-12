import os
import sys
import pymysql
cnct = pymysql.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	db = "python_ai_2018",
	charset = "utf8"
) 
os.system("cls")
print("""
(0) 離開程式
(1) 顯示會員列表
(2) 新增會員資料
(3) 更新會員資料
(4) 刪除會員資料
(5) 新增會員的電話
(6) 刪除會員的電話
""")
a = int(input("指令："))
while a != 0:
	os.system("cls")
	if a == 1:
		cmnd = cnct.cursor()
		x = cmnd.execute("SELECT `member`.`id`, `name`, `birthday`, `address`, `tel` FROM `member` LEFT JOIN `tel` ON `member`.`id` = `tel`.`member_id`")
		y = cmnd.fetchall()
		table = pttb.PrettyTable(["編號","姓名", "生日", "地址", "電話"], encoding = "utf8")
		for b in y[:]:
			table.add_row(b)
			table.align["編號"] = "l"
			table.align["姓名"] = "l"
			table.align["生日"] = "l"
			table.align["地址"] = "l"
		print(table)
		cnct.commit()
	elif a == 2:
		cmnd = cnct.cursor()
		b = input("請輸入會員姓名：")
		c = input("請輸入會員生日：")
		d = input("請輸入會員地址：")
		cmnd.execute("INSERT INTO `member`(name, birthday, address) VALUES(%s, %s, %s)", (b, c, d))
		cnct.commit()
	elif a == 3:
		cmnd = cnct.cursor()
		x = cmnd.execute("SELECT * FROM `member`")
		y = cmnd.fetchall()
		for z in y:
			print(z)
		b = input("請選擇你要修改的資料編號：")
		c = input("請輸入會員姓名：")
		d = input("請輸入會員生日：")
		f = input("請輸入會員地址：")	
		cmnd.execute("UPDATE `member` SET `name` = %s, `birthday` = %s, `address` = %s WHERE `id` = %s",(c, d, f, b))
		cnct.commit()
	elif a == 4:
		cmnd = cnct.cursor()
		x = cmnd.execute("SELECT * FROM `member`")
		y = cmnd.fetchall()
		for z in y:
			print(z)
		b = input("請選擇你要刪除的資料編號：")
		cmnd.execute("DELETE FROM `member` WHERE `id` = %s", b)
		cnct.commit()
	elif a == 5:
		cmnd = cnct.cursor()
		x = cmnd.execute("SELECT `member`.`id`, `name`, `birthday`, `address`, `tel` FROM `member` LEFT JOIN `tel` ON `member`.`id` = `tel`.`member_id`")
		y = cmnd.fetchall()
		for z in y:
			print(z)
		b = input("請選擇要添加電話的會員編號：")
		c = input("請輸入電話：")
		cmnd.execute("INSERT INTO `tel`(`member_id`, `tel`) VALUES (%s, %s)", (b, c))
		cnct.commit()
	elif a == 6:
		cmnd = cnct.cursor()
		x = cmnd.execute("SELECT `member`.`id`, `name`, `birthday`, `address`, `tel` FROM `member` LEFT JOIN `tel` ON `member`.`id` = `tel`.`member_id`")
		y = cmnd.fetchall()
		for z in y:
			print(z)
		b = input("請選擇要刪除電話的會員編號：")
		cmnd.execute("SELECT * FROM `tel` WHERE `member_id` = %s", b)
		d = cmnd.fetchall()
		for f in d:
			print(f)
		c = input("請輸入要刪除的電話編號：")
		cmnd.execute("DELETE FROM `tel` WHERE `id` = %s", c)
		cnct.commit()

	print("""
(0) 離開程式
(1) 顯示會員列表
(2) 新增會員資料
(3) 更新會員資料
(4) 刪除會員資料
(5) 新增會員的電話
(6) 刪除會員的電話
""")
	a = int(input("指令："))

cnct.close()