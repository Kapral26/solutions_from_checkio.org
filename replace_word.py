'''Замена слова в тексте'''
def left_join(phrases):
	l=[]
	for i in phrases:
		l.append((i.replace("right","left")))
	return ','.join(l)

phrases = "left", "right", "left", "stop"

print(left_join(phrases))
