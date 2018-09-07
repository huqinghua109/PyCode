import pandas as pd
import datetime as dtt
import numpy as np
import matplotlib.pyplot as plt

excel_path = "E:\\Desktop\\PyCode\\data.xlsx"
basis_excel_path = "E:\\Desktop\\PyCode\\cleandata_basis.xlsx"

df = pd.read_excel(excel_path)
print(df.shape)
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

def basis_cal(clean_df):
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

def basis_year_cal(basis_df_orig, contract_month=1):
	basis_df = basis_df_orig
	basis_df['date'] = basis_df.index
	df_d = {}
	for year in range(2005,2019,1):
		d1 = dtt.datetime(year,contract_month+3,1).date()
		d2 = dtt.datetime(year+1,contract_month+3,1).date()
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
	# basis_year_df.fillna(method='ffill', inplace=True)
	return basis_year_df

#########################################################################
# raw data to basis1-5-9
# clean_df = df_clean(df)
# print(clean_df)
# basis_df = basis_cal(clean_df)
# print(basis_df)
# basis1_year_df = basis_year_cal(basis_df, contract_month=1)
# print(basis1_year_df)
# basis5_year_df = basis_year_cal(basis_df, contract_month=5)
# print(basis5_year_df)
# basis9_year_df = basis_year_cal(basis_df, contract_month=9)
# print(basis9_year_df)

# writer = pd.ExcelWriter(basis_excel_path)
# clean_df.to_excel(writer, 'cleanpricedata')
# basis_df.to_excel(writer, 'cornbasis')
# basis1_year_df.to_excel(writer, 'cornyearbasis1')
# basis5_year_df.to_excel(writer, 'cornyearbasis5')
# basis9_year_df.to_excel(writer, 'cornyearbasis9')
# writer.save()
#########################################################################
# raw data to clean data
clean_df = df_clean(df)
cs_clean_excel_path = "E:\\Desktop\\PyCode\\cs_cleandata_basis.xlsx"
writer = pd.ExcelWriter(cs_clean_excel_path)
clean_df.to_excel(writer, 'cscleanpricedata')
writer.save()
#########################################################################

















