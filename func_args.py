'''
Работа с неопределенным количеством аргументов
	В данном случае как раз найти разницу между самым большим и самым маленьким
'''
def checkio(*args):
	if len(args) == 0:
		return 0
	else:
		return round(max(args) - min(args),3)

print(checkio(1, 2, 3))