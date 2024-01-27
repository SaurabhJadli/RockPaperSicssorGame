import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random

# main window object
root = Tk()

# Title of GUI window
root.title('Rock Paper Scissor Game.')
#root.iconbitmap('@/home/suu/Desktop/py/default.XBM')

# Window size
root.geometry('800x680')

# Canvas
canvas = Canvas(root, width=800, height=680, bg='cyan')
canvas.grid(row=0, column=0)

# Creating labels for text display
l1 = Label(root, text='Player', font=('Arial', 25), bg='cyan')
l2 = Label(root, text='Computer', font=('Algerian', 25), bg='cyan')
l3 = Label(root, text='Vs', font=('Algerian', 40, "bold"), bg='cyan')

# Placing all the labels on window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

# Default image for Game
img_p = Image.open("default.png")
img_p = img_p.resize((300, 300))

# Flipping image from left to right
img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

# Rock image
rock_p = Image.open('rock.png')
rock_p = rock_p.resize((300, 300))

# Flipping image from left to right
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

# Paper image
paper_p = Image.open('paper.png')
paper_p = paper_p.resize((300, 300))

# Flipping image from left to right
paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

# Scissor image
scissor_p = Image.open('scissor.png')
scissor_p = scissor_p.resize((300, 300))

# Flipping image from left to right
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

# Selection image
img_s = Image.open("Selection.png")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

# Putting image on canvas on specific coordinates
canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)


# game function
def game(player):
	select = [1, 2, 3]
	
	# Randomly selects no. for computer
	computer = random.choice(select)

	# Setting image for player on canvas
	if player == 1:
	
		# Puts rock image on canvas
		canvas.create_image(0, 100, anchor=NW, image=rock_p)
	elif player == 2:
		
		# Puts paper image on canvas
		canvas.create_image(0, 100, anchor=NW, image=paper_p)
	else:
		
		# Puts scissor image on canvas
		canvas.create_image(0, 100, anchor=NW, image=scissor_p)

	# Setting image for computer on canvas
	if computer == 1:
		
		# Puts rock image on canvas
		canvas.create_image(500, 100, anchor=NW, image=rock_c)
	elif computer == 2:
		
		# Puts paper image on canvas
		canvas.create_image(500, 100, anchor=NW, image=paper_c)
	else:
		
		# Puts scissor image on canvas
		canvas.create_image(500, 100, anchor=NW, image=scissor_c)

	# Obtaining result by comparison
	if player == computer: # Case of DRAW
		res = 'Draw'
		
	# Case of player's win
	elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
		res = 'You won'
	
	# Case of computer's win
	else:
		res = 'Computer won'

	# Putting result on canvas
	canvas.create_text(390, 600, text='Result:- ' + res,
					fill="black", font=('Algerian', 25), tag='result')


# Function for clear button
def reset():

	# Removes result from canvas
	canvas.delete('result')

	# Puts default image on canvas
	canvas.create_image(0, 100, anchor=NW, image=img_p)
	canvas.create_image(500, 100, anchor=NW, image=img_c)
 
def clearR():
    canvas.delete('result')


# Button for selecting rock
rock_b = Button(root, text='Rock', command=lambda: [clearR(), game(1)], bg='brown')
rock_b.place(x=27, y=487)

# Button for selecting paper
paper_b = Button(root, text='Paper', command=lambda: [clearR(), game(2)], bg='white')
paper_b.place(x=120, y=487)

# Button for selecting scissor
scissor_b = Button(root, text='Scissor', command=lambda: [clearR(), game(3)], bg='blue')
scissor_b.place(x=220, y=487)

# Button for clear
reset_b = Button(root, text='RESET', font=('Times', 10, 'bold'),
				width=10, command=reset, bg='orange', activebackground='red').place(x=370, y=28)

# Exit button
exit_b = Button(root, text='EXIT', font=('Times', 10, 'bold'),
				width=10, command=root.quit, bg='red', activebackground='red').place(x=30, y=640)

l4 = Label(root, text='Creator: Saurabh Jadli', font=('Algerian', 10), bg='cyan')
l4.place(x=630, y=640)

root.mainloop()
