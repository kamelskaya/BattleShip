class player:
	def __init__(self,name):
		self.name = name
		
	
class ship:
	location = {}
	size = 0
	def __init__(self,location,size,is_hit = False):
		self.location = location
		self.size = size

name_player = input("Welcome to Battle Ship! Please, enter your name")
player1 = player(name_player)
print("Your name is "player1.name)