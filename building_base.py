

class Building(object):
	def __init__(self,south, west, width_WE, width_NS, height = 10):
		self.south = south
		self.west = west
		self.width_WE = width_WE
		self.width_NS = width_NS
		self.height = height
	
	def corners(self):
		south_west = [self.south,self.west]
		south_east = [south_west[0], south_west[1] + self.width_WE]
		north_west = [south_west[0] + self.width_NS, south_west[1]]
		north_east = [south_west[0] + self.width_NS, south_west[1] + self.width_WE]
		return	{"north-west": north_west, "north-east": north_east, "south-west": south_west, "south-east": south_east}

	def area(self):
		return float(self.width_NS * self.width_WE)

	def volume(self):
		return float(self.width_NS * self.width_WE * self.height)

	def __repr__(self):
		return "Building({south}, {west}, {width_WE}, {width_NS}, {height})".format(south=self.south, west=self.west, width_WE=self.width_WE, width_NS=self.width_NS, height=self.height)



if __name__ == "__main__":
	ho = Building(5,4,4,4)
	print(ho.corners())
	print(ho.area())
	print(ho.volume())
	print(ho.__repr__())
