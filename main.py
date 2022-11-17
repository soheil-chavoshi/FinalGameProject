############################################
#LIBRARIES AND VARIABLES
############################################

from tkinter import *
from time import *
from random import*
#from PIL import Image, ImageTk

#Tkinter setup
root = Tk()
s = Canvas(root, width=400,height=400, background="#2b0f59")


#Variables
velocity_x = 0 
velocity_y = 0
player_speed = 199
player_x = 200
player_y = 200

#Level 0 is startup, 1+ is gameplay, -1 is gameover
Level = 1
Score = 0

###########################################
#Functions
###########################################

def input_up_handler(event):

	global velocity_x
	global velocity_y
	
	if event.keysym == "d" or event.keysym == "a":
		velocity_x = 0

	if event.keysym == "w" or event.keysym == "s":
		velocity_y = 0
		

def input_down_handler(event):

	global Level
	if Level == 0:
		if event.keysym == "space":
			Level = 1

	if Level >= 1:
		
		global velocity_x
		global velocity_y
		
		if event.keysym == "d":
			velocity_x = -1
		elif event.keysym == "a":
			velocity_x = 1

		if event.keysym == "w":
			velocity_y = 1
		elif event.keysym == "s":
			velocity_y = -1

def start_game():
	
	print(0)
	global Level

	title = s.create_rectangle(0,0,400,400,fill="black")

	while Level == 0:

		s.update()
		sleep(0.1)

	s.delete(title)

	#time elapsed between every frame
	delta = 0
	previous_frame_time = 0
	player_img = PhotoImage(img)
	
	while Level >= 1:
		print(Level)
		delta = previous_frame_time - time()
		previous_frame_time = time()
		
		global player_x, player_y
		
		global velocity_x
		global velocity_y
		global player_speed
		size = 10

		#Create player
		player = s.create_image(player_x,player_y, image=player_img)

		s.update()
		
		yield
		
		s.delete(player)

		#Move player position

		player_x += velocity_x * player_speed * delta
		player_y += velocity_y * player_speed * delta


		#Out of boundary player movement
		if player_x >= 400:
			player_x = 0
		if player_y >= 400:
			player_y = 0

		if player_x+size <= 0:
			player_x = 400
		if player_y+size <= 0:
			player_y = 400
		

		sleep(0.02)

###########################################
#Game/Tkinter setup
###########################################
print(Level)
root.after(0, start_game)
#root.title("Final Game Project #TBD#")

s.bind( "<Key>", input_down_handler)
s.bind( "<KeyRelease>", input_up_handler) 

s.pack()
s.focus_set()