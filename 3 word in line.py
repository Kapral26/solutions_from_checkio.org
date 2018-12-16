'''Подсчет есть ли в строке три слова подряд'''
def checkio(words: str) -> bool:
	words = words.split(" ")
	chk = 0
	for word in words:
		if word.isdigit():
			chk = 0
			continue
		else:
			chk += 1
		if chk >= 3:
			return True
	return False



text = "one two 3 four five six 7 eight 9 ten eleven 12"

print(checkio(text))


