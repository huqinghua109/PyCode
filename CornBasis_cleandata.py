import pandas as pd
import datetime as dtt
import numpy as np
import matplotlib.pyplot as plt
import copy

excel_path = "E:\\Desktop\\PyCode\\data.xlsx"
clean_excel_path = "E:\\Desktop\\PyCode\\cleandata_basis.xlsx"
clean_excel_path2 = "E:\\Desktop\\PyCode\\cleandata_basis2.xlsx"

# df = pd.read_excel(excel_path)
# print(df.shape)
# print(df.iloc[3062,6].date())
# if not pd.isnull(df.iloc[3062,0]):
# 	print(type(df.iloc[3062,0]))
# else:
# 	print('Nodata')

def df_clean(df):
	delta1 = 0
	delta2 = 0
	delta3 = 0
	dflens = len(df.ix[:,0])
	print(df.shape)
	clean_df = pd.DataFrame(np.zeros((dflens,8)))
	for i in range(dflens):
		if pd.notnull(df.iloc[i,0]):
			# print(df.iloc[i,0])
			clean_df.iloc[i,0] = df.iloc[i,0].date()
			clean_df.iloc[i,1] = df.iloc[i,1]
			try:
				while df.iloc[i,0] > df.iloc[i+delta1,2]:
					delta1 += 1
				while df.iloc[i,0] > df.iloc[i+delta2,4]:
					delta2 += 1
				while df.iloc[i,0] > df.iloc[i+delta3,6]:
					delta3 += 1
			except Exception as e:
				print(e)
				print(i+delta1)
				print(df.iloc[i,0])
				print(df.iloc[i+delta1-1,2])
			
			if df.iloc[i,0] < df.iloc[i+delta1,2]:
				clean_df.iloc[i,2] = np.NaN
				clean_df.iloc[i,3] = np.NaN
				delta1 -=1
			elif df.iloc[i,0] == df.iloc[i+delta1,2]:
				clean_df.iloc[i,2] = df.iloc[i+delta1,2].date()
				clean_df.iloc[i,3] = df.iloc[i+delta1,3]

			if df.iloc[i,0] < df.iloc[i+delta2,4]:
				clean_df.iloc[i,4] = np.NaN
				clean_df.iloc[i,5] = np.NaN
				delta2 -=1
			elif df.iloc[i,0] == df.iloc[i+delta2,4]:
				clean_df.iloc[i,4] = df.iloc[i+delta2,4].date()
				clean_df.iloc[i,5] = df.iloc[i+delta2,5]

			if df.iloc[i,0] < df.iloc[i+delta3,6]:
				print( df.iloc[i,0], df.iloc[i+delta3,6])
				clean_df.iloc[i,6] = np.NaN
				clean_df.iloc[i,7] = np.NaN
				delta3 -=1
			elif df.iloc[i,0] == df.iloc[i+delta3,6]:
				clean_df.iloc[i,6] = df.iloc[i+delta3,6].date()
				clean_df.iloc[i,7] = df.iloc[i+delta3,7]

	clean_df = clean_df[clean_df.ix[:,0]!=0]
	return clean_df
######################################################################
# corn basis process
def basis_cal(clean_df_orig):
	clean_df = copy.copy(clean_df_orig)
	clean_df.index = clean_df.ix[:,0]
	basis_df = pd.DataFrame(np.zeros((len(clean_df),3)), index=clean_df.index, columns=['basis1', 'basis5', 'basis9'])
	for i in basis_df.index:
		# print(i.month)
		# print(i.day)
		basis_df.ix[i,'monthday'] = i.strftime('%m-%d')
		if i.month <= 3:
			basis_df.ix[i,0] = np.NaN	
			if i.month == 1:
				if i.day < 10:
					basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]
				# else:
				# 	basis_df.ix[i,0] = np.NaN			
			basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]			
			basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]		
		elif i.month == 4:
			basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]			
			basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]			
			basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]
		elif i.month > 4 and i.month < 8:
			basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]	
			basis_df.ix[i,1] = np.NaN	
			if i.month == 5:
				if i.day < 10:
					basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]
				# else:		
				# 	basis_df.ix[i,1] = np.NaN			
			basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]
		elif i.month == 8:
			basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]			
			basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]			
			basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]
		elif i.month > 8 and i.month < 12:
			basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]			
			basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]	
			basis_df.ix[i,2] = np.NaN
			if i.month == 9:
				if i.day < 10:
					basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]
				# else:		
				# 	basis_df.ix[i,2] = np.NaN
		elif i.month == 12:
			basis_df.ix[i,0] = clean_df.ix[i,1] - clean_df.ix[i,3]			
			basis_df.ix[i,1] = clean_df.ix[i,1] - clean_df.ix[i,5]			
			basis_df.ix[i,2] = clean_df.ix[i,1] - clean_df.ix[i,7]		
	return basis_df
