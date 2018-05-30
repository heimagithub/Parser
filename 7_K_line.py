import requests
import json

from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

import numpy as np 
from datetime import datetime 

import time

# style.use('ggplot')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


res = requests.get('https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=m&mkt=10&sym=2330')

res = res.text.split('null(')
res = res[1].split(');')
data = json.loads(res[0])


x = 0
y = len(data['ta'])
ohlc = []


while x < y:
	append_me = float(mdates.date2num(datetime.strptime(str(data['ta'][x]['t']), '%Y%m%d'))), float(data['ta'][x]['o']), float(data['ta'][x]['h']), float(data['ta'][x]['l']), float(data['ta'][x]['c']), float(data['ta'][x]['v'])
	ohlc.append(append_me)
	x += 1 



fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
fig.subplots_adjust(bottom=0.2)

# for label in ax1.xaxis.get_ticklabels():
# 	label.set_rotation(45)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# candlestick_ohlc(ax1, ohlc, width = 0.6, colorup = '#77d879', colordown = '#db3f3f')
candlestick_ohlc(ax1, ohlc, width = 1, colorup = 'r', colordown = 'g')

# ax1.xaxis_date()
# ax1.autoscale_view()

plt.xlabel('Date')
plt.ylabel('Price')
# plt.autoscale(True, 'both', None)
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.grid(True)
plt.title('Stark')
plt.legend()
plt.show()