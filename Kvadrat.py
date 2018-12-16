import math

def square(wall):

    P = wall * 4
    S =  wall ** 2
    D = wall * math.sqrt(2)
    main_info = {P, S, D}
    return main_info

wall = float(input('Сотроно квадрата \n'))

print(square(wall))