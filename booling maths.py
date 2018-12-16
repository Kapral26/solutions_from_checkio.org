'''
Булевая алгебра

 В этой миссии вам нужно реализовать несколько булевых операций:
- "конъюнкция" ("conjunction") обозначенная x ∧ y, удовлетворяющая условиям x ∧ y = 1 если x = y = 1 и  ∧ y = 0 иначе.
- "дизъюнкция" ("disjunction") обозначенная x ∨ y, удовлетворяющая условиям x ∨ y = 0 если x = y = 0 и x ∨ y = 1 иначе.
- "импликация" ("implication") (прямая импликация) обозначенная x→y и описанная как ¬ x ∨ y. Если x это истина, тогда значение x → y берется такое как у y. Но если x ложь, тогда значение y может быть игнорированно.
- "исключение" ("exclusive") (исключающее ИЛИ) обозначенное x ⊕ y и описанное как (x ∨ y)∧ ¬ (x ∧ y). Это исключает вероятность обоих x и y. В терминах арифметики, это сложение по модулю 2, где 1 + 1 = 0.
- "эквивалентность" ("equivalence") обозначенная x ≡ y и описанная как ¬ (x ⊕ y). Это истина, когда x и y имеют одинаковые значения.

Здесь вы можете увидеть таблицу истинности для данных операций:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------


'''


OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
	if operation == "conjunction":
		if x == y and x == 1:
			result = 1
		else:
			result = 0 
	elif operation == "disjunction":
		if x == y and x == 0:
			result = 0
		else:
			result = 1 
	elif operation == "implication":
		if x <= y:
			result = 1
		else:
			result = 0 
	elif operation == "exclusive":
		if x != y:
			result = 1
		else:
			result = 0 		
	elif operation == "equivalence":
		if x == y:
			result = 1
		else:
			result = 0 
		
	return result

print(boolean(0, 0, "disjunction"))