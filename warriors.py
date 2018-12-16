class Warrior:
	health = 50
	attack = 5
	is_alive = True


class Knight(Warrior):
	attack = 7

def fight(unit_1, unit_2):
	u1health = unit_1.health
	u2health = unit_2.health
	for i in range(10):
		u2health -= unit_1.attack
		print(u1health, u2health)
		print(unit_1.is_alive, unit_2.is_alive)
		if u1health > 0 and u2health <= 0:
			unit_2.is_alive = False
			unit_1.health = u1health
			print("Первый Выиграл, его жизни -", unit_1.health)
			return True
		elif u1health == 0 and u2health == 0:
			unit_1.is_alive = False
			unit_2.is_alive = False
		elif u1health <= 0 and u2health > 0:
			unit_1.is_alive = False
			unit_2.health = u2health
			print("Второй Выиграл, его жизни -", unit_2.health)
			break
		else:
			u1health -= unit_2.attack
	return False
	
	# print(unit_1.is_alive(u1health))
	# print(unit_2.is_alive(u2health))

if __name__ == '__main__':
	unit_1 = Warrior()
	unit_2 = Knight()
	unit_3 = Warrior()
	print(fight(unit_1, unit_2))

	print(fight(unit_2, unit_3))


	