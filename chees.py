'''
Анализ положений пешек, подсчет тех кто защищен от всех атак.

'''

def safe_pawns(pawns: set) -> int:
	# Массив горизонтальной шкалы
	vertical = 'abcdefgh'
	# Всего элементов
	result = len(pawns)
	# положения на численой шкале
	cont_num = [x[1] for x in pawns]
	# Если кол-во пешек и количество пешек на одной линии значит все пешки не защищены
	if len(cont_num) == cont_num.count(cont_num[0]):
		return 0
	else:
		for x in pawns:
			try:
				# Если не кране правый столбец, то проверка наличия фигуры со сдвигом на право и минус 1
				if x[0] != 'h':
					x_1 = str(vertical[vertical.index(x[0])+1]) + str(int(x[1]) - 1)
				else:
					x_1 = 0
				# print('done -', x)
			except IndexError:
				x_1 = 0
			try:
				# Если не кране левый столбец, то проверка наличия фигуры со сдвигом на лево и минус 1
				if x[0] != 'a':	
					x__1 = str(vertical[vertical.index(x[0])-1]) + str(int(x[1]) - 1)
				else:
					x__1 = 0
			except IndexError:
				x__1 = 0
			# проверка если нижних пешек нет, то она не защищена. Отнимаем от кол-ва всех элементов
			if x_1 not in pawns and x__1 not in pawns:
				# print(x)
				result = result - 1
			else:
				print(x__1, x, x_1)
		return result


# print(safe_pawns(["a2","b2","c2","d2","e2","f2","g2","h2"]))
# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
# print(safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}))
# print(safe_pawns({"h8"}))
print(safe_pawns(["a8","b7","c6","d5","e4","f3","g2","h1"]))
# print(safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"]))