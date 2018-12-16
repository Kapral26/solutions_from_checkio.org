'''Возведение в стемень n, n-го элемента массива, если число больше возвращаем -1'''
def index_power(array: list, n: int) -> int:
	try:
		return array[n]**n
	except IndexError:
		return -1


print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 2], 3))