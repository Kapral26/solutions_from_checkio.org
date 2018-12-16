'''
Проверка на ввод пароля. не меньше 10 символов, минимум 1 заглавная, 1 в нижнем и 1 цифра

'''

def checkio(data: str) -> bool:
	import re
	res = re.match("[a-zA-Z0-9]+", data)
	lens = len(data) >= 10
	digit = list(filter(lambda x: x.isdigit(),data))
	lowchar = list(filter(lambda x: x.islower(),data))
	upchar = list(filter(lambda x: x.isupper(),data))
	if digit and upchar and lowchar and res and lens:
		return True
	else:
		return False

print(checkio('12345678910'))
print(checkio('1213pokl'))
print(checkio('A1213pokl'))
print(checkio('A1213привет'))