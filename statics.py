# statics.py

class housetype:

	value = 0
	clear = 0
	def __init__(self, name):
		self.name = name
		if name == "EGW":
			self.value = 285000
			self.clear = 2
		elif name == "BUN":
			self.value = 399000
			self.clear = 3
		elif name == "MAI":
			self.value = 610000
			self.clear = 6