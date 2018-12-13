import datetime as dtt
import pandas as pd
import numpy as np
import copy


cornData_excel_path = "E:\\Desktop\\uads\\AnalysisReport\\CornData.xlsx"
# port_df = pd.read_excel(cornData_excel_path, sheet_name='NSPort')
# l = ['%s' % (i+1) for i in range(port_df.shape[0])]
# print(l)
df = pd.DataFrame([[1,2,3,4], [5,6,7,8], [9,10,11,12]],columns=['a', 'b', 'c', 'd'])
df.index = pd.date_range('20180101', periods=3)
df[df.index[3]] = [13,14,15,16]
print(df)
