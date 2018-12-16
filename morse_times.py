'''
Перевести время в формат морзянки.

первая часы: первая часть числа 2 символа, вторая 4
		минуты, секунды: первая часть числа 3 символа, вторая 4

если число состоит из 1 части, добавить перед ней 0

'''

def checkio(time_string):
	time = [ x if len(x) > 1 else '0' + str(x) for x in time_string.split(":")]
	time =	[
	' '.join(
			[	
				bin(int(str(x[0]))).replace('0b','').zfill(2),
				bin(int(str(x[1]))).replace('0b','').zfill(4)
			]
			) if x == time[0]
				else ' '.join(
			[	
				bin(int(str(x[0]))).replace('0b','').zfill(3),
				bin(int(str(x[1]))).replace('0b','').zfill(4)
			]
			)  for x in time
				]

	return ' : '.join([x.replace('0b', '0').replace('1','-').replace('0', '.') for x in time])



print((checkio("10:37:49")))
print(".- .... : .-- .--- : -.. -..-")
# print(checkio("21:34:56"))


"..- .... : .-- .--- : -.. -..-"
".- .... : .-- .--- : -.. -..-"