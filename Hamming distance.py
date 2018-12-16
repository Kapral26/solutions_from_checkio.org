'''
Расстояние хэмминга = кол-во элементов массива, у которых один индекс но разные значения
'''

def checkio(n, m):
	print(max(m,n))
	max_bin = bin(max(m,n)).replace("0b", '')
	min_bin = bin(min(m,n)).replace("0b", '').zfill(len(max_bin))
	print(min_bin)
	print(max_bin)
	count = 0
	for i in range(len(max_bin)):
		if max_bin[i] != min_bin[i]:
			count +=1

	return count

print(checkio(1,999999))