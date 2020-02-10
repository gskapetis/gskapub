# DESCRIPTION
# ###########
# This is the simple game of tic tac toe coded in python.
# The first player select the symbol (X or O) that is going to use.
# After end of game by win or draw, player select if he/she wants to play again.


MY_X_POINTS = []
MY_O_POINTS = []
MY_UPDATED_BOARD = [MY_X_POINTS, MY_O_POINTS]


def user_x_or_o(player_num):
	print ("Hello Player No {}".format(player_num))
	user_selection_choice = input("Please select X or O: ")
	while user_selection_choice != "X" and user_selection_choice != "O":
		user_selection_choice = input("Invalid input. Please select X or O: ")

	#print("Player {} selcted {}".format(player_num, user_selection_choice))
	#myplayer_selection = [player_num, user_selection_choice]
	return user_selection_choice


def print_current_state_of_map(X_places, O_places):
	# myX = "X"
	# myO = "O"

	MY_UPDATED_BOARD = [[], []]

	pos1 = " "
	pos2 = " "
	pos3 = " "
	pos4 = " "
	pos5 = " "
	pos6 = " "
	pos7 = " "
	pos8 = " "
	pos9 = " "

	for x in X_places:
		if x == 1:
			pos1 = "X"
		if x == 2:
			pos2 = "X"
		if x == 3:
			pos3 = "X"
		if x == 4:
			pos4 = "X"
		if x == 5:
			pos5 = "X"
		if x == 6:
			pos6 = "X"
		if x == 7:
			pos7 = "X"
		if x == 8:
			pos8 = "X"
		if x == 9:
			pos9 = "X"


	for y in O_places:
		if y == 1:
			pos1 = "O"
		if y == 2:
			pos2 = "O"
		if y == 3:
			pos3 = "O"
		if y == 4:
			pos4 = "O"
		if y == 5:
			pos5 = "O"
		if y == 6:
			pos6 = "O"
		if y == 7:
			pos7 = "O"
		if y == 8:
			pos8 = "O"
		if y == 9:
			pos9 = "O"

	myline5 = [pos7, "|", pos8,"|", pos9, "\n"]
	myline4 = ["-", "-", "-","-", "-", "\n"]
	myline3 = [pos4, "|", pos5,"|", pos6, "\n"]
	myline2 = ["-", "-", "-","-", "-", "\n"]
	myline1 = [pos1, "|", pos2,"|", pos3, "\n"]

	myline1 = "".join(myline1)
	myline2 = "".join(myline2)
	myline3 = "".join(myline3)
	myline4 = "".join(myline4)
	myline5 = "".join(myline5)
 	
	mynum = myline5+myline4+myline3+myline2+myline1

	
	print(mynum)		


def my_read_choice(player, my_X_or_O):
	print(">>> Hello Player No {}".format(player))
	position = input("Player {} please give me your choice: ".format(player))
	while position not in ["1","2","3","4","5","6","7","8","9"]:
		position = input(">>> Invalid position. Player {} please give me another position: ".format(player))

	position = int(position)

	while position in MY_O_POINTS or position in MY_X_POINTS or position not in range(1,10) :
		 position = int(input(">>> Invalid position. Player {} please give me another position: ".format(player)))
	
	
	if my_X_or_O == "X":
		MY_X_POINTS.append(position)
		MY_X_POINTS.sort()
	else :
		MY_O_POINTS.append(position)
		MY_O_POINTS.sort()

	print(MY_X_POINTS)
	print(MY_O_POINTS)


def is_inlcuded(A, B): 
    
	result =  all(elem in B  for elem in A)
	if result:
		return True
	else:
		return False
    

def my_is_win_or_draw(my_x, my_o):
	myresult = ""

	if is_inlcuded([1,2,3],my_x) == True or is_inlcuded([4,5,6],my_x) == True  or is_inlcuded([7,8,9],my_x) == True or is_inlcuded([1,4,7],my_x) == True or is_inlcuded([2,5,8],my_x) == True or is_inlcuded([3,6,9],my_x) == True or is_inlcuded([1,5,9],my_x) == True or is_inlcuded([3,5,9],my_x) == True or is_inlcuded([3,5,7],my_x) == True :
		myresult = "WIN"
		print("You WON !!! :) ")
	elif is_inlcuded([1,2,3],my_o) == True or is_inlcuded([4,5,6],my_o) == True or is_inlcuded([7,8,9],my_o) == True or is_inlcuded([1,4,7],my_o) == True or is_inlcuded([2,5,8],my_o) == True or is_inlcuded([3,6,9],my_o) == True or is_inlcuded([1,5,9],my_o) == True or is_inlcuded([3,5,9],my_o) == True or is_inlcuded([3,5,7],my_o) == True :
		myresult = "WIN"
		print("You WON!!! :)")
	elif (len(my_x) == 4 and len(my_o) ==5) or (len(my_x) == 5 and len(my_o) ==4) and myresult != "WIN":
		myresult = "DRAW"
		print("This is a DRAW!")
	else:
		myresult = "NONE"

	return myresult	




def play_again():
	myinput = input("Play again? (Y/N): ")
	print("My input play again: {}".format(myinput))
	if myinput.lower() == "y" or myinput.lower() == "yes":
		return True
	elif myinput.lower() == "n" or myinput.lower() == "no":
		return False
	else:
		print("No valid choice. Terminating ...")
		return False

###### MAIN #######

PLAY_AGAIN = True
MY_RESULT = "NONE"

while PLAY_AGAIN == True:
	user1_XORO_choice = ""
	user2_XORO_choice = ""
	
	user1_XORO_choice = user_x_or_o(1)

	if user1_XORO_choice == "X":
		user2_XORO_choice = "O"
	else:
		user2_XORO_choice = "X"

	print_current_state_of_map(MY_X_POINTS, MY_O_POINTS)

	myturn = False # player 1 plays when myturn = False
	while MY_RESULT != "WIN" and MY_RESULT != "DRAW":	
		if myturn == False:
			my_read_choice(1, user1_XORO_choice)
			print_current_state_of_map(MY_X_POINTS, MY_O_POINTS)
			myturn = True
		else:
			my_read_choice(2, user2_XORO_choice)
			print_current_state_of_map(MY_X_POINTS, MY_O_POINTS)
			myturn = False
		MY_RESULT = my_is_win_or_draw(MY_X_POINTS, MY_O_POINTS)

	PLAY_AGAIN = play_again()	
	




