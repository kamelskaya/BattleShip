##Класс PLAYER с набором кораблей
class player:
	ships = []
	is_lose = False
	def __init__(self,name):
		self.name = name
		
	def player_hit(self,location):
		#for ship in ships:
		#	if location in ship.location:
		#		ship_hit = True
		
			
	def is_player_lose(self):
		ships_hit = 0	
		for ship in ships:
			if ship.is_hit:
				ships_hit +=1
		if ships_hit>=len(ships):
			self.is_lose=True
			print("Sorry, but you are loooose!!!")
		
		
		
		
#Class SHIP		
class ship:
	location = {}
	size = 0
	
	def __init__(self,location,size,is_hit = False):
		self.location = location
		self.size = size

name_player = input("Welcome to Battle Ship! Please, enter your name ")
player1 = player(name_player)

start_game = input("Starting new game? y/n ")
if start_game == "y":
	ship3_location = input("Enter your ship location with size 3 (directory with values from 1 to 5):  ")
	if type(ship3_location) is not dict:
		print(type(ship3_location))
		ship3_location = input("It's not location, try again. Location must be directory with values from 1 to 5 (for example {1:1,1:2,1:3}):  ")
	else:
	#if ship3_location.length() !=3:
	#	pass
		ship3 = ship(ship3_location,3)
		player.ships.append(ship3)
		print("Your ship location is "+player1.name)