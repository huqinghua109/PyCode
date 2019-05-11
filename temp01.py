from dataclasses import dataclass
import datetime as dtt
import pandas as pd
import numpy as np
import copy
import time


# cornData_excel_path = "E:\\Desktop\\uads\\AnalysisReport\\CornData.xlsx"
# df = pd.read_excel(cornData_excel_path, sheet_name='PigPrice')
# print(df.index[0])
# l = ['%s' % (i+1) for i in range(port_df.shape[0])]
# print(l)
# df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], columns=['a', 'b', 'c', 'd'])
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
print(time.localtime())
print(time.strftime("%Y%m%d", time.localtime()))