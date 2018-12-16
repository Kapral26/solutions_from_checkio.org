''' проверка условий'''
def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        number = 'Fizz Buzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    else:
        number = str(number)
    return number

print(checkio(123))