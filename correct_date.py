'''
Перевод в удобночитаемый вид даты(Есть библиотека datetime)
'''

def date_time(time: str) -> str:
	mounth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	mounth = list(zip([x for x in range(1,13)], mounth))
	date = time.split(' ')[0].split('.')
	print(date)
	full_date = [str(int(date[0])), [x[1] for x in mounth if str(x[0]) == str(int(date[1]))][0], date[2], 'year']
	full_time = []
	times = time.split(' ')[1].split(':')
	print(times)
	full_time.append(str(int(times[0])))
	print(int(times[0]))
	if times[0] == '01':
		full_time.append('hour')
	else:
		full_time.append('hours')
	full_time.append(str(int(times[1])))
	print(int(times[1]))
	if times[1] == '01':
		full_time.append('minute')
	else:
		full_time.append('minutes')
	return ' '.join([' '.join(full_date), ' '.join(full_time)])

print(date_time("01.01.2000 00:00"))

# year, hour/hours, minute/minutes

