'''
Перевод числа в римской вид
'''

def checkio(data):
	#Словарь с основными обозначениями
	dict_num = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'IV': 4, 'IX':9, 'CD': 400  ,'XL':40, 'XC':90, 'CM':900}
	#Cgbcjr njkmrj pyfxtybq b tuj cjhnbhjdrf
	dict_num_val = [x for x in dict_num.values()]
	dict_num_val.sort(reverse=True)
	print(dict_num_val)
	res = []
	for i in dict_num_val:
		#Делим без остатка
		num = divmod(data,i)
		print(num)
		# Если целой части нет
		if num[0] != 0:
			# Определяем ключ от целой части, для буквенного обозначения
			key = [x[0] for x in dict_num.items() if x[1] == i][0]
			print(key)
			# Добавляем буквенное обозначение в массив
			res.append(key*num[0])
			# дробную чать записываем в переменную
			data = num[1]
		# else:
		# 	res.append(num[0]*i)
	
	return ''.join(res)
print(checkio(99))
# print( checkio(6))
# print( checkio(76))
# print( checkio(499))
# print( checkio(3888))