######################################################################
# corn year basis process
def basis_year_cal(basis_df_orig, contract_month=1):
	basis_df = copy.copy(basis_df_orig)
	basis_df['date'] = basis_df.index
	print(basis_df.ix[0,'date'].date())
	print(type(basis_df.ix[0,'date'].date()))
	df_d = {}
	for year in range(2005,2019,1):
		d1 = dtt.datetime(year,contract_month+3,1)
		d2 = dtt.datetime(year+1,contract_month+3,1)
		df_d['%s'%year] = basis_df[(basis_df['date']>=d1) & (basis_df['date']<d2)]

	startday = dtt.datetime(2000,contract_month+3,1)
	endday = dtt.datetime(2001,contract_month+3,1)
	oneday = dtt.timedelta(days=1)
	columns = ['%sbasis%s'% (i, contract_month) for i in range(2006,2020)]
	rows = pd.date_range(startday, endday-oneday)
	basis_year_df = pd.DataFrame(np.zeros([len(rows),len(columns)]), index=rows, columns=columns)

	d = startday
	while d<endday:
		dstr = d.strftime('%m-%d')
		l = []
		for key,value in df_d.items():
			if dstr in list(value['monthday']):
				basis = value[value['monthday']==dstr].ix[0,'basis%s'%contract_month]
				if pd.isnull(basis):
					basis = np.NaN
			else:
				basis = np.NaN
			l.append(basis)
		if l.count(np.NaN)<len(columns):
			basis_year_df.loc[d,:] = l	
		else:
			basis_year_df.drop(labels=[d], axis=0, inplace=True)
		d += oneday
	basis_year_df.fillna(method='ffill', limit=2, inplace=True)
	return basis_year_df
