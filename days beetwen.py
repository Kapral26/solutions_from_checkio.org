'''
Разница дат в днях
'''
from datetime import datetime, timedelta, date
def days_diff(date1, date2):
	date1 = date(date1[0], date1[1], date1[-1])
	#------------
	date2 = date(date2[0], date2[1], date2[-1])
	result = date1 - date2
	try:
		result = int(str(abs(result)).split(' ')[0])
	except ValueError:
		result = 0

	print('Страшный день календаря', date1 + timedelta(666))
	return result


# date3 = 1,1,1
# print(date3[0], date3[1], date3[-1])
# print(date(date3))
# print(days_diff((1982, 4, 19), (1982, 4, 22)))
# print(days_diff((2014,1,1), (2014,8,27)))
# print(days_diff((1,1,1), (9999,12,31)))
print(days_diff((1990,6,24), (2018,6,5)))






