from dataclasses import dataclass
import datetime as dtt
import pandas as pd
import numpy as np
import copy
import time
import random

CORNPRICE_EXCEL = "E:\\Desktop\\workstation\\database\\CornPice.xlsx"
FUTURES_EXCEL = "E:\\Desktop\\workstation\\database\\FuturesData.xlsx"
PIGPRICE_EXCEL = "E:\\Desktop\\workstation\\database\\PigData.xlsx"
SALERATE_EXCEL = "E:\\Desktop\\workstation\\database\\CornSalerate.xlsx"
NORTHPORT_EXCEL = "E:\\Desktop\\workstation\\database\\NorthPort.xlsx"
SORTHPORT_EXCEL = "E:\\Desktop\\workstation\\database\\SorthPort.xlsx"
DEEPPROCESSING_EXCEL = "E:\\Desktop\\workstation\\database\\DeepProcessOprationAndProfit.xlsx"
WEBDATA_EXCEL = "E:\\Desktop\\PyCode\\webdata.xlsx"
FACTORY_EXCEL = "E:\\Desktop\\workstation\\database\\FactoryInventories.xlsx"
ANALYSIS_EXCEL = "E:\\Desktop\\workstation\\Analysis.xlsx"
IMPORTANDEXPORT_EXCEL = "E:\\Desktop\\workstation\\database\\ImportAndExport.xlsx"


# df = pd.DataFrame(np.random.randint(1,5,[10,1]), index=pd.date_range("20170101","20170110"))
# print(df[df.index<dtt.datetime(2017,1,5)])
# import_df = pd.read_excel(IMPORTANDEXPORT_EXCEL, sheet_name='Sheet1', skiprows=1, index_col=0)
# import_df = import_df.sort_index()
# cumsum_df = import_df[(import_df.index<dtt.datetime(2015,10,1)) & (import_df.index>dtt.datetime(2014,9,30))].iloc[:,[0,4,8]].cumsum()
# print(cumsum_df)
now = dtt.datetime.now()
print(now)
print(now.strftime("%m-%d"))