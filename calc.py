

def arifthmetic(num1,num2,dev):
    result = 0 
    if dev == '+':
        result = num1 + num2 
    elif dev == '-':
        result = num1 - num2 
    elif dev == '*':
        result = num1 * num2 
    elif dev == '/':
        result = num1 / num2 
    else:
        result = 'Неизвестная операция'
    return(result)

num1 = float(input('Число номер 1\n'))
dev = input('Оперрация\n')
num2 = float(input('Число номер 2\n'))

print('Результат  - ', arifthmetic(num1,num2,dev))