import pandas as pd

from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib.dates import WeekdayLocator, MONDAY, DayLocator, DateFormatter

from datetime import datetime 

import numpy as np 

import time


def pandas_candlestick_ohlc(stock_data, otherseries=None):    

    mondays = WeekdayLocator(MONDAY) 
    alldays = DayLocator()   
    dayFormatter = DateFormatter('%d')

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    if stock_data.index[-1] - stock_data.index[0] < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%b %d')  
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)

    stock_array = np.array(stock_data.reset_index()[['date','open','high','low','close']])
    stock_array[:,0] = date2num(stock_array[:,0])
    candlestick_ohlc(ax, stock_array, colorup = "red", colordown="green", width=0.4)

    if otherseries is not None:
        for each in otherseries:
            plt.plot(stock_data[each], label=each)            
        plt.legend()

    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()

df = pd.read_csv('/home/heima/Parser/test.csv')

ohlc = []
ti = []
vo = []
cl = []

for i in range(len(df)):
	append_me = float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))), float(df.open[i]), float(df.high[i]), float(df.low[i]), float(df.close[i]), float(df.volumn[i])
	ohlc.append(append_me)

	ti.append(float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))))
	vo.append(float(df.volumn[i]))
	cl.append(float(df.close[i]))

	# print(str(float(mdates.date2num(datetime.strptime(str(int(df.time[i])), '%Y%m%d'))))+' | '+str(df.volumn[i]))

cl = pd.DataFrame(cl)

goog = {}
## MA
goog["ma5"] = np.round(cl.rolling(window = 5, center = False).mean(), 2)
goog["ma20"] = np.round(cl.rolling(window = 20, center = False).mean(), 2)

print(cl)
print(goog["ma5"])

fig = plt.figure()
## show all datatime
fig.subplots_adjust(bottom = 0.15)

ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 2)

plt.plot(ti, goog["ma5"], label = 'MA5')
plt.plot(ti, goog["ma20"], label = 'MA20')
legend = ax1.legend(loc='best', shadow=True, fontsize='x-large')

candlestick_ohlc(ax1, ohlc, width = 10, colorup = 'r', colordown = 'g')


# pandas_candlestick_ohlc(goog, ['ma5','ma20'])

ax1.set_title('Stark')
ax1.grid(True)
plt.gca().axes.get_xaxis().set_visible(False)


ax2 = plt.subplot2grid((3,3), (2,0), colspan = 3)

plt.bar(ti, vo)
plt.bar(ti, vo, width = 10)
ax2.set_ylabel('Volumn')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.setp(plt.gca().get_xticklabels(), rotation = 30)


plt.show()






