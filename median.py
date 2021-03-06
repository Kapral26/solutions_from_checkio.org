'''
Нахождене медианы в массиве

Медиана - это числовое значение, которое делит сортированый массив чисел на большую и меньшую половины. 
В сортированом массиве с нечетным числом элементов медиана - это число в середине массива.
Для массива с четным числом элементов, где нет одного элемента точно посередине, медиана - это среднее значение двух чисел, находящихся в середине массива. 
В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива. 
'''

from typing import List

def checkio(data: List[int]) -> [int, float]:
	data.sort()
	print(data)
	part = len(data)//2
	if len(data)%2 == 0:
		result = (data[part]+data[part-1])/2
	else:
		result = data[part]
	#replace this for solution
	return result

# print(checkio([1, 2, 3, 4, 5]))
# print(checkio([3,6,20,99,10,15]))
# print(checkio([25.8, 19.0, 23.6, 17.2, 16.2, 30.5, 10, 18.9, 29.5, 14.2, 20.6, 12.2, 16, 18.6, 23.2, 15.1, 16.3, 17.8, 22.6, 11.8, 22.8, 18.8, 20.2, 17]))
array = [47.8,37.2,68.7,31.5,39.4,53.5,55.9,48.1,31.3,15.5,44.7,22.1,33.6,37.8,42.1,25.4,28.9,32.0,31.2,31.7,40.5,31.4,31.8,20.8,32.8,47.7,47.3,34.9,24.8,23.3,18.8,39.2,35.4,36.4,35.4,38.9,35.9,36.2,33.5,41.9,30.5,34.3,41.5,31.8,28.4,43.0,26.0,36.9,62.5,42.6,36.9,49.1,35.6,54.1,42.7,36.8,49.9,27.8,23.4,20.6,21.2,23.6,28.0,32.3,26.0,35.0,32.3,28.0,40.2]
print(checkio(array))