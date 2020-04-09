import json

from DataApi import DataApi

config = open('quantos_config.json')
setting = json.load(config)
symbols = setting['SYMBOLS']

api = DataApi()
r,msg = api.login(setting['USERNAME'], setting['TOKEN'])
print(r)
print(msg)

def downloadSymbolDaily(symbol):
	data, errormsg = api.daily(symbol, start_date=20170503, end_date=20170708, fields="open,high,low,last,volume,turnover", adjust_mode = "post")
	return data, msg

def downloadAllSymbolsDaily():
	for symbol in symbols:
		pass
def temp01():
	data, msg = downloadSymbolDaily('c1901')
	print(msg)
	print(data)

temp01()