import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 

import tkinter as tk 
from tkinter import ttk

import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.finance import candlestick_ohlc


LARGE_FONT = ('Verdana', 12)

class SeaofBTCapp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side = 'top', fill = 'both', expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for F in (FirstPage, Home):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = 'nsew')

		self.show_frame(FirstPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class FirstPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = 'First Page', font = LARGE_FONT)
		label.pack(pady = 10, padx = 10)

		button1 = ttk.Button(self, text = 'Stark', command = lambda: controller.show_frame(Home))
		button1.pack()

class Home(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = 'Home Page', font = LARGE_FONT)
		label.pack(pady = 10, padx = 10)

		e = tk.Entry(self,show='*')
		e.pack()



		df = pd.read_csv('/home/heima/Parser/2317.csv')

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

		fig = plt.figure()
        ## show all datatime
		fig.subplots_adjust(bottom = 0.15)

		ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 2)

		plt.plot(ti, goog["ma5"], label = 'MA5')
		plt.plot(ti, goog["ma20"], label = 'MA20')
		legend = ax1.legend(loc='best', shadow=True, fontsize='x-large')

		candlestick_ohlc(ax1, ohlc, width = 10, colorup = 'r', colordown = 'g')


		ax1.set_title('Stark')
		ax1.grid(True)
		plt.gca().axes.get_xaxis().set_visible(False)


		ax2 = plt.subplot2grid((3,3), (2,0), colspan = 3)

		plt.bar(ti, vo)
		plt.bar(ti, vo, width = 10)
		ax2.set_ylabel('Volumn')
		ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		plt.setp(plt.gca().get_xticklabels(), rotation = 30)


        # plt.show()


        

		canvas = FigureCanvasTkAgg(fig, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		def Search_fun():
			var = e.get()
			l2.config(text = var)

			##
			fig.clear()

			df = pd.read_csv('/home/heima/Parser/2330.csv')

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

			# fig = plt.figure()
	        ## show all datatime
			# fig.subplots_adjust(bottom = 0.15)

			ax1 = plt.subplot2grid((3,3), (0,0), colspan = 3, rowspan = 2)

			plt.plot(ti, goog["ma5"], label = 'MA5')
			plt.plot(ti, goog["ma20"], label = 'MA20')
			legend = ax1.legend(loc='best', shadow=True, fontsize='x-large')

			candlestick_ohlc(ax1, ohlc, width = 10, colorup = 'r', colordown = 'g')


			ax1.set_title('Stark')
			ax1.grid(True)
			plt.gca().axes.get_xaxis().set_visible(False)


			ax2 = plt.subplot2grid((3,3), (2,0), colspan = 3)

			plt.bar(ti, vo)
			plt.bar(ti, vo, width = 10)
			ax2.set_ylabel('Volumn')
			ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
			plt.setp(plt.gca().get_xticklabels(), rotation = 30)

			canvas = FigureCanvasTkAgg(fig, self)
			canvas.show()
			# canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)		
			##

		b1 = tk.Button(self,text = "Search",width = 15,height = 2,command = Search_fun)
		b1.pack()

		l2 = tk.Label(self, text = '', font = LARGE_FONT)
		l2.pack(pady = 50, padx = 10)
		

app = SeaofBTCapp()
app.mainloop()