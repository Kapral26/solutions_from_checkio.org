'''
Прверка все ли эелемнты массива одинковы
'''

from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
	ll = [x for x in elements if elements.count(x) == len(elements)] 
	if ll != [] or elements == []:
		return True
	else:
		return False


def all_the_same2(elements: List[Any]) -> bool:
	if len(set(elements)) == 1:
		return True
	else:
		return False

print(all_the_same([1, 1, 1]))
print(all_the_same2([1, 1, 1]))