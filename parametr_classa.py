
class Lamp():
	def __init__(self):
		self.light_color = ['Green', 'Red', 'Blue', 'Yellow']
		self.main_status = 0

	def light(self):
		if self.main_status >= len(self.light_color):
			self.main_status = 0
		print( self.light_color[self.main_status])
		self.main_status += 1
		

def main():
	lamp_1 = Lamp()
	lamp_1.light()
	lamp_1.light()
	lamp_1.light()
	lamp_1.light()
	lamp_1.light()

if __name__ == '__main__':
	main()