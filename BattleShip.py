##Класс PLAYER с набором кораблей
class player:
	ships = []
	is_lose = False
	def __init__(self,name):
		self.name = name
		
	def player_hit(self,location):
		for ship in ships:
			if location in ship.location:
				ship_hit = True
		is_player_lose(self)
			
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
 
def new_ship(size=1):
	ship1_locationstr = input("Enter your ship location with size 1 (like ¨1:2¨ with values from 1 to 5):  ")
	ship1_location = ship1_locationstr.split(":")
	attemps = 0
	while (len(ship1_location)!=2):
	
		ship1_locationstr = input("It's not location, try again. Location must be two numbers with : (for example 1:3):  ")
		ship1_location = ship1_locationstr.split(":")	
		attemps+=1
		print("{0} / {1}".format(ship1_location,len(ship1_location)))
	if attemps>3:
		print("You can't location your ships. Game over")
		return False
	ship1 = ship(ship1_location,1)		
	print("Created new ship")
	return ship1

##NEW GAME
name_player = input("Welcome to Battle Ship! Please, enter your name ")
player1 = player(name_player)

start_game = input("Starting new game? y/n ")
if start_game == "y":
	##Create ships for player
	ship1 = new_ship()
	if ship1==False:
		exit()
	ship2 = new_ship()
	if ship2==False:
		exit()
	ship3 = new_ship()
	if ship3==False:
		exit()
	ship4 = new_ship()
	if ship4==False:
		exit()
	player.ships.append(ship1)
	player.ships.append(ship2)
	player.ships.append(ship3)
	player.ships.append(ship4)
	print("You have {} ships".format(len(player1.ships)))
	
	