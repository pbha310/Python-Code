"""
Upi:Pbha310
Id: 6691164
Description: tesselation arrangement of shapes closely fitted together
"""


from tkinter import *
# ------Draws one of the five different tiles.------
def draw_tile(a_canvas, tile_type, left, top, size):
 	colours = ["yellow","green","blue"," deepskyblue", "purple","red","orange","cyan"]
 	if tile_type == 1:
 		a_canvas.create_rectangle(left,top,left + size,  top + 2 * size, fill = colours[1], outline = "grey",width="2")
 		a_canvas.create_rectangle(left+size,top+size,left + 2 * size ,  top + 3 * size, fill = colours[1], outline = "grey",width="2")
 		a_canvas.create_rectangle(left+2*size,top+3*size,left + 3 * size ,top+2*size, fill = colours[1], outline = "grey",width="2")
 		a_canvas.create_line(left+2*size,top+3*size,left + 2 * size ,top+2*size, fill = colours[1],width="2")
 		a_canvas.create_line(left+1*size,top+size+1,left +1* size , top  + 2 * size-1 , fill = colours[1],width="2" )
 	elif tile_type ==2:
 		a_canvas.create_rectangle(left,top,left + 2 * size ,  top+size, fill = colours[2], outline = "grey",width="2")
 		a_canvas.create_rectangle(left+2*size,top,left + size,  top + 2 * size, fill = colours[2], outline = "grey",width="2")
 		a_canvas.create_rectangle(left+3*size,top+2*size,left + 2 * size ,  top+size, fill = colours[2], outline = "grey",width="2")
 		a_canvas.create_rectangle(left+3*size,top+3*size,left + 2 * size ,  top+size, fill = colours[2], outline = "grey",width="2")
 		a_canvas.create_line(left+1*size,top+1,left + size,  top + 1 * size-1, fill = colours[2],width="2")
 		a_canvas.create_line(left+2*size,top+2*size,left + 2 * size ,  top+size, fill = colours[2],width="2")
 	elif tile_type ==3:
 		a_canvas.create_rectangle(left,top,left + 1*size,  top + 2 * size, fill = colours[7], outline = "grey",width="2")
 		a_canvas.create_rectangle(left,top+size,left-size,  top + 3 * size, fill = colours[7], outline = "grey",width="2")
 		a_canvas.create_rectangle(left-size,top+2*size,left - 2 * size ,  top+3*size, fill = colours[7], outline = "grey",width="2")
 		a_canvas.create_line(left,top+size+1,left,  top + 2 * size-1, fill = colours[7],width="2")
 		a_canvas.create_line(left-size,top+2*size-1,left-size,  top + 3 * size-1, fill = colours[7],width="2")
 	elif tile_type ==4:
 		a_canvas.create_rectangle(left,top,left + 2 * size ,  top+size, fill = colours[4], outline = "grey",width="2")
 		a_canvas.create_rectangle(left,top,left+size,  top + 2 * size, fill = colours[4], outline = "grey",width="2")
 		a_canvas.create_rectangle(left,top+2*size,left - size ,  top+1*size, fill = colours[4], outline = "grey",width="2")
 		a_canvas.create_rectangle(left,top+3*size,left - size ,  top+1*size, fill = colours[4], outline = "grey",width="2")
 		a_canvas.create_line(left,top+size,left,  top + 2 * size, fill = colours[4],width="2")
 		a_canvas.create_line(left+size,top+1,left+size,  top + 1* size-1, fill = colours[4],width="2")
 	elif tile_type ==5:
 		a_canvas.create_rectangle(left,top,left +size ,  top+size, fill = colours[5], outline = "grey",width="2")

def process_single_line(a_canvas, line_of_pattern, left, top, size): 

	empty_case = 0	
	for character in line_of_pattern:
			empty_case += 1

			if character == "1":
					tile_type = int(character)
					
					draw_tile(a_canvas,tile_type, left+(empty_case*size-20),top,size)
			elif character == "2":
					tile_type = int(character)
					
					draw_tile(a_canvas,tile_type, left+(empty_case*size-20),top,size)
			elif character == "3":
					tile_type = int(character)
					
					draw_tile(a_canvas,tile_type, left+(empty_case*size-20),top,size)
			elif character == "4":
					tile_type = int(character)
					
					draw_tile(a_canvas,tile_type, left+(empty_case*size-20),top,size)
			elif character == "5":
					tile_type = int(character)
					
					draw_tile(a_canvas,tile_type, left+(empty_case*size-20),top,size)
			
# ------Organise the processing of the pattern. ------
def process_pattern(a_canvas, size):
 	left = size
 	top = size
 	list_of_lines = get_list_of_pattern_lines("TileMap.txt")
 	for line_string in list_of_lines:
 		process_single_line(a_canvas, line_string, left, top, size)
 		top += size
# ------Get the list of lines (strings) from the file. ------
def get_list_of_pattern_lines(filename):
 	file_to_read = open(filename, "r")
 	file_info = file_to_read.read()
 	lines_list = file_info.split("\n")
 	file_to_read.close()
 	return lines_list
# ------Draws the five tiles on the right side of the canvas. ------
def draw_five_tiles(a_canvas, left, top, size):
 	size = size * 3 // 4
 	large_rect = (left, top, left + size * 11, top + size * 12)
 	a_canvas.create_rectangle(large_rect, fill="Blue4", outline="SlateBlue1", width = 2)
 	left_size_multiply = [0, 1, 6, 3, 7, 1]
 	down_size_multiply = [0, 1, 1, 6, 6, 10]
 	for tile_type in range(1, 6):
 		left_value = left + size * left_size_multiply[tile_type]
 		top_value = top + size * down_size_multiply[tile_type]
 		draw_tile(a_canvas, tile_type, left_value, top_value, size)
# ------Draws the blue background grid lines of the given size. ------
def draw_grid(a_canvas, size, right_hand_side, bottom):
 	for row in range(size, bottom, size):
 		a_canvas.create_line(-1, row, right_hand_side + 1, row, fill="SlateBlue1")
 	for col in range(size, right_hand_side, size):
 		a_canvas.create_line(col, -1, col, bottom + 1, fill="SlateBlue1")
		
# ------main function. ------
def main():
 	size = 20
 	canvas_width = 700
 	canvas_height = 340
 	root = Tk()
 	root.title("A5- Pbha310")
 	geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
 	root.geometry(geometry_string)
 	a_canvas = Canvas(root)
 	a_canvas.config(background="SlateBlue1") #Uncomment when you have finished
 	a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window
 	#Draw the light blue background grid lines
 	draw_grid(a_canvas, size, canvas_width, canvas_height)
 	process_pattern(a_canvas, size)
 	draw_five_tiles(a_canvas, canvas_width - size * 3 // 4 * 12, size, size)
 	root.mainloop()
main()
