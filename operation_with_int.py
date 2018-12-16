''' Сумма всех элементов с четным индесом и умножение этого на последний элемент массива'''
def checkio(args: list):
	if args != []:
		sun = 0
		for i in range(len(args)):
			if i % 2 == 0:
				sun = sun + args[i] 
		return sun * args[-1]
	else:
		return 0

'''
быстрое решение

list[::2] - четные индексы списка

'''
def checkio1(array):
    return sum(array[::2]) * array[-1]

print(checkio([1, 2, 3]))
print(checkio1([1, 2, 3]))