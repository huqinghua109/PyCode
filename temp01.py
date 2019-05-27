from dataclasses import dataclass
import datetime as dtt
import pandas as pd
import numpy as np
import copy
import time

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
CFTC_EXCEL = "E:\\Desktop\\workstation\\database\\CFTCopi.xlsx"
CBOTFUTURES_EXCEL = "E:\\Desktop\\workstation\\database\\CBOTFuturesData.xlsx"

cftc_df = pd.read_excel(CFTC_EXCEL, sheet_name='Sheet1', skiprows=1, index_col=0)
cftc_df.columns = ["corn_opi", "corn_long", "corn_short", "wsr_opi", "wsr_long", "wsr_short", "whr_opi", "whr_long", "whr_short", "soy_opi", "soy_long", "soy_short"]
cftc_df['corn_netlong'] = cftc_df.iloc[:,1] - cftc_df.iloc[:,2]
cftc_df['corn_netlong_ratio'] = round(cftc_df['corn_netlong'] / cftc_df.iloc[:,0],2)
cftc_df['wsr_netlong'] = cftc_df.iloc[:,4] - cftc_df.iloc[:,5]
cftc_df['wsr_netlong_ratio'] = round(cftc_df['wsr_netlong'] / cftc_df.iloc[:,3],2)
cftc_df['whr_netlong'] = cftc_df.iloc[:,7] - cftc_df.iloc[:,8]
cftc_df['whr_netlong_ratio'] = round(cftc_df['whr_netlong'] / cftc_df.iloc[:,6],2)
cftc_df['soy_netlong'] = cftc_df.iloc[:,10] - cftc_df.iloc[:,11]
cftc_df['soy_netlong_ratio'] = round(cftc_df['soy_netlong'] / cftc_df.iloc[:,9],2)

cbotFuturesPrice_df = pd.read_excel(CBOTFUTURES_EXCEL, sheet_name='Sheet1', skiprows=0, index_col=0)
# print(cbotFuturesPrice_df)
cftc_df = pd.merge(cftc_df, cbotFuturesPrice_df, how="left", on="date")
cftc_data_df = cftc_df[['corn_opi', 'corn_netlong_ratio', 'corn_netlong', 'cornprice', 'wsr_opi', 'wsr_netlong_ratio', 'wsr_netlong', 'wsrprice', 'whr_opi', 'whr_netlong_ratio', 'whr_netlong', 'soy_opi', 'soy_netlong_ratio', 'soy_netlong', 'soyprice']]
print(cftc_data_df)
# jinzhou_df = pd.read_excel(CORNPRICE_EXCEL, sheet_name='prices', skiprows=1, index_col=0).iloc[:,0]
# # print(type(jinzhou_df))
# def price_year_process(df):
# 	df = df.to_frame()
# 	minyear = df.index[0].year
# 	maxyear = df.index[-1].year
# 	df['date'] = df.index
# 	df['monday'] = df['date'].apply(lambda x: x.strftime("%m-%d"))
# 	# print(df)
# 	year_df = pd.DataFrame(index=pd.date_range("20001001","20010930"))
# 	year_df["date"] = year_df.index
# 	year_df["monday"] = year_df['date'].apply(lambda x: x.strftime("%m-%d"))

# 	for year in range(minyear, maxyear+1):
# 		thisyear_df = df[(df.index>dtt.datetime(year-1,9,30))&(df.index<dtt.datetime(year,10,1))]
# 		thisyear_df.columns = ["%s/%s"%(year-1, year), "date" , "monday"]
# 		year_df = pd.merge(year_df, thisyear_df.iloc[:,[0,2]], how="left", on="monday")
# 	return year_df

# price_year_process(jinzhou_df)
# print(jinzhou_df.index)
# import_df = pd.read_excel(IMPORTANDEXPORT_EXCEL, sheet_name='Sheet1', skiprows=1, index_col=0)
# import_df = import_df.sort_index()

# if import_df.index[0].month < 11:
# 	startyear = import_df.index[0].year
# else:
# 	startyear = import_df.index[0].year + 1
# if import_df.index[-1].month < 10:
# 	endyear = import_df.index[-1].year
# else:
# 	endyear = import_df.index[-1].year + 1

