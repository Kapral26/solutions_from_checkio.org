import datetime
from datetime import datetime

# OLD VERSION
def is_year_leap(year):
	date = 0
	try:
		date = datetime(year, 2, 29)
		# print(year, ' - True')
	except ValueError:
		return(False)
	return True

arrya_years = []
for i in range(1, 9999):
	arrya_years.append(int(i))

count_v = 0
count_other = 0
for ya in arrya_years:
	# print (is_year_leap(ya))
	if is_year_leap(ya) == True:
		# print (is_year_leap(ya))
		count_v += 1
	else:
		count_other +=1
# ---------------

# new VERSION
for x in range(1970, 9999):
	try:
		print(datetime(x, 2, 29).year)
	except ValueError:
		continue