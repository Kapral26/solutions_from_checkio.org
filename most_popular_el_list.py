"""
		элемент массива который больше всего встречается в списке
"""

def most_frequent(data: list) -> str:

	return max(data, key = lambda x: data.count(x))

print(most_frequent([
		'a', 'b', 'c', 
		'a', 'b',
		'a'
	]))	