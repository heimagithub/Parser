import pandas as pd

from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime 

import time

df = pd.read_csv('/home/heima/Parser/test.csv')#, names = ['time', 'close', 'high', 'low', 'volumn'])
# print(df)
# print(type(df))
# [80 rows x 7 columns]
# <class 'pandas.core.frame.DataFrame'>

# print(df.close[1])

# print(len(df))

ohlc = []
ti = []
vo = []

for i in range(len(df)):
	append_me = float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))), float(df.open[i]), float(df.high[i]), float(df.low[i]), float(df.close[i]), float(df.volumn[i])
	ohlc.append(append_me)

	ti.append(float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))))
	vo.append(float(df.volumn[i]))

	print(str(float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))))+' | '+str(df.volumn[i]))


fig, (ax1, ax2) = plt.subplots(2, sharex = True, figsize = (15,8))

candlestick_ohlc(ax1, ohlc, width = 10, colorup = 'r', colordown = 'g')
ax1.set_title('Stark')
ax1.grid(True)
# ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.bar(ti, vo)
plt.bar(ti, vo, width = 10)
ax2.set_ylabel('Volumn')
plt.show()

# plt.bar(ti, vo, width = 10)
# plt.grid(True)
# plt.show()



