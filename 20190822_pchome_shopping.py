import sys
sys.path.append("C:\\Users\\su\\PycharmProjects\\demo.py\\venv\\Lib\\site-packages")	# 因自己的電腦讀取modules有問題而設
import os
import requests
import json
import prettytable
a = input("關鍵字：")
os.system("cls")
website = requests.get(
	"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="+a+"&page=1&sort=sale/dc",
)
website.encoding = "utf8"
jsn = json.loads(website.text)
table = prettytable.PrettyTable(["名稱", "價格"], encoding = "utf8")
total = jsn["totalPage"]
for r in jsn["prods"]:
	table.add_row([r["name"], r["price"]])
	table.align["名稱"] = "l"
	table.align["價格"] = "l"
print(table)
b = 1
while int(b) != 0 and int(b) <= total:
	website = requests.get(
		"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="+a+"&page="+str(b)+"&sort=sale/dc",
	)
	website.encoding = "utf8"
	jsn = json.loads(website.text)
	table = prettytable.PrettyTable(["名稱", "價格"], encoding = "utf8")
	for r in jsn["prods"]:
		table.add_row([r["name"], r["price"]])
		table.align["名稱"] = "l"
		table.align["價格"] = "l"
	os.system("cls")
	print(table)
	b = input("前往頁碼：")
print("頁碼超過範圍!")