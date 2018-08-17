import pandas as pd
import datetime as dtt
import numpy as np
import matplotlib.pyplot as plt

excel_path = "E:\Desktop\物通农业\玉米基差.xlsx"
basis_excel_path = "E:\Desktop\物通农业\CornBasisChart1.xlsx"

df = pd.read_excel(excel_path, sheet_name="cleandata")
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
	new_df = pd.DataFrame(np.zeros((dflens,8)))
	for i in range(dflens):
		if pd.notnull(df.iloc[i,0]):
			# print(df.iloc[i,0])
			new_df.iloc[i,0] = df.iloc[i,0].date()
			new_df.iloc[i,1] = df.iloc[i,1]
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
				new_df.iloc[i,2] = 'NaN'
				new_df.iloc[i,3] = 'NaN'
				delta1 -=1
			elif df.iloc[i,0] == df.iloc[i+delta1,2]:
				new_df.iloc[i,2] = df.iloc[i+delta1,2].date()
				new_df.iloc[i,3] = df.iloc[i+delta1,3]

			if df.iloc[i,0] < df.iloc[i+delta2,4]:
				new_df.iloc[i,4] = 'NaN'
				new_df.iloc[i,5] = 'NaN'
				delta2 -=1
			elif df.iloc[i,0] == df.iloc[i+delta2,4]:
				new_df.iloc[i,4] = df.iloc[i+delta2,4].date()
				new_df.iloc[i,5] = df.iloc[i+delta2,5]

			if df.iloc[i,0] < df.iloc[i+delta3,6]:
				print( df.iloc[i,0], df.iloc[i+delta3,6])
				new_df.iloc[i,6] = 'NaN'
				new_df.iloc[i,7] = 'NaN'
				delta3 -=1
			elif df.iloc[i,0] == df.iloc[i+delta3,6]:
				new_df.iloc[i,6] = df.iloc[i+delta3,6].date()
				new_df.iloc[i,7] = df.iloc[i+delta3,7]

	new_df = new_df[new_df.ix[:,0]!=0]
	return new_df

def basis_cal(df):
	df.index = df.ix[:,0]
	basis_df = pd.DataFrame(np.zeros((len(df),3)), index=df.index, columns=['basis1', 'basis5', 'basis9'])
	for i in basis_df.index:
		# print(i.month)
		# print(i.day)
		basis_df.ix[i,'monthday'] = i.strftime('%m-%d')
		if i.month <= 3:
			basis_df.ix[i,0] = ''	
			if i.month == 1:
				if i.day < 10:
					basis_df.ix[i,0] = df.ix[i,1] - df.ix[i,3]
				else:
					basis_df.ix[i,0] = ''			
			basis_df.ix[i,1] = df.ix[i,1] - df.ix[i,5]			
			basis_df.ix[i,2] = df.ix[i,1] - df.ix[i,7]		
		elif i.month == 4:
			basis_df.ix[i,0] = df.ix[i,1] - df.ix[i,3]			
			basis_df.ix[i,1] = df.ix[i,1] - df.ix[i,5]			
			basis_df.ix[i,2] = df.ix[i,1] - df.ix[i,7]
		elif i.month > 4 and i.month < 8:
			basis_df.ix[i,0] = df.ix[i,1] - df.ix[i,3]	
			basis_df.ix[i,1] = ''	
			if i.month == 5:
				if i.day < 10:
					basis_df.ix[i,1] = df.ix[i,1] - df.ix[i,5]
				else:		
					basis_df.ix[i,1] = ''			
			basis_df.ix[i,2] = df.ix[i,1] - df.ix[i,7]
		elif i.month == 8:
			basis_df.ix[i,0] = df.ix[i,1] - df.ix[i,3]			
			basis_df.ix[i,1] = df.ix[i,1] - df.ix[i,5]			
			basis_df.ix[i,2] = df.ix[i,1] - df.ix[i,7]
		elif i.month > 8:
			basis_df.ix[i,0] = df.ix[i,1] - df.ix[i,3]			
			basis_df.ix[i,1] = df.ix[i,1] - df.ix[i,5]	
			basis_df.ix[i,2] = ''
			if i.month == 9:
				if i.day < 10:
					basis_df.ix[i,2] = df.ix[i,1] - df.ix[i,7]
				else:		
					basis_df.ix[i,2] = ''

	return basis_df

def basis_year_cal(basis_df):
	baDict = {}
	for i in range(2005,2019,1):
		yti = dtt.datetime.now().replace(year=i,month=12,day=31)
		yti_1 = dtt.datetime.now().replace(year=i-1,month=12,day=31)
		df = basis_df[(basis_df.index<=yti) & (basis_df.index>yti_1)]
		df.index = df.ix[:,'monthday']
		df.columns = ['%sbasis1'% i, '%sbasis5'%i, '%sbasis9'%i, 'monthday%s'%i]
		# print(df)s
		baDict[str(i)] = df
	df_l = [baDict[str(i)] for i in range(2005,2019,1)]
	basis_year_df = pd.concat(df_l, axis=1, sort=True)

	return basis_year_df


# new_df = df_clean(df)
basis_df = basis_cal(df)
print(basis_df.tail())
basis_year_df = basis_year_cal(basis_df)
writer = pd.ExcelWriter(basis_excel_path)
basis_df.to_excel(writer, 'cornbasis')
basis_year_df.to_excel(writer, 'cornyearbasis')
writer.save()

















