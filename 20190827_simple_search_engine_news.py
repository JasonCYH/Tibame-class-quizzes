import requests
from bs4 import BeautifulSoup
import pymysql as pmsql
import jieba
import jieba.analyse
import os
import prettytable
cnct = pmsql.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	db = "2019-08-27",
	charset = "utf8"
)

cmnd = cnct.cursor()
# aaaa = cmnd.execute("SELECT `member`.`id`, `name`, `birthday`, `address`, `tel` FROM `member` LEFT JOIN `tel` ON `member`.`id` = `tel`.`member_id`")
# bbbb = cmnd.fetchall()
# p = requests.get("https://udn.com/news/breaknews/1")
# p.encoding = "utf-8"
# x = BeautifulSoup(p.text, "html.parser")
# a1 = x.find("div", {"id": "breaknews_body"})
# a2 = a1.find("dl").find_all("dt")
# for a3 in a2:
# 	a4 = a3.find("h2")
# 	if a4 != None:
# 		r = requests.get("https://udn.com"+a4.find("a").attrs["href"])
# 		r.enconding = "utf-8"
# 		e = BeautifulSoup(r.text, "html.parser")
# 		b1 = e.find("div", {"id": "story_body_content"})
# 		txt = ""
# 		for dd in b1.find_all("p"):
# 			txt += dd.text
# 		cmnd.execute("INSERT INTO `udn_news`(`url`, `title`, `content`) VALUES(%s, %s, %s)", (a4.find("a").attrs["href"], a4.find("a").text, txt))
# 		cnct.commit()
# 		new_id = cmnd.lastrowid
# 		k = jieba.analyse.extract_tags(txt)
# 		for kk in k:
# 			cmnd.execute("INSERT INTO `udn_keyword`(`news_id`,`keyword`) VALUES(%s, %s)",(new_id, kk))	
# 			cnct.commit()
# for page in range(2,11):
# 	q = requests.get("https://udn.com/news/get_breaks_article/"+str(page)+"/1/0?_=1566888391480")
# 	q.encoding = "utf-8"
# 	xpage = BeautifulSoup(q.text,"html.parser")
# 	dt = xpage.find_all("dt", class_ = "lazyload")
# 	for ddt in dt:
# 		xxx=ddt.find("h2")
# 		if xxx!=None and xxx!=-1:
# 			title = xxx.find("a").text
# 			url = xxx.find("a").attrs["href"]
# 			get_news = requests.get("https://udn.com"+url) 
# 			get_news.encoding = "utf-8"
# 			news_soup = BeautifulSoup(get_news.text, "html.parser")
# 			content = news_soup.find("div", id = "story_body_content").find_all("p")
# 			txt2 = ""
# 			for con_num in range(0,len(content)):
# 				con_all = content[con_num].text
# 				txt2 += con_all
# 			cmnd.execute("INSERT INTO `udn_news`(`url`, `title`, `content`) VALUES(%s, %s, %s)", (url ,title ,txt2))
# 			cnct.commit()
# 			news_id = cmnd.lastrowid
# 			m = jieba.analyse.extract_tags(txt2)
# 			for mm in m:
# 				cmnd.execute("INSERT INTO `udn_keyword`(`news_id`,`keyword`) VALUES(%s, %s)",(news_id, mm))	
# 				cnct.commit()

srch_key = input("請輸入關鍵字：")
os.system("cls")
cmnd.execute("SELECT `title`, `url` FROM `udn_news` LEFT JOIN `udn_keyword` ON `udn_news`.`id` = `udn_keyword`.`news_id` WHERE `keyword` = %s", srch_key)
table = prettytable.PrettyTable(["新聞標題", "網址"], encoding = "utf-8")
for x in cmnd.fetchall()[:]:
	table.add_row([x[0], "https://udn.com"+ x[1]])
print(table)
cnct.close()