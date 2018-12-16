VOWELS = "aeiouy"

def translate(phrase):
	phrase = list(phrase)
	# print(phrase)
	for x in range(len(phrase)):
		try:
			if phrase[x] not in VOWELS and phrase[x+1] in VOWELS and phrase[x] != ' ':
				phrase.pop(x+1)
		except IndexError:
			continue	
	phrase = ''.join(phrase)
	
	for x in range(len(phrase)):
		try:
			if phrase[x] in VOWELS and phrase[x] == phrase[x+1] and phrase[x] == phrase[x+2]:
				phrase = phrase.replace(phrase[x]*3, phrase[x])
		except IndexError:
			continue
	return phrase

print(translate("hoooowe yyyooouuu duoooiiine"))
