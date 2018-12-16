'''Поиск заглаынх букв в строке и составление их них слова'''

# Old version
def find_message(text: str) -> str:
	"""Find a secret message"""
	message = ''
	for char in list(text):
		if char.isupper():
			message +=  char
	return message

def find_message2(text: str) -> str:
	return ''.join([x for x in text if x.isupper()])

text = "How are you? Eh, ok. Low or Lower? Ohhh."



print(find_message2(text))
