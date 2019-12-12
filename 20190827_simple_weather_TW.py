import prettytable
import requests
from bs4 import BeautifulSoup
table = prettytable.PrettyTable(["地區", "氣溫"], encoding = "utf-8")
gethtml = requests.get("https://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1566875848583")
gethtml.encoding = "utf-8"
soup = BeautifulSoup(gethtml.text, "html.parser")
city = soup.find_all("td", width="60%")
temp = soup.find_all("td", width="50%")
for a in range(0,len(city)):
	table.add_row([city[a].text, temp[a].text])
	table.align["地區"] = "l"
	table.align["氣溫"] = "l"
print(table)