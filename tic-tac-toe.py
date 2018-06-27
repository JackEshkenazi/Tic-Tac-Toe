from turtle import Turtle
import random
line = Turtle()
line.speed(25)

def board(size):

	line.forward(300 *size)
	line.penup()
	line.goto(300*size,100 *size)
	line.pendown()
	line.backward(300 * size)
	line.penup()
	line.goto(100*size, 200 *size)
	line.right(90)
	line.pendown()
	line.forward(300 * size)
	line.penup()
	line.goto(200 *size,-100 *size)
	line.pendown()
	line.backward(300 * size)
	
board(1)

board_contents = ["1","2","3","4","5","6","7","8","9"]
You = []
Computer = []

shape = input("Are you x's or o's?")
while shape not in "xoOX":
	print("try again")
	shape=input()
	
	
if shape == "x" or shape == "X":
		mySymbol=1
		compSymbol=2
elif shape =="o" or shape =="O":
	mySymbol=2
	compSymbol=1
	
	
def circle(x,y, symbol):

	if symbol == 1:
		line.penup()
		line.goto(x,y)
		y = y+50
		line.goto(x,y)
		line.pendown()
		x = x+100
		y = y-100
		line.goto(x,y)
		line.penup()
		line.backward(100)
		x = x -100
		line.pendown()
		line.goto(x,y)

	else:
		line.penup()
		line.goto(x, y)
		line.pendown()
		line.circle(50)

def myMove():
	
	print("Type the square number. Available squares are:")
	move1 = input(board_contents )
	
	while move1 not in board_contents:
		print("Try again")
		move1=input()
	
	board_contents.remove(move1)
	You.append(move1)
	
	if move1 == "1":
		circle(0, 150, mySymbol)
	elif move1 == "2":
		circle(100, 150, mySymbol)
	elif move1 == "3":
		circle(200, 150, mySymbol)
	elif move1 == "4":
		circle(0, 50, mySymbol)
	elif move1 == "5":
		circle(100, 50, mySymbol)
	elif move1 == "6":
		circle(200, 50, mySymbol)
	elif move1 == "7":
		circle(0, -50, mySymbol)
	elif move1 == "8":
		circle(100, -50, mySymbol)
	elif move1 == "9":
		circle(200, -50, mySymbol)
	return move1

def nextMoveWin(a,b,c, listyy):
	posibillity = [a,b,c]
	y = set(listyy).intersection(posibillity)
		
	if len(y) == 2:
		if a not in listyy:
			return a
		elif b not in listyy:
			return b
		elif c not in listyy:
			return c
	else:
		return("NOPE")

def computerMove(x):
	
	if mySymbol ==2 and board_contents == ["1","2","3","4","5","6","7","8","9"]:
		circle(100, 50, compSymbol)
		board_contents.remove("5")
		Computer.append("5")
		print("5")
		
	elif x in ("12346789") and len(board_contents)==8:
		circle(100, 50, compSymbol)
		board_contents.remove("5")
		Computer.append("5")
		print("5")
			
	else:
		move2 = "void"
		
		option = nextMoveWin("1", "2", "3", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("1", "4", "7", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("4", "5", "6", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("2", "5", "8", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("7", "8", "9", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("3", "6", "9", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("1", "5", "9", You)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("7", "5", "3", You)
		if len(option) == 1:
			move2 = option
		
		option = nextMoveWin("1", "2", "3", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("1", "4", "7", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("4", "5", "6", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("2", "5", "8", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("7", "8", "9", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("3", "6", "9", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("1", "5", "9", Computer)
		if len(option) == 1:
			move2 = option
		option = nextMoveWin("7", "5", "3", Computer)
		if len(option) == 1:
			move2 = option
		
		if move2 not in board_contents:
			move2 = random.choice(board_contents)
		
		board_contents.remove(move2)
		Computer.append(move2)

		if move2 == "1":
			circle(0, 150, compSymbol)
		elif move2 == "2":
			circle(100, 150, compSymbol)
		elif move2 == "3":
			circle(200, 150, compSymbol)
		elif move2 == "4":
			circle(0, 50, compSymbol)
		elif move2 == "5":
			circle(100, 50, compSymbol)
		elif move2 == "6":
			circle(200, 50, compSymbol)
		elif move2 == "7":
			circle(0, -50, compSymbol)
		elif move2 == "8":
			circle(100, -50, compSymbol)
		elif move2 == "9":
			circle(200, -50, compSymbol)
		print(move2)
		

def checkWinner(YouComputer):
	
	if "1" in YouComputer and "2" in YouComputer and "3" in YouComputer:
		return("win!")
	elif "4" in YouComputer  and "5" in YouComputer and "6" in YouComputer:
		return("win!")
	elif "7" in YouComputer  and "8" in YouComputer and "9" in YouComputer:
		return("win!")
	elif "1" in YouComputer  and "4" in YouComputer and "7" in YouComputer:
		return("win!")
	elif "2" in YouComputer  and "5" in YouComputer and "8" in YouComputer:
		return("win!")
	elif "3" in YouComputer  and "6" in YouComputer and "9" in YouComputer:
		return("win!")
	elif "1" in YouComputer  and "5" in YouComputer and "9" in YouComputer:
		return("win!")
	elif "3" in YouComputer  and "5" in YouComputer and "7" in YouComputer:
		return("win!")

	
def game():
	while mySymbol == 1:
		x = myMove()
		checkWinner(You)
		if checkWinner(You) == "win!":
			print("You win!")
			break
			
		elif board_contents == []:
			print("It's a tie")
			break
		computerMove(x)
		checkWinner(Computer)
		if checkWinner(Computer) == "win!":
			print("Computer wins!")
			break
		elif board_contents == []:
			print("It's a tie")
			break
	
	while mySymbol == 2:
		if board_contents == ["1","2","3","4","5","6","7","8","9"]:
			x = "nothing here"
			computerMove(x)
			myMove()
	
		else:
			computerMove(x)
			checkWinner(Computer)
			if checkWinner(Computer) == "win!":			
				print("Computer wins!")
				break

			elif board_contents == []:
				print("It's a tie")
				break

			x = myMove()
			checkWinner(You)
			if checkWinner(You) == "win!":
				print("You win!")
				break

game()