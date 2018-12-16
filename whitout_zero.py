'''Произведение всех цифр числа за исключением 0'''
def checkio(number: int) -> int:
	chk = 1
	for i in list(str(number)):
		if int(i) != 0:
			chk = int(chk) * int(i)
	return chk

print(checkio(123405))