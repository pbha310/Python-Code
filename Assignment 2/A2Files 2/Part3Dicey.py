"""
This program is used to test the three part 3 functions.
Complete the three functions.
The expected output is shown in the comment at the bottom of this file.

*** MAKE SURE YOU COPY YOUR PART 1 AND PART 2 FUNCTIONS INTO THIS PROGRAM ***
Author: Adriana Ferraro
"""

import random

#----------------------------------------------------------
# Main function - Testing Part 3 of assignment 2
#----------------------------------------------------------
def main():
	print("get_list_of_dice_rolls()")
	print("Note:  the dice values are random so your output will be different.")
	print()
	dice_rolls1 = get_list_of_dice_rolls(3) 
	dice_rolls2 = get_list_of_dice_rolls(1) 
	dice_rolls3 = get_list_of_dice_rolls(5) 
	dice_rolls4 = get_list_of_dice_rolls(4) 
	print("Should be a list of 3 random dice values:", dice_rolls1)
	print("Should be a list of 1 random dice value:", dice_rolls2)
	print("Should be a list of 5 random dice values:", dice_rolls3)
	print("Should be a list of 4 random dice values:", dice_rolls4)
	print("---------------------------")
	print("---------------------------")
	print("get_score()")
	score1 = get_score([4, 6, 6, 6, 6]) 
	score2 = get_score([4, 5, 6, 5, 6]) 
	score3 = get_score([6, 6, 2, 2, 2]) 
	score4 = get_score([5, 5, 6, 5, 5]) 
	score5 = get_score([6, 6, 6, 6, 6]) 
	score6 = get_score([6, 5, 1, 3, 2]) 
	print(score1, score2, score3, score4, score5, score6)
	print("---------------------------")
	print("---------------------------")
	print("Note:  the dice values are random so your output will be different.")
	print("Check that the scores are correct for the dice which are rolled.")
	print()
	print("process_player_turn()")
	player_score1 = process_player_turn("Adriana")
	print("Player score: ", player_score1)
	print()
	player_score2 = process_player_turn("Joe")
	print("Player score: ", player_score2)
	print("---------------------------")
	print("---------------------------")
#----------------------------------------------------------
# Functions which process a player's turn.
# Complete the following 3 functions below.
#----------------------------------------------------------
def get_list_of_dice_rolls(number_of_rolls):
	diceroll = []
	for num in range(number_of_rolls):
		diceroll.append(random.randrange(1,7))
	return(diceroll)


def get_score(list_of_dice):

	score =  get_max_number_of_matches(list_of_dice)
	if score == 0 or score ==2 or score ==1:
		return 0
	if score ==3:
		return 3
	if score ==4:
		return 4
	if score ==5:
		return 5
	
def process_player_turn(player_name):
    name= display_turn_info(player_name)
    list = get_list_of_dice_rolls(5)  
    display = display_dice(list)
    max = get_max_number_of_matches(list)
    if max > 2:
        display_number= get_dice_number_with_two_matches(list)
        new_list = [ list,list]
        two = display_exactly_two_matches_message(display_number)
        list_2 = get_list_of_dice_rolls(3)
        list += list_2
        score =  get_score(list)
        
     
        
    
    
	    
	    
	
	
#----------------------------------------------------------
# Functions from part 2
# which obtain the maximum number of matches and
# the dice number if there are exactly two matches
#----------------------------------------------------------
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
	
#----------------------------------------------------------
# Functions from part 1
#----------------------------------------------------------	
def display_turn_info(player_name):
	print(" ",player_name, "Turn")
	
def display_dice(list_of_dice):
	print("   ","Dice:", end=" ")
	for i in list_of_dice:
		print(i,end=" ")
	print()
	
def display_exactly_two_matches_message(dice_number):
	print("   "," Two ",dice_number,"'s. Roll the remaining 3 dice.",sep="")
	
main()

"""
EXPECTED OUTPUT FOR PART 3
get_list_of_dice_rolls()
Note:  the dice values are random so your output will be different.

Should be a list of 3 random dice values: [6, 4, 2]
Should be a list of 1 random dice value: [6]
Should be a list of 5 random dice values: [1, 4, 3, 5, 3]
Should be a list of 4 random dice values: [2, 1, 3, 3]
---------------------------
---------------------------
get_score()
4 0 3 4 5 0
---------------------------
---------------------------
Note:  the dice values are random so your output will be different.
Check that your scores are correct for the dice which are rolled.

process_player_turn()
  Adriana's turn
    Dice:  6 2 3 4 5
Player score:  0

  Joe's turn
    Dice:  5 2 6 1 2
    Two 2's. Roll the remaining 3 dice.
    Dice:  2 2 6 4 6
Player score:  0
---------------------------
---------------------------
"""

