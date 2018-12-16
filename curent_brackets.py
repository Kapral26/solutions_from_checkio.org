'''
Проверка корректности простановки скобок
'''

def checkio(expression):
	import re
	#Список скобок
	array_symbol = ['()', '{}', '[]']
	# оставляем только скобки
	result = re.findall('[^0-9\+\-\*\/]', expression)
	# Обьединяем все элементы списка
	result = ''.join(result)
	# Заменяем все элементы объединенных скобок 10 в 3 с тепени раз. чтобы все заменить на пустоту
	for i in range(10**3):
		for symbol in array_symbol:
			result = result.replace(symbol, '')
	# Если после всех замен список пуст, то все бенч
	if len(result) == 0:		
		return True
	else:
		return False
print(checkio("((5+3)*2+1)"))
print(checkio("{[(3+1)+2]+}"))
print(checkio("(3+{1-1)}"))


