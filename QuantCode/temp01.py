from jqdatasdk import *

auth('15542377707', 'huqinghua129')
# futures = get_all_securities('futures')
# print(futures)
bars = get_bars('C1901.XDCE', fields=['date', 'open', 'high', 'low', 'close', 'volume'], unit='1d', count=10, end_dt='2018-12-11')
print(bars)