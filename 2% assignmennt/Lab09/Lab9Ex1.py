from tkinter import * 
 
def draw_in_canvas(canvas):
	my_drawing = canvas
	my_drawing.create_polygon(50,100,125,25,200,100, fill = "blue" )
	
	
	
	my_drawing.create_rectangle(50,100,200,250, fill = "yellow")

	
	my_drawing.create_rectangle(50,100,100,150, fill = "white")
	my_drawing.create_rectangle(150,100,200,150, fill = "white")
	my_drawing.create_rectangle(100,175,150,250, fill = "blue"  )
	my_drawing.create_oval(110,210,115,215, fill = "white")
	my_drawing.create_line(50,100,100,150)
	my_drawing.create_line(50,150,100,100)
	my_drawing.create_line(150,100,200,150)
	my_drawing.create_line(150,150,200,100)
	my_font = ("Courier" , 12, "bold")
	my_drawing.create_text(125,260, text = "Mr Plod lives here.", font = my_font)
	
	
	
	
	
def draw_grid(a_canvas):
	grid_size = 50
	for row in range(50, 301, 50):
		a_canvas.create_line(-1, row, 251, row, fill = "lightblue")
	for column in range(50, 251, 50):
		a_canvas.create_line(column, -1, column, 301, fill = "lightblue")
		
def main(): 
	window = Tk()  
	window.title("Mr. Plod's House")  
	window.config(background = 'white')   
	window.geometry("250x300+10+20") 

	a_canvas = Canvas(window) 
	a_canvas.config(background = "white")   
	a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
	draw_grid(a_canvas)
	draw_in_canvas(a_canvas) 
	window.mainloop()   
 
main()