# df = pd.DataFrame()
# for year in range(startyear,endyear):
# 	cumsum_df = import_df[(import_df.index<dtt.datetime(year+1,10,1)) & (import_df.index>dtt.datetime(year,9,30))].iloc[:,[0,4,8,12]].cumsum()
# 	cumsum_df.columns = ["%scorn"%year, "%sbarley"%year, "%ssorghum"%year, "%scassava"%year]
# 	cumsum_df.index = ["10月", "11月", "12月", "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月"][:cumsum_df.shape[0]]
# 	df = pd.concat([df,cumsum_df],axis=1)
# print(df)
# 		pass
# ffi_df = pd.read_excel(ANALYSIS_EXCEL, sheet_name='feedfactoryinventory', header=None)
# chanqu_df = pd.read_excel(ANALYSIS_EXCEL, sheet_name='chanqu', header=None)
# summarize_df = pd.read_excel(ANALYSIS_EXCEL, sheet_name='summarize', header=None)
# visual_df = ffi_df.append([chanqu_df,summarize_df])
# print(visual_df)
# dt1 = dtt.datetime(2017,1,1)
# dt2 = dtt.datetime.now()
# print(dt1<dt2)
# df1 = pd.DataFrame([[1,2,3],[1,2]])
# df1.columns = ['a', 'b', 'c']
# print(type(df1['a']))
# print(type(df1[['a']]))
# salerate_df = pd.read_excel(SALERATE_EXCEL, sheet_name='salerate', skiprows=1, index_col =0)
# salerate_avg_df = salerate_df.copy()
# salerate_avg_df["hlj_avg5"] = salerate_df.iloc[:,[-15,-23,-31,-39,-47]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["jl_avg5"] = salerate_df.iloc[:,[-14,-22,-30,-38,-46]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["ln_avg5"] = salerate_df.iloc[:,[-13,-21,-29,-37,-45]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["nm_avg5"] = salerate_df.iloc[:,[-12,-20,-28,-36,-44]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["hb_avg5"] = salerate_df.iloc[:,[-11,-19,-27,-35,-43]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["sd_avg5"] = salerate_df.iloc[:,[-10,-18,-26,-34,-42]].apply(lambda x: x.mean(), axis=1)
# salerate_avg_df["hn_avg5"] = salerate_df.iloc[:,[-9,-17,-25,-33,-41]].apply(lambda x: x.mean(), axis=1)
# print(salerate_avg_df.iloc[:,-7:])
# print(salerate_df.iloc[:,-7:])
# pigPrice_df = pd.read_excel(PIGPRICE_EXCEL, sheet_name='PigPrice')
# print(pigPrice_df.shape)
# cornPrice_df = pd.read_excel(CORNPRICE_EXCEL, sheet_name='prices', skiprows=0, index_col =0)
# print(cornPrice_df.shape)
# pigPrice_df = pd.merge(pigPrice_df, cornPrice_df[["guangdong"]], how="left", on="date")
# print(pigPrice_df.shape)
# price_df = pd.read_excel(CORNPRICE_EXCEL, sheet_name='价格', skiprows=0, index_col =0)
# futures_df = pd.read_excel(FUTURES_EXCEL, sheet_name='futures', skiprows=0, index_col =0)
# df = pd.merge(futures_df, price_df[["锦州港"]], how="left", on="日期")
# print(df)
# print(futures_df.shape)
# print(price_df.shape)
# if port_df.iloc[-1,[2,5,8,11]].isnull().sum() > 0:
# 	portclean_df = port_df[:-1]
# else:
# 	portclean_df = port_df
# northPort_df = portclean_df.iloc[:,:12]
# northPort_df.columns = ["jzgather", "jzout", "jzcarry", "byqgather", "byqout", "byqcarry", "blgather", "blout", "blcarry", "dywgather", "dywout", "dywcarry"]
# northPort_df["northGather"] = portclean_df.iloc[:,[0,3,6,9]].apply(lambda x: x.sum(), axis=1)
# northPort_df["northOut"] = portclean_df.iloc[:,[1,4,7,10]].apply(lambda x: x.sum(), axis=1)
# northPort_df["northCarryOutSum"] = portclean_df.iloc[:,[2,5,8,11]].apply(lambda x: x.sum(), axis=1)
# northPort_df["weekchange"] = northPort_df["northCarryOutSum"] - northPort_df["northCarryOutSum"].shift(1)
# print(northPort_df.index)
# if port_df.iloc[-1,[14,17]].isnull().sum() > 0:
# 	portclean_df = port_df[:-1]
# else:
# 	portclean_df = port_df
# sorthPort_df = portclean_df.iloc[:,12:18]
# sorthPort_df["sorthGather"] = portclean_df.iloc[:,[12,15]].apply(lambda x: x.sum(), axis=1)
# sorthPort_df["sorthOut"] = portclean_df.iloc[:,[13,16]].apply(lambda x: x.sum(), axis=1)
# sorthPort_df["sorthCarryOutSum"] = portclean_df.iloc[:,[14,17]].apply(lambda x: x.sum(), axis=1)
# print(sorthPort_df)
# cornData_excel_path = "E:\\Desktop\\uads\\AnalysisReport\\CornData.xlsx"
# df = pd.read_excel(cornData_excel_path, sheet_name='PigPrice')
# print(df.index[0])
# l = ['%s' % (i+1) for i in range(port_df.shape[0])]
# print(l)
# df = pd.DataFrame([[1, 2, 3.3333333, 4], [5, 6, 7, 8], [9, 10, 11, 12]], columns=['a', 'b', 'c', 'd'])
# df1 = df.cumsum(2)

# df.round(decimals=2)
# print(df)
# df.index = pd.date_range('20180101', periods=3)
# print(df.index[2])
# print(df.loc[df.index[2], :])
# df.loc[df.index[2]] = [13, 14, 15, 16]
# print(df)
# print('中文乱码？')

# def fun(df):
# 	df1 = copy.copy(df)
# 	df1.iloc[2,2] = 999
# 	print("df in func")
# 	print(df1)

# print("df 1")
# print(df)

# fun(df)

# print("df 2")
# print(df)
# print(time.localtime())
# print(time.strftime("%Y%m%d", time.localtime()))