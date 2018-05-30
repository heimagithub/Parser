import requests
import json

import matplotlib.dates as mdates
from datetime import datetime 

import pandas as pd

import time


ti = []
sa = []
sm = []
op = []
hi = []
lo = []
cl = []
pdiff = []
okacc = []
# vo = []


mon = ['12','11','10','09','08','07','06','05','04','03','02','01']

mon_Idx = 10
year = 2018
year_end = 1991

while(1):

	if mon_Idx == 12:
		year -= 1
		mon_Idx = 0

	if year == year_end:
		break

	date = str(year)+mon[mon_Idx]+'01'

	res = requests.get('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo=2330')
	data = json.loads(res.text)

	if len(data) == 1:
		break

	# data['data'] = data['data'].reverse()

	ti_ = []
	op_ = []
	hi_ = []
	lo_ = []
	cl_ = []
	# vo_ = []

	for row in data['data']:

		date = row[0].split("/")
		date2 = str(int(date[0])+1911)+date[1]+date[2]
		print(date2)

		ti_.append(date2)
		# sa.append(float(row[1]))
		# sm.append(float(row[2]))
		op_.append(float(row[3]))
		hi_.append(float(row[4]))
		lo_.append(float(row[5]))
		cl_.append(float(row[6]))		


	for idx in range(len(op_)-1, -1, -1):

		ti.append(ti_[idx])
		op.append(op_[idx])
		hi.append(hi_[idx])
		lo.append(lo_[idx])
		cl.append(cl_[idx])

	mon_Idx += 1
	time.sleep(3)

ti = ti[::-1]
op = op[::-1]
hi = hi[::-1]
lo = lo[::-1]
cl = cl[::-1]
# ti = ti.reverse()
# op = op.reverse()
# hi = hi.reverse()
# lo = lo.reverse()
# cl = cl.reverse()

book = {}
book['time'] = ti
book['open'] = op
book['close'] = cl
book['high'] = hi
book['low'] = lo
# book['volumn'] = vo

print(book)

df = pd.DataFrame(book, columns = ['time', 'open', 'close', 'high', 'low'])
df.to_csv('/home/heima/Parser/test.csv')