'''
Определене угла солна на основании времени

по алгоритму:
	90/6 = градусов в час
	90/6/60 = в минуту

от текущего времени отнимаем 6 и умножаем на градусов в час, минуты просто умножаем

'''

def sun_angle(time):
	time = time.split(":")
	cirkul = round((float(time[0]) - 6) * 90/6 + float(time[1]) * (90/6)/60,2)
	if cirkul > 180.00 or cirkul < 0:
		cirkul = "I don't see the sun!"
	return cirkul

print(sun_angle("05:55"))