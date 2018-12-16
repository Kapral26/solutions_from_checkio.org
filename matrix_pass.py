

cipher_grille = ('X...',
				 '..X.',
				 'X..X',
				 '....')
ciphered_password = ('itdf',
         'gdce',
         'aton',
         'qrdi')				 

def recall_password(cipher_grille, ciphered_password):
	for_result = []
	in_array = []
	revers_array = []
	array_code = []
	for count in range(4):
		for i in range(len(cipher_grille)):
			for y in range(len(cipher_grille[i])):
				in_array.append(cipher_grille[y][i])
				if cipher_grille[i][y] == 'X':
					array_code.append([i,y])
			revers_array.append(''.join(in_array)[::-1])
			in_array.clear()
		cipher_grille = tuple(revers_array)
		revers_array.clear()
	# print(array_code)

	for i in array_code:
		for_result.append(ciphered_password[i[0]][i[1]])
	# print(''.join(for_result))
	return(''.join(for_result))

	
print(recall_password(cipher_grille, ciphered_password))

	
# print(array_code)
