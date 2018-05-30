import requests
import json

from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

import numpy as np 
from datetime import datetime 

import time

res = requests.get('https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=m&mkt=10&sym=2330')

res = res.text.split('null(')
res = res[1].split(');')
data = json.loads(res[0])


x = 0
y = len(data['ta'])
ohlc = []
ti = []
vo = []


while x < y:
	append_me = float(mdates.date2num(datetime.strptime(str(data['ta'][x]['t']), '%Y%m%d'))), float(data['ta'][x]['o']), float(data['ta'][x]['h']), float(data['ta'][x]['l']), float(data['ta'][x]['c']), float(data['ta'][x]['v'])
	ohlc.append(append_me)
	vo.append(float(data['ta'][x]['v']))
	ti.append(mdates.date2num(datetime.strptime(str(data['ta'][x]['t']), '%Y%m%d')))

	print(str(x)+' | '+str(mdates.date2num(datetime.strptime(str(data['ta'][x]['t']), '%Y%m%d')))+' | '+str(data['ta'][x]['v']))
	x += 1 


fig, (ax1, ax2) = plt.subplots(2, sharex = True, figsize = (15,8))
candlestick_ohlc(ax1, ohlc, width = 1, colorup = 'r', colordown = 'g')
ax1.set_title('Stark')
ax1.grid(True)
# ax1.xaxis_date()
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.bar(ti, vo)
ax2.set_ylabel('Volume')
plt.show()


fig2 = plt.figure()
plt.bar(ti,vo)
plt.show()








# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))
# fig.subplots_adjust(bottom=0.2)

# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# candlestick_ohlc(ax1, ohlc, width = 1, colorup = 'r', colordown = 'g')

# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.setp(plt.gca().get_xticklabels(), rotation=30)

# plt.grid(True)
# plt.title('Stark')
# plt.legend()
# plt.show()