'''
Поиск победителя в крестики нолики

'''


from typing import List
def checkio(game_result: List[str]) -> str:
	array_x = ['X','X','X']
	array_o = ['O','O','O']
	#Массив строк и столбцов
	array = [[x[i] for x in game_result] for i in range(3)] + [list(x) for x in game_result] 
	# Диагональ 1
	d1 = [[game_result[0][0], game_result[1][1], game_result[2][2]]]
	# Диагональ 2
	d2 = [[game_result[2][0], game_result[1][1], game_result[0][2]]]
	# Общий массив всех послежовательностей
	all_array = array + d1 + d2
	# Поиск элемента по маске где 3 одинковых
	res = [x for x in all_array if x == array_x or x == array_o]
	# Если такой есть определяем, кто победил
	if res:
		if res[0][0] == 'X':
			result = 'X'
		elif res[0][0] == 'O':
			result = 'O'
	# Ни кто не победил
	else:
		result = 'D'
	return result


print(checkio(["OXO","XXO","XOX"]))
print(checkio([
        "OOX",
        "XXO",
        "OXX"]))

# print (checkio([
#         "OO.",
#         "XOX",
#         "XOX"]))