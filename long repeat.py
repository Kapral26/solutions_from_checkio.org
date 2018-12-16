" максимальная последовательно повторенной буквы"


def long_repeat(line):
	count = 0
	array = []
	for part in range(len(line)):
		try:
			if line[part] != line[part+1]:
				# print(line[count:part+1])
				array.append(line[count:part+1])
				count = part+1
		
		except IndexError:
			# print(line[count: len(line)])
			array.append(line[count: len(line)])
	array = [len(x) for x in array if max(x)]
	if array == []:
		return 0
	else:
		return max(array)


print(long_repeat("sdsffffse"))
print(long_repeat('ddvvrwwwrggg'))
print(long_repeat(''))

