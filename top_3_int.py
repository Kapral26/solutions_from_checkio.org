'''
Вывести топ n(кол-во) элементов списка
'''
import random
array1 = [random.randint(0, 1000000) for i in range(10)]

def top_item_sort(counts: int, array: list):
	array.sort()
	return(array[-counts:])


print(top_item_sort(3, array1))