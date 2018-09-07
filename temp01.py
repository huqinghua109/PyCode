import datetime as dtt
import pandas as pd
import numpy as np


excel_path = "E:\\Desktop\\PyCode\\cleandata_basis.xlsx"
df = pd.read_excel(excel_path,sheet_name='cleanpricedata')
print(df.iloc[:,7])