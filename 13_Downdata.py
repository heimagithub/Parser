import requests
import json

from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

import numpy as np 
from datetime import datetime 

import time

import pandas as pd

res = requests.get('https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=m&mkt=10&sym=2330')

res = res.text.split('null(')
res = res[1].split(');')
data = json.loads(res[0])

# print(len(data['ta']))

# 'c': 73.6, 'h': 74.0, 't': 20111031, 'l': 68.1, 'v': 826861, 'o': 70.0
ti = []
op = []
cl = []
hi = []
lo = []
vo = []

for i in range(len(data['ta'])):

	ti.append(float(data['ta'][i]['t']))
	op.append(float(data['ta'][i]['o']))
	cl.append(float(data['ta'][i]['c']))
	hi.append(float(data['ta'][i]['h']))
	lo.append(float(data['ta'][i]['l']))
	vo.append(float(data['ta'][i]['v']))

	print(data['ta'][i]['v'])

book = {}
book['time'] = ti
book['open'] = op
book['close'] = cl
book['high'] = hi
book['low'] = lo
book['volumn'] = vo

df = pd.DataFrame(book, columns = ['time', 'open', 'close', 'high', 'low', 'volumn'])
df.to_csv('/home/heima/Parser/test.csv')