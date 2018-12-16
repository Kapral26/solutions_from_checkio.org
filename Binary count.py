'''
Подсчет количества еденц в двоичном коде числа
'''


def checkio(number):
	return bin(number).count('1')

print(checkio(14))