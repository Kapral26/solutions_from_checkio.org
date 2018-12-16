def two_teams(sailors):
	first_team = [key for key, value in sailors.items() if value <= 20 or value >= 40]
	second_team = [key for key, value in sailors.items() if value > 20 and value < 40]
	first_team.sort()
	second_team.sort()
	return [first_team, second_team]

def main():
	res = two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19})
	print(res)


if __name__ == '__main__':
	main()