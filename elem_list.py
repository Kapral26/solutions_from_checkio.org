'''
returns a tuple with 3 elements - first, third and second to the last
'''

def easy_unpack2(elements: tuple) -> tuple:
	return(elements[0],elements[2], elements[-2])


print(easy_unpack2((1, 2, 3, 4, 5, 6, 7, 9)))
print(easy_unpack2((6, 3, 7)))
