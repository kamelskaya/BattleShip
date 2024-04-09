
import random
computer_looser = False
computer_hits = []

##Класс PLAYER с набором кораблей
class player:
	ships = []
	is_lose = False
	def __init__(self,name):
		self.name = name
		
	def player_hit(self,location):
		ship_hit = False
		for ship in self.ships:
			for loc in ship.location:
				if location == loc:
					ship_hit = True
					ship.is_hit = True
					print("BUUUUUUUUUUUUUUUHHHHHHHHHH!!!! Your ship {} sunk!!".format(location))
		
		if ship_hit:
			count_ships_hit = 0	
			for ship in self.ships:
				if ship.is_hit:
					count_ships_hit +=1
			if count_ships_hit>=len(self.ships):
				self.is_lose=True
				print("Sorry, but you are loooose!!!")
				exit()	
		else:
			print("NO, computer is missed in location {}".format(location))
			
		
#Class SHIP		
class ship:
	location = []
	size = 0
	is_hit = False
	
	def __init__(self,location,size):
		self.location= location
		self.size = size
 
def entering_location():
	ship1_locationstr = input("Enter your ship location (like ¨1:2¨ with values from 1 to 5):  ")
	ship1_location = ship1_locationstr.split(":")
	attemps = 0
	while (len(ship1_location)!=2):
		if attemps>=3:
			print("You can't location your ships. Game over")
			return False
		ship1_locationstr = input("It's not location, try again. Location must be two numbers with : (for example 1:3):  ")
		ship1_location = ship1_locationstr.split(":")	
		attemps+=1
		
	return ship1_locationstr
 
 
#Creating new ship (for player) 
def new_ship(size=1):
	list_location =[]
	if size==1:
	
		location = entering_location() 
		list_location.append(location)
		if location == False:
			return False
	
		ship1 = ship(list_location,1)		
	if size==2:
		location = entering_location() 
		if location == False:
			return False
		list_location.append(location)
		
		location = entering_location() 
		if location == False:
			return False
		list_location.append(location)
		ship1 = ship(list_location,2)
	return ship1

#PLAYER HIT	
def players_hit():
	hit_locationstr = input("Your hit! Write location to hit computer (two numbers with ':' for example 1:3)")
	hit_location = hit_locationstr.split(":")
	attemps = 0
	while (len(hit_location)!=2):
		if attemps>=3:
			print("You can't hit")
			return False
		hit_locationstr = input("It's not location, try again. Location must be two numbers with : (for example 1:3):  ")
		hit_location = hit_locationstr.split(":")	
		attemps+=1
	
	#Check if the player sank the computer ship
	was_sank = False
	for computer_ship in computer_ships:
		for loc in computer_ship.location:
			if hit_locationstr == loc:
				print("BUUUUUUUUUUUUUUUHHHHHHHHHH!!!! You sank in ship!!")
				computer_ship.is_hit = True
				was_sank = True
			
	#Check if computer looses
	if was_sank == True:
		ships_hit = 0
		for computer_ship in computer_ships:
			if computer_ship.is_hit == True:
				ships_hit +=1
		if ships_hit>=len(computer_ships):
				print("You win!!!")	
				computer_looser = True
	else:
		print("NO, you a missed")

#COMPUTER HIT	
def computer_hit(player):
	input("Now hit of computer! Are you ready?")
	hit_locationstr = str(random.randint(1, 5)) + ":"+str(random.randint(1, 5))
	while hit_locationstr in computer_hits:
		hit_locationstr = str(random.randint(1, 5)) + ":"+str(random.randint(1, 5))
	
	player.player_hit(hit_locationstr)
	computer_hits.append(hit_locationstr)



#################
##NEW GAME
name_player = input("Welcome to Battle Ship! Please, enter your name ")
player1 = player(name_player)

start_game = input("Starting new game? y/n ")
if start_game == "y":
	computer_looser = False

	#Create ships for computer
	computer_ships = []
	#Ship size 1
	ship_location = []
	ship_location.append(str(random.randint(1, 5)) + ":"+str(random.randint(1, 5)))
	computer_ship1 = ship(ship_location,1)	
	
	#Ship size 1
	ship_location = []
	ship_location.append(str(random.randint(1, 5)) + ":"+str(random.randint(1, 5)))
	computer_ship2 = ship(ship_location,1)	
	
	#Ship size 2
	ship_location = []
	ship_location.append(str(random.randint(1, 5)) + ":"+str(random.randint(1, 5)))
	ship_location.append(str(random.randint(1, 5)) + ":"+str(random.randint(1, 5)))
	computer_ship3 = ship(ship_location,2)	
	

	computer_ships.append(computer_ship1)
	computer_ships.append(computer_ship2)
	computer_ships.append(computer_ship3)
	print("Computer ships with location {0},{1},{2}".format(computer_ship1.location,computer_ship2.location,computer_ship3.location))
	
	#Create ships for player
	ship1 = new_ship()
	if ship1==False:
		exit()
	ship2 = new_ship()
	if ship2==False:
		exit()
	ship3 = new_ship(2)
	if ship3==False:
		exit()
	
	player.ships.append(ship1)
	player.ships.append(ship2)
	player.ships.append(ship3)
	#player.ships.append(ship4)
	print("Player ships with location {0},{1},{2}".format(ship1.location,ship2.location,ship3.location))
	
	players_hit()
	computer_hit(player1)
	attemps=0
	while (computer_looser==False and player1.is_lose==False):	
		print(computer_looser)
		players_hit()
		computer_hit(player1)
		if attemps>=3:
			print("You can't win. Game over")
			exit()
		attemps+=1	
		
	