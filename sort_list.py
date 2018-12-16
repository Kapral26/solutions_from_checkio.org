'''
Сортировка чисел не зависимо от их знака = по модулю

быстрый результат
return sorted(list(numbers_array), key=lambda x: abs(x))

'''
def checkio(numbers_array: tuple) -> list:
	numbers_array = list(numbers_array)
	l =[]
	for i in numbers_array:
		print(abs(i))
		l.append(abs(i))
	l.sort()
	for i in range(len(l)):
		if l[i] not in numbers_array:
			l[i] = -l[i]
	return l

print(checkio((-20, -5, 15, 10)))