from bs4 import BeautifulSoup
import urllib.request

url = "http://www.nmc.cn/publish/agro/disastersmonitoring/Agricultural_Drought_Monitoring.htm"
preurl = "http://www.nmc.cn/publish/precipitation/1-day.html"
response = urllib.request.urlopen(preurl)
soup = BeautifulSoup(response, "html.parser")

# res = soup.find('ul', id='mycarousel').get("data-original")
res = soup.find('ul', id='mycarousel')
# res = soup.find_all('li')
# select = soup.select("#mycarousel")
# print(len(res.find_all('img')))
print(res.find_all('img')[4].get("data-original"))