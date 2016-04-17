# test.py

class housetype:

	def __init__(self, name):
		self.name = name
		if name == "EGW":
			self.value = 285000
			self.clear = 2
			self.width = 8
			self.height = 8
		elif name == "BUN":
			self.value = 399000
			self.clear = 3
			self.width = 10
			self.height = 7.5
		elif name == "MAI":
			self.value = 610000
			self.clear = 6
			self.width = 11
			self.height = 10.5
			# total dimensions = width | height + clear

class map:
	"""Map class which contains the houses"""
	houses = []
	width = 160
	height = 150

	requiredWater = 4800
	maxWaterbodies = 4

class house:
	"""House class defining the properties of a single house to be placed in the map array"""
	kind = ""
	def __init__(self, kind):
		self.kind = kind
		self.properties = housetype(kind)
	free = 0
	x = 0
	y = 0