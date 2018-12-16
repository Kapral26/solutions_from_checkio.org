from collections import Counter

'''
найти самое популярную букву, не зависимо от регистра

'''

def checkio(data: str) -> str:
	import string
	import re
	#Все буквы делаем нижнего регистра
	data = data.lower()
	#оставляем только буквы
	data = re.findall('[A-z]', data)
	#список всех латинских букв
	lists = list(string.ascii_letters)
	#Генерируем словарь где ключ это буква, а значение это кол-во повторений
	rr = {x: data.count(x) for x in data}
	#Максимальное значение повторений
	max_rr = max(list(rr.values()))
	#Список всех значений равных максимальному
	ll = [x for x in rr.values() if x == max_rr]
	#Если значений больше двух, то будем выводить ту букывц, которая ближе к началу алфавита, иначе букву с максимальным повторением
	if len(ll) >= 2:
		pp = [list(x)[0] for x in rr.items() if list(x)[1] == max_rr]
		result = min(pp, key = lambda x: lists.index(x))
	else:
		result = max(data, key = lambda x: data.count(x))
	return result


print(checkio("Hello World!"))
print(checkio("One"))
print(checkio("Oops!"))
print(checkio("AAaooo!!!!"))
print(checkio("Lorem ipsum dolor sit amet"))