'''
Шифрование шифром Цезаря
'''
def to_encrypt(text, delta):
	import string
	letter = list(string.ascii_letters)
	# ll =  [letter[letter.index(x)+delta] for x in list(text) if x != ' ']
	array = []
	for x in text.lower():
		try:
			array.append(letter[letter.index(x)+delta].lower())
		except:
			array.append(x)
	return "".join(array)

print(to_encrypt('abc', -10))
print(to_encrypt("a b c", 3))