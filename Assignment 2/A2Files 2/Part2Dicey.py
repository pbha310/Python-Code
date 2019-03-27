"""
This program is used to test the three part 2 functions.
Complete the three functions.
The expected output is shown in the comment at the bottom of this file.
Author: Adriana Ferraro
"""

#----------------------------------------------------------
# Main function - Testing Part 2 of assignment 2
#----------------------------------------------------------
def main():
	print("get_how_many_match()")
	num_matches1 = get_how_many_match(2, [5, 2, 2, 5, 2]) 
	num_matches2 = get_how_many_match(5, [5, 2, 2, 5, 2]) 
	num_matches3 = get_how_many_match(4, [5, 2, 2, 5, 2]) 
	num_matches4 = get_how_many_match(3, [5, 3, 4, 3, 3]) 
	num_matches5 = get_how_many_match(6, [5, 2, 2, 6, 2]) 
	print(num_matches1, num_matches2, num_matches3, num_matches4, num_matches5)
	print("---------------------------")
	print("---------------------------")
	print("get_dice_number_with_two_matches()")
	two_matches1 = get_dice_number_with_two_matches([4, 5, 6, 5, 2]) 
	two_matches2 = get_dice_number_with_two_matches([4, 5, 3, 4, 2]) 
	two_matches3 = get_dice_number_with_two_matches([3, 3, 5, 4, 2])  
	two_matches4 = get_dice_number_with_two_matches([4, 5, 3, 2, 2]) 
	two_matches5 = get_dice_number_with_two_matches([4, 6, 6, 4, 2]) 
	print(two_matches1, two_matches2, two_matches3, two_matches4, two_matches5)
	print("---------------------------")
	print("---------------------------")
	print("get_max_number_of_matches()")
	max_matches1 = get_max_number_of_matches([4, 5, 6, 5, 2]) 
	max_matches2 = get_max_number_of_matches([4, 5, 3, 4, 2]) 
	max_matches3 = get_max_number_of_matches([3, 1, 2, 4, 5])  
	max_matches4 = get_max_number_of_matches([4, 5, 6, 5, 2]) 
	max_matches5 = get_max_number_of_matches([4, 5, 2, 5, 5]) 
	print(max_matches1, max_matches2, max_matches3, max_matches4, max_matches5)
	print("---------------------------")
	print("---------------------------")

#----------------------------------------------------------
# Functions which obtain the maximum number of matches and
# the dice number if there are exactly two matches
# Complete the following 3 functions below.
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

			

			

		
	


			


main()

"""
EXPECTED OUTPUT FOR PART 2
get_how_many_match()
3 2 0 3 1
---------------------------
---------------------------
get_dice_number_with_two_matches()
5 4 3 2 4
---------------------------
---------------------------
get_max_number_of_matches()
2 2 1 2 3
---------------------------
---------------------------
"""

