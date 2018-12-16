VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
		  't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
		  'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
		  'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
		  'q': 10, 'z': 10}

def worth_of_words(words):
	array_test = []
	sum_char = 0
	for word in words:
		for char in word:
			# print(VALUES.get(char))
			sum_char += VALUES.get(char)
		array_test.append(sum_char)
		sum_char = 0
	indx = array_test.index(max(array_test))
	return words[indx]

if __name__ == '__main__':
	print("Example:")
	print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))