import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.finance import candlestick_ohlc

import matplotlib.dates as mdates
from datetime import datetime

import tkinter as tk

class Application(tk.Tk):
    '''
    文件夹选择程序
        界面与逻辑分离
    '''
    stark_index = 2330

    def __init__(self):
        '''初始化'''
        super().__init__() # 有点相当于tk.Tk()
        self.wm_title("Embed matplotlib in tkinter")
        
        self.createWidgets()

    def createWidgets(self):
        '''界面'''
        fig = Figure(figsize=(10,8), dpi=100)
        # self.ax = fig.add_subplot(111)
        grid = plt.GridSpec(3, 1, wspace=0.5, hspace=0.5)
        self.ax1 = fig.add_subplot(grid[0,1:2])
        self.ax2 = fig.add_subplot(grid[2,0])

        # self.ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 2)
        # self.ax2 = plt.subplot2grid((3,3), (2,0), colspan = 3)


        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        footframe = tk.Frame(master=self).pack(side=tk.BOTTOM)

        tk.Button(master=footframe, text='重画', command=self.draw).pack(side=tk.BOTTOM)
        tk.Button(master=footframe, text='退出', command=self._quit).pack(side=tk.BOTTOM)
        
        self.draw() # 绘图

        
    def draw(self):
        '''绘图逻辑'''

        if self.stark_index == 2330:
            self.stark_index = 2317
        else:
            self.stark_index = 2330

        filename = '/home/heima/Parser/'+str(self.stark_index)+'.csv'
        
        df = pd.read_csv(filename)

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

        x = np.random.randint(0,50,size=100)
        y = np.random.randint(0,50,size=100)
        
        #self.fig.clf()                  # 方式一：①清除整个Figure区域
        #self.ax = self.fig.add_subplot(111)    # ②重新分配Axes区域
        self.ax1.clear()                  # 方式二：①清除原来的Axes区域
        self.ax2.clear()                  # 方式二：①清除原来的Axes区域

        self.ax1.plot(ti, goog["ma5"], label = 'MA5')
        self.ax1.plot(ti, goog["ma20"], label = 'MA20')
        legend =  self.ax1.legend(loc='best', shadow=True, fontsize='x-large')
        candlestick_ohlc(self.ax1, ohlc, width = 10, colorup = 'r', colordown = 'g')

        self.ax1.set_title('Stark')
        self.ax1.grid(True)
        # self.ax1.gca().axes.get_xaxis().set_visible(False)

        self.ax2.bar(ti, vo)
        self.ax2.bar(ti, vo, width = 10)
        self.ax2.set_ylabel('Volumn')
        self.ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        self.ax2.grid(True)

        for tick in self.ax2.get_xticklabels():
            tick.set_rotation(45)
        
        self.canvas.show()
    
    
    def _quit(self):
        '''退出'''
        self.quit()     # 停止 mainloop
        self.destroy()  # 销毁所有部件

        
if __name__ == '__main__':
    # 实例化Application
    app = Application()
    
    # 主消息循环:
    app.mainloop()