######################################################################
# corn month spread process
def month_spread_cal(clean_df_orig, recent=9, far=1, contract='corn'):
	clean_df = copy.copy(clean_df_orig)
	clean_df['date'] = clean_df.index
	for i in clean_df.index:
		clean_df.ix[i,'monthday'] = i.strftime('%m-%d')
	minyear = clean_df.ix[0,'date'].year
	maxyear = clean_df.ix[-1,'date'].year
	if contract=='corn':
		a = 0
	elif contract =='cs':
		a = 6
	# spread fenpian
	df_d = {}
	for year in range(minyear,maxyear+1,1):
		if recent==9 and far==1:
			d1 = dtt.datetime(year,far+1,1)
			d2 = dtt.datetime(year,recent,1)
			spread_df = clean_df.iloc[:,a+7]-clean_df.iloc[:,a+3]
		elif recent==1 and far==5:
			d1 = dtt.datetime(year,far+1,1)
			d2 = dtt.datetime(year+1,recent,1)
			spread_df = clean_df.iloc[:,a+3]-clean_df.iloc[:,a+5]
		elif recent==5 and far==9:
			d1 = dtt.datetime(year,far+1,1)
			d2 = dtt.datetime(year+1,recent,1)
			spread_df = clean_df.iloc[:,a+5]-clean_df.iloc[:,a+7]
		spread_df = spread_df.to_frame()
		spread_df['date'] = clean_df.index
		spread_df['monthday'] = clean_df['monthday']
		df_d['%s'%year] = spread_df[(spread_df['date']>=d1) & (spread_df['date']<d2)]

	# spread year cal
	if recent==9 and far==1:
		startday = dtt.datetime(2000,far+1,1)
		endday = dtt.datetime(2000,recent,1)
		columns = ['%s%s_%s'% (i, recent, far) for i in range(minyear,maxyear+1)]
	elif recent==1 and far==5:
		startday = dtt.datetime(2000,far+1,1)
		endday = dtt.datetime(2001,recent,1)
		columns = ['%s%s_%s'% (i, recent, far) for i in range(minyear+1,maxyear+2)]
	elif recent==5 and far==9:
		startday = dtt.datetime(2000,far+1,1)
		endday = dtt.datetime(2001,recent,1)
		columns = ['%s%s_%s'% (i, recent, far) for i in range(minyear+1,maxyear+2)]
	# startday = dtt.datetime(2000,d1.month,1)
	# endday = dtt.datetime(2001,d2.month,10)
	oneday = dtt.timedelta(days=1)
	rows = pd.date_range(startday, endday-oneday)
	spread_year_df = pd.DataFrame(np.zeros([len(rows),len(columns)]), index=rows, columns=columns)

	d = startday
	while d<endday:
		dstr = d.strftime('%m-%d')
		l = []
		for key,value in df_d.items():
			if dstr in list(value['monthday']):
				spread = value[value['monthday']==dstr].ix[0,0]
				if pd.isnull(spread):
					spread = np.NaN
			else:
				spread = np.NaN
			l.append(spread)
		if l.count(np.NaN)<len(columns):
			spread_year_df.loc[d,:] = l	
		else:
			spread_year_df.drop(labels=[d], axis=0, inplace=True)
		d += oneday
	spread_year_df.fillna(method='ffill', limit=2, inplace=True)

	return spread_year_df
######################################################################
# cs month spread process
# def cs_month_spread_cal(clean_df_orig):
# 	clean_df = copy.copy(clean_df_orig)
######################################################################
# corn cs spread process
def corn_cs_spread_cal(clean_df_orig):
	clean_df = copy.copy(clean_df_orig)
	corn_cs_spread_df = pd.DataFrame(np.zeros((len(clean_df),4)), index=clean_df.index, columns=['corncs1', 'corncs5', 'corncs9', 'monthday'])
	for i in corn_cs_spread_df.index:
		corn_cs_spread_df.ix[i,'monthday'] = i.strftime('%m-%d')
		if pd.notnull(clean_df.ix[i,3]) and pd.notnull(clean_df.ix[i,9]):
			corn_cs_spread_df.ix[i,0] = clean_df.ix[i,3] - clean_df.ix[i,9]	
		else:
			corn_cs_spread_df.ix[i,0] = np.NaN

		if pd.notnull(clean_df.ix[i,5]) and pd.notnull(clean_df.ix[i,11]):		
			corn_cs_spread_df.ix[i,1] = clean_df.ix[i,5] - clean_df.ix[i,11]
		else:
			corn_cs_spread_df.ix[i,1] = np.NaN

		if pd.notnull(clean_df.ix[i,7]) and pd.notnull(clean_df.ix[i,13]):					
			corn_cs_spread_df.ix[i,2] = clean_df.ix[i,7] - clean_df.ix[i,13]
		else:
			corn_cs_spread_df.ix[i,2] = np.NaN

		if pd.isnull(corn_cs_spread_df.ix[i,0]) and pd.isnull(corn_cs_spread_df.ix[i,1]) and pd.isnull(corn_cs_spread_df.ix[i,2]):
			corn_cs_spread_df.drop(labels=[i], axis=0, inplace=True)

	return corn_cs_spread_df

