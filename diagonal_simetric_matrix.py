'''
Проверка а кососимметричность матрицы
'''

def checkio(matrix):
	for one in range(len(matrix)):
		for two in range(len(matrix[one])):
			if sum([matrix[one][two],matrix[two][one]]) == 0:
				print('Индексы:', one,two, '| обратный вариант:', -one, -two)
				print('То что совпало -',matrix[one][two], matrix[two][one])
			else:
				print('Сасай')
				return False
	return True

# print(checkio([
# 		[0, 1, 2],
# 		[-1, 0, 1],
# 		[-2, -1, 0]]))

print(
	 checkio([[-8,5,-1,7,0],[-5,-5,-7,-6,8],[1,7,1,3,4],[-7,6,-3,5,-4],[0,-8,-4,4,7]])
)