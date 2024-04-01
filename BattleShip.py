class player:
	def __init__(self,name):
		self.name = name
		
	
class ship:
	location = {}
	size = 0
	def __init__(self,location,size,is_hit = False):
		self.location = location
		self.size = size

