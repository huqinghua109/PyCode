import pandas as pd
import numpy as np
import datetime as dtt

EXCEL_PATH = "E:\\Desktop\\PyCode\\CornBasisChart1.xlsx"

df = pd.read_excel(EXCEL_PATH,sheet_name='say')
print(df)