
def house(plan):
	plan = plan.split("\n")
	width = max([i.count("#") for i in plan])
	print(width)

	row = []
	for i in range(len(plan)):
		
		nn = ''
		for y in range(len(plan[i])):
			# print(y)
			# nn += str(plan[y][i])
			try:
				nn += str(plan[y][i])
			except IndexError:
				continue
		row.append(nn)
		del nn
	
	print(row)
	height = max([i.count("#") for i in row])

	# print(width, height, width*height)
	return width*height

def main():

	res1 = house("0000##0000\n#000##000#\n##########\n##000000##\n0########0\n")
	print(res1)


if __name__ == '__main__':
	main()