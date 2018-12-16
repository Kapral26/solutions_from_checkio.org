'''
Оставить только не уникальные элементы списка

[x for x in data if data.count(x) != 1]
вывести все элементы списка date где количество больше 1
'''
def checkio(data: list) -> list:
	return [x for x in data if data.count(x) != 1] 

print(checkio([1, 2, 3, 1, 3]))