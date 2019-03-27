"""
Name: Prince Bhatia
Upi: Pbha310
Id number: 6691164
Description: Random dice game which matches 3 of a kind or more.
"""

import random

def main():

	round_number = 1
	player1_total_score = 0
	player2_total_score = 0
	player1_name = "Prince"
	player2_name = "kon"
	display = display_welcome()
	round_1_p1= process_player_turn(player1_name)
	round_1_p2= process_player_turn(player2_name)
	results_1= display_round_results(1,player1_name,round_1_p1,player2_name,round_1_p2)
	print()
	round_2_p1= process_player_turn(player1_name)
	round_2_p2= process_player_turn(player2_name)
	results_1= display_round_results(2,player1_name,(round_1_p1+round_2_p1),player2_name,(round_1_p2+round_2_p2))
	print()
	round_3_p1= process_player_turn(player1_name)
	round_3_p2= process_player_turn(player2_name)
	results_1= display_round_results(3,player1_name, (round_2_p1+round_3_p1+round_1_p1),player2_name,(round_2_p2+round_1_p2+round_3_p2))
	print()
	final_result = display_final_results(player1_name,(round_2_p1+round_3_p1+round_1_p1),player2_name,(round_2_p2+round_1_p2+round_3_p2))

	
	
	
	

def get_list_of_dice_rolls(number_of_rolls):
	diceroll = []
	for num in range(number_of_rolls):
		diceroll.append(random.randrange(1,7))
	return(diceroll)


def get_score(list_of_dice):

	score =  get_max_number_of_matches(list_of_dice)
	if score == 0:
	    return 0
	if score ==1:
	    return 1
	if score ==2:
	    return 2
	if score ==3:
		return 3
	if score ==4:
		return 4
	if score ==5:
		return 5
	
def process_player_turn(player_name):
    name= display_turn_info(player_name)
    list = get_list_of_dice_rolls(5) 
    two_matches = get_dice_number_with_two_matches(list)
    display = display_dice(list)
    
    two_matches_values = get_how_many_match(two_matches, list)
    
    if two_matches_values == 2:
        
            list = [two_matches,two_matches]
            list += get_list_of_dice_rolls(3)
            score =  get_score(list)
            display = display_exactly_two_matches_message(two_matches)
            display = display_dice(list)
    max_rolls = get_max_number_of_matches(list)
    if max_rolls >=3:
        final_score = max_rolls
    else:
        final_score=0
    return final_score
			
		
		
		

	
def get_how_many_match(value_to_match, list_of_dice):
	list = []
	for dice in list_of_dice:
		if value_to_match == dice:
			list.append(dice)
	return len(list)
	
def get_dice_number_with_two_matches(list_of_dice):
	
	for dice in range(len(list_of_dice)):
		if get_how_many_match(list_of_dice[dice],list_of_dice) == 2:
			dice = list_of_dice[dice]
			return(dice)
	
def get_max_number_of_matches(list_of_dice):
	match = []
	for dice in list_of_dice:
	    matches = get_how_many_match(dice, list_of_dice)
	    match.append(matches)
	return max(match)
		

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
		name = str(player1_name)
		result2 = "Congratulations to " + name
		
		number2 = len(result2)
		print("*"*number2)
		print(result2)
		print("*"*number2,'\n')

	

	elif player2_score > player1_score:
		name2 = str(player2_name)
		result3 = "Congratulations to " + name2
		number3 = len(result3)
		print("*"*number3)
		print(result3)
		print("*"*number3,'\n')	
main()

