import json
import re
import requests
import hashlib
import time
import urllib
from bs4 import BeautifulSoup
from pymongo import MongoClient, ASCENDING

config = open('global_setting.json')
setting = json.load(config)
url = 'http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html'

# respose = requests.get(url)
# for k,v in respose.__dict__.items():
# 	print(k,v)
# print(respose.__dict__.keys())
# print('*'*40)
# print('status_code: ' % respose.status_code)
# print('headers: ' % respose.headers)
# print('raw: ' % respose.raw)
# print('url: ' % respose.url)
# print('encoding: ' % respose.encoding)
# print('history: ' % respose.history)
# print('reason: ' % respose.reason)
# print('cookies: ' % respose.cookies)
# print('elapsed: ' % respose.elapsed)
# print('request: ' % respose.request)
# print('connection: ' % respose.connection)
respose = urllib.request.urlopen(url)
page = respose.read()
fp = open('temp.html', 'w+b')
fp.write(page)
fp.close()

soup = BeautifulSoup(page, 'lxml')
# l1 = soup.find_all('a')
# for item in l1:
# 	url = item.get('href')
# 	print('%s:%s' % (item.string, url))
print(soup)