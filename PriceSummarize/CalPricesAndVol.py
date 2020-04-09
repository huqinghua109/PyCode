import os,sys

import pandas as pd
import xlrd

path = os.path.join(os.getcwd(), 'files')
new_excel_path = os.path.join(os.getcwd(), 'saleInfo.xlsx')

def getData(path):
	df_dict = {}
	for dirpath, dirnames, filenames in os.walk(path):
		for file in filenames:
			excel_path = os.path.join(dirpath, file)
			df = pd.read_excel(excel_path)
			df.columns = df.iloc[2,:]
			company = df.iloc[0,0].split('：')[1]
			df = df.iloc[3:-1,1:]
			df.dropna(inplace=True)
			if company in df_dict:
				df_dict[company] = pd.concat([df_dict[company], df], axis=0, sort=False)
			else:
				df_dict[company] = df
	return df_dict

def getSummarize(df_dict):
	summarize_df = pd.DataFrame(columns = ['潮粮数量', '结算金额', '折干量', '折干价'])
	for key,value in df_dict.items():
		if '天跃' in key:
			ratio = 1.25
		elif '稷丰' in key or '亿鼎' in key:
			ratio = 1.3
		else:
			ratio = 1.3
		wet_vol = 0
		dry_vol = 0
		sum_money = 0
		for i in range(value.shape[0]):
			wet_vol = wet_vol + value.iloc[i,8]
			sum_money = sum_money + value.iloc[i,9]
			dry_vol = dry_vol + value.iloc[i,8]*(1-(value.iloc[i,5]/100-0.145)*ratio)
		dry_price = sum_money/dry_vol

		summarize_df.loc[key,:] = [wet_vol, sum_money, dry_vol, dry_price]
	return summarize_df

df_dict = getData(path)
summarize_df = getSummarize(df_dict)

writer = pd.ExcelWriter(new_excel_path)
for key,value in df_dict.items():
	value.to_excel(writer, key)
summarize_df.to_excel(writer, 'summarize')

writer.save()