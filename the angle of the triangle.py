'''
Углы треугольника, при передаче функции длины сторон
'''

from typing import List

def checkio(a: int, b: int, c: int) -> List[int]:
	from math import degrees, acos
	try:
		res_c = acos((a**2 + b**2 - c**2) / (2*a*b))
		res_b = acos((a**2 + c**2 - b**2) / (2*a*c))
		res_a = acos((b**2 + c**2 - a**2) / (2*c*b))
		res = [ round(degrees(res_a)), round(degrees(res_b)), round(degrees(res_c))]
		res.sort()
		if [x for x in res if x == 0 ]:
			res = [0,0,0]
	except ValueError:
		res = [0,0,0]
	return res

print(checkio(10, 20, 30))
print(checkio(80,80,60))

