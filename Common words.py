'''
Поиск слов, которые есть в двух фразах имеется ввиду полное сапостовление
'''


def checkio(first, second):
	array_first = first.split(",")
	array_second = second.split(",")
	# Собирается массив если множество совпадает и не равно пустоте
	result = [','.join([x for x in array_first if set(x) == set(y)]) for y in array_second if [x for x in array_first if set(x) == set(y)] != []]
	if result == []:
		return "" 
	result.sort()
	return ','.join(result)


# print(checkio("hello,world", "hello,earth"))
# print(checkio("one,two,three", "four,five,six"))
print(checkio("one,two,three","four,five,one,two,six,three"))