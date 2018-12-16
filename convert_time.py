

import time
def time_converter(tim):
	tim = tim.replace(' ','').replace('.', '')
	times = time.strptime(tim.upper(), '%I:%M%p')
	return time.strftime('%H:%M', times)

print("Example:")
print(time_converter('12:30 p.m.'))
# p.m.