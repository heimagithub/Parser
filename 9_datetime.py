# import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange

from datetime import datetime
import datetime as dt


# date1 = datetime.datetime(2000, 3, 2)
# date2 = datetime.datetime(2000, 3, 6)
# delta = datetime.timedelta(hours=6)
# dates = drange(date1, date2, delta)

# y = arange(len(dates)*1.0)

# print(date1)
# print(dates)

# fig, ax = plt.subplots()
# ax.plot_date(dates, y*y)
# plt.show()


date1 = 20150303
date2 = 20150305

date1 = datetime.strptime(str(date1), '%Y%m%d').date()
date2 = datetime.strptime(str(date2), '%Y%m%d').date()

delta = dt.timedelta(hours=6)
dates = drange(date1, date2, delta)

print(dates)


