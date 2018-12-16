MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(text):
	text = text.lower()
	array = text.split('   ')
	text = []
	for x in array:
		part = x.split(' ')
		lists = [p[0][0] for p in [[i[1]for i in MORSE.items() if i[0] == y] for y in part]]	
		print(lists)
		lists = ''.join(lists)
		text.append(lists)
	
	result = ' '.join(text)

	return result[0].upper() + result[1:]


print(
	morse_decoder('...- ...-- .-. -.-- .---- ----- -. --. ... - .-. .---- -. --. .-- .---- - .... ... ----- -- ...-- -. ..- -- -... ...-- .-. .....')
)

