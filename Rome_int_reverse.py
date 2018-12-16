'''
Перевод из римской системы счисления в десятичную
'''

def reverse_roman(data):
	dict_num = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'IV': 4, 'IX':9, 'CD': 400  ,'XL':40, 'XC':90, 'CM':900}	
	aa = [[int(x[1]) for x in dict_num.items() if x[0] == y] for y in data]
	aa = [int(x[0]) for x in aa]
	print(aa, sum(aa))
	chk = []
	sums = 0
	for i in range(len(aa)):
		#print(sums, aa[i])
		try:
			if int(aa[i]) < int(aa[i+1]):
				chk.append( int(aa[i+1]) - int(aa[i]) )
				print('minus',int(aa[i+1]) ,'-', int(aa[i]))
				aa.pop(i+1)
				aa.append(0)
			else:
				chk.append(int(aa[i]))
		except IndexError:
			chk.append(int(aa[i]))
			continue

	return chk, sum(chk)

# print(reverse_roman('I'))
print(reverse_roman("MMMCMXCIX"))
# print(reverse_roman('CDXCIX'))
# print(reverse_roman("LXXXVIII"))
# print(reverse_roman("CDLXXIII"))