def corn_cs_spread_year_cal(corn_cs_spread_orig, contract_month=1):
	corn_cs_spread_df = copy.copy(corn_cs_spread_orig)
	corn_cs_spread_df['date'] = corn_cs_spread_df.index
	print(corn_cs_spread_df.ix[0,'date'])
	print(type(corn_cs_spread_df.ix[0,'date']))
	print(corn_cs_spread_df.ix[0,'date'].year)
	minyear = corn_cs_spread_df.ix[0,'date'].year
	maxyear = corn_cs_spread_df.ix[-1,'date'].year

	df_d = {}
	for year in range(minyear,maxyear+1,1):
		d1 = dtt.datetime(year,contract_month+1,1)
		d2 = dtt.datetime(year+1,contract_month,10)
		df_d['%s'%year] = corn_cs_spread_df[(corn_cs_spread_df['date']>=d1) & (corn_cs_spread_df['date']<d2)]

	startday = dtt.datetime(2000,contract_month+1,1)
	endday = dtt.datetime(2001,contract_month,10)
	oneday = dtt.timedelta(days=1)
	columns = ['%sc-cs%s'% (i, contract_month) for i in range(minyear+1,maxyear+2)]
	rows = pd.date_range(startday, endday-oneday)
	corn_cs_spread_year_df = pd.DataFrame(np.zeros([len(rows),len(columns)]), index=rows, columns=columns)

	d = startday
	while d<endday:
		dstr = d.strftime('%m-%d')
		l = []
		for key,value in df_d.items():
			if dstr in list(value['monthday']):
				basis = value[value['monthday']==dstr].ix[0,'corncs%s'%contract_month]
				if pd.isnull(basis):
					basis = np.NaN
			else:
				basis = np.NaN
			l.append(basis)
		if l.count(np.NaN)<len(columns):
			corn_cs_spread_year_df.loc[d,:] = l	
		else:
			corn_cs_spread_year_df.drop(labels=[d], axis=0, inplace=True)
		d += oneday
	corn_cs_spread_year_df.fillna(method='ffill', limit=2, inplace=True)
	return corn_cs_spread_year_df



clean_df = pd.read_excel(clean_excel_path, sheet_name='cleanpricedata')
print(clean_df)
basis_df = basis_cal(clean_df)
# print(basis_df)
basis1_year_df = basis_year_cal(basis_df, contract_month=1)
# print(basis1_year_df)
basis5_year_df = basis_year_cal(basis_df, contract_month=5)
# print(basis5_year_df)
basis9_year_df = basis_year_cal(basis_df, contract_month=9)
# print(basis9_year_df)
corn_cs_spread_df = corn_cs_spread_cal(clean_df)
# print(corn_cs_spread_df)
corn_cs_spread1_year = corn_cs_spread_year_cal(corn_cs_spread_df, contract_month=1)
# print(corn_cs_spread1_year)
corn_cs_spread5_year = corn_cs_spread_year_cal(corn_cs_spread_df, contract_month=5)
# print(corn_cs_spread5_year)
corn_cs_spread9_year = corn_cs_spread_year_cal(corn_cs_spread_df, contract_month=9)
# print(corn_cs_spread9_year)
c9_1_spread_year_df = month_spread_cal(clean_df, recent=9, far=1, contract='corn')
c1_5_spread_year_df = month_spread_cal(clean_df, recent=1, far=5, contract='corn')
c5_9_spread_year_df = month_spread_cal(clean_df, recent=5, far=9, contract='corn')
# print(c5_9_spread_year_df)


writer = pd.ExcelWriter(clean_excel_path2)
clean_df.to_excel(writer, 'cleanpricedata')
# corn basis
basis_df.to_excel(writer, 'cornbasis')
basis1_year_df.to_excel(writer, 'cornyearbasis1')
basis5_year_df.to_excel(writer, 'cornyearbasis5')
basis9_year_df.to_excel(writer, 'cornyearbasis9')
# corn cs spread
corn_cs_spread_df.to_excel(writer, 'corncsspread')
corn_cs_spread1_year.to_excel(writer, 'corncsspread1year')
corn_cs_spread5_year.to_excel(writer, 'corncsspread5year')
corn_cs_spread9_year.to_excel(writer, 'corncsspread9year')
# corn month spread
c9_1_spread_year_df.to_excel(writer, 'c9_1_year')
c1_5_spread_year_df.to_excel(writer, 'c1_5_year')
c5_9_spread_year_df.to_excel(writer, 'c5_9_year')

writer.save()

















