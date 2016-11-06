class Counter():
	
	def __init__(self):
		self.counter = 0
	
	
	def direction_count(self,direction):
		dir_dict={'up':1,'right':2,'down':3,'left':4}
		self.counter += dir_dict[direction]
