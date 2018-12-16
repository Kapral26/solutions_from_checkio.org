
dict1 = {
		'CAC': 10.0,
		'ATX': 390.2,
		'WIG': 1.2
	}

dict2 = {
		'CAC': 91.1,
		'ATX': 1.01,
		'TASI': 120.9
	}


def best_stock(data):
	max_stock = 0
	max_key = ''
	for key in data:
		if data[key] > max_stock:
			max_stock = data[key]
			max_key = key
	return(max_key)

def best_stock2(data):
	return [x for x in dict1 if dict1[x] == max(dict1.values())][0]

print(best_stock(dict1))
print(best_stock(dict2))


print(best_stock2(dict1))
print(best_stock2(dict2))

