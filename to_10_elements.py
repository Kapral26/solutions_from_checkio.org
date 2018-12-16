''' 
Перевод из любой стсемы счисления в десятичный

int - товарищ, который умеет конвертировать из системы счисления в систему счисления

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1

Но я сделал из любой системы счисления, а inе имеет ограничение
'''


def checkio(str_number: str, radix: int) -> int:
	import string
	lists = list(string.ascii_uppercase)[:radix]
	k = len(str_number)-1
	res = 0
	for i in list(str_number):
		try:
			if int(i) < radix:
				res = res + int(i) * radix ** k
				# print(int(i), '*', radix,'^',k)
			else:
				return -1
		except ValueError:
			if radix > 10:
				try:
					res = res + (lists.index(i) + 10) * radix ** k
				except ValueError:
					return -1
			else :
				return -1
		k -= 1
	return res



print('2 -',checkio('101', 2))
print('5 -', checkio('101', 5))
print('16 -', checkio('AF', 16))
print('36 -', checkio('Z', 36))
print('10 -', checkio('AB', 10))
print('16 -', checkio("F0",16))
print('15 -', checkio("ASD",15))
print('9 -', checkio("909",9))
print('563 -', checkio("909144",563))