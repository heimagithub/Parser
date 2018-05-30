

mon = ['12','11','10','09','08','07','06','05','04','03','02','01']

mon_Idx = 8
year = 2018
year_end = 2015

date = []

while(1):

	if mon_Idx == 12:
		year -= 1
		mon_Idx = 0

	if year == year_end:
		break

	date.append(str(year)+mon[mon_Idx]+'01')

	mon_Idx += 1

print(date)

