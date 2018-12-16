'''
Проверить является две фразу аннаграммами друг другу
'''


def verify_anagrams(first_word, second_word):
	first = list([x for x in first_word.lower() if x != ' '])
	second = list([x for x in second_word.lower() if x != ' '])
	print(first)	
	print(second)
	first.sort()
	second.sort()
	if first == second:
		return True
	else:
		return False

print(verify_anagrams("Programming", "Gram Ring Mop"))
print(verify_anagrams("Hello", "Ole Oh"))