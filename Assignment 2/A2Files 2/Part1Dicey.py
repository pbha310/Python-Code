"""
This program is used to test the six part 1 functions.
Complete the six functions.
The expected output is shown in the comment at the bottom of this file.
Author: Adriana Ferraro
"""

#----------------------------------------------------------
# Main function - Testing Part 1 of assignment 2
#----------------------------------------------------------
def main():
	print("display_welcome()")
	display_welcome()
	print("---------------------------")
	print("---------------------------")
	print("display_turn_info()")
	display_turn_info("Harry")
	display_turn_info("Joe")
	print("---------------------------")
	print("---------------------------")
	print("display_dice()")
	display_dice([2, 2, 4, 6, 3])
	display_dice([3, 6, 4, 3, 5])
	display_dice([2, 6, 4, 6])
	print("---------------------------")
	print("---------------------------")
	print("display_exactly_two_matches_message()")
	display_exactly_two_matches_message(4)
	display_exactly_two_matches_message(1)
	print("---------------------------")
	print("---------------------------")
	print("display_round_results()")
	display_round_results(2, "Adriana", 6, "Bruno", 7) 
	display_round_results(1, "Jim", 4, "Jill", 3) 
	print("---------------------------")
	print("---------------------------")
	print("display_final_results()")
	display_final_results("Fred", 9, "Hilbert", 10)
	display_final_results("Erica", 9, "Edward", 9)
	display_final_results("Jerry", 15, "Jordan", 0)
	print("---------------------------")
	print("---------------------------")
#----------------------------------------------------------
# All the functions which print information to the 
# standard output window.  
# Complete the following 6 functions below.
#----------------------------------------------------------
def display_welcome():
	print()
	print("Welcome to DICEY, written by Pbha310")
	print()
	
def display_turn_info(player_name):
	print(" ",player_name, "Turn")
	
def display_dice(list_of_dice):
	print("   ","Dice:", end=" ")
	for i in list_of_dice:
		print(i,end=" ")
	print()
	
def display_exactly_two_matches_message(dice_number):
	print("   "," Two ",dice_number,"'s. Roll the remaining 3 dice.",sep="")
	
def display_round_results(round_number, player1_name, player1_score, player2_name, player2_score):
	print("Round",round_number, "results:",player1_name, "has",player1_score,"points, and",player2_name,"has",player2_score,"points")
	print()

def display_final_results(player1_name, player1_score, player2_name, player2_score):
	print()
	if player1_score == player2_score:
		result = "The result is a tie"
		number = len(result)
		print("*"*number)
		print(result)
		print("*"*number,'\n')

	elif player2_score < player1_score:
		result2 = "Congratulations to Jerry"
		number2 = len(result2)
		print("*"*number2)
		print(result2)
		print("*"*number2,'\n')

	

	elif player2_score > player1_score:
		result3 = "Congratulations to Hilbert"
		number3 = len(result3)
		print("*"*number3)
		print(result3)
		print("*"*number3,'\n')

main()

"""
EXPECTED OUTPUT FOR PART 1
display_welcome()

Welcome to DICEY, written by afer023

---------------------------
---------------------------
display_turn_info()
  Harry's turn
  Joe's turn
---------------------------
---------------------------
display_dice()
    Dice:  2 2 4 6 3
    Dice:  3 6 4 3 5
    Dice:  2 6 4 6
---------------------------
---------------------------
display_exactly_two_matches_message()
    Two 4's. Roll the remaining 3 dice.
    Two 1's. Roll the remaining 3 dice.
---------------------------
---------------------------
display_round_results()
Round 2 results: Adriana has 6 points, and Bruno has 7 points

Round 1 results: Jim has 4 points, and Jill has 3 points

---------------------------
---------------------------
display_final_results()

**************************
Congratulations to Hilbert
**************************


*******************
The result is a tie
*******************


************************
Congratulations to Jerry
************************

---------------------------
---------------------------
"""
