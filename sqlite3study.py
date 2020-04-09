import sqlite3
import datetime as dtt
from time import sleep
from peewee import (
    AutoField,
    CharField,
    Database,
    DateTimeField,
    FloatField,
    Model,
    MySQLDatabase,
    PostgresqlDatabase,
    SqliteDatabase,
    chunked,
)


path = "E:\\Desktop\\PyCode\\test.db"
db = SqliteDatabase(path)
# print(db)

class BaseModel(Model):
	"""docstring for BaseModel"""
	id = AutoField()
	symbol: str = CharField()
	exchange: str = FloatField()
	datetime: datetime = DateTimeField()

	class Meta:
		database = db
		table_name = "ohlc"


def createTable():
	BaseModel.create_table()


def insertData():
	for i in range(10):
		ohlc1 = BaseModel()
		ohlc1.symbol = i
		ohlc1.exchange = 'DCE'
		ohlc1.datetime = i
		ohlc1.save()

def fetchdata():
	# ohlc = BaseModel.select()
	# print(ohlc)
	# for i in ohlc:
	# 	print(i)
	# print(ohlc.symbol, ohlc.datetime)
	for i in BaseModel.select():
		print(i.datetime)

def fetchInfo():
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	sqlite = "SELECT name FROM sqlite_master WHERE type=='table'"
	sqlite1 = "SELECT * FROM ohlc"

	cursor.execute(sqlite1)
	values = cursor.fetchall()
	print(values)

def main():
	# dtt1 = dtt.datetime.now()
	# createTable()
	insertData()
	# fetchdata()
	# fetchInfo()
	# sleep(360)

	# dtt2 = dtt.datetime.now()
	# print(dtt1)
	# print(dtt2)
	# print(dtt2-dtt1)

main()