

def season(mouth):
	array_month = []
	times = 0
	for m in range(1,13):
		array_month.append(m)
	if mouth in array_month[2:5]:
		times = 'Весна'
	elif mouth in array_month[5:8]:
		times = 'Лето'
	elif mouth in array_month[8:11]:
		times = 'Осень'
	elif mouth in array_month[:-1] or mouth == array_month[11]:
		times = 'Зима'
	else:
		times = 'Это не месяц, а дичайшая херь'
	return(times)

array_month = []
for m in range(1,15):
	array_month.append(m)
for ss in array_month:
	print(ss, season(ss))
