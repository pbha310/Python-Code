## COMPSCI 105 - Summer, 2017
## Author: <<put your name here>>

class Polynomial:

    def __init__(self):
        self.list_of_coefficient = []
        self.list_of_exponent = []

    def __str__(self):
        count = 0
        new_string = ""
        dic = {}
        for value in range(len(self.list_of_coefficient)):
            dic[self.list_of_exponent[value]] = self.list_of_coefficient[value]
        self.list_of_exponent.sort(reverse=True)
        coeff_sorted = []
        for value in self.list_of_exponent:
            coeff_sorted += [dic[value]]
        self.list_of_coefficient = coeff_sorted
        if self.list_of_coefficient == []:
            new_string = '0'
        else:
            if str(self.list_of_coefficient[0])[0] == "-":
                    new_string += "-"+ str(self.list_of_coefficient[0])[1:]
            elif str(self.list_of_coefficient[0]) == '0':
                count = 1       
            elif (self.list_of_coefficient[0]) == 1:
                new_string += ''
            elif (self.list_of_coefficient[0]) == -1:
                new_string += '-'
            else:
                new_string += str(self.list_of_coefficient[0])
            if count == 1 and len(self.list_of_coefficient)==1:
                new_string += '0'
            elif count ==1 :
                pass
            elif str(self.list_of_exponent[0])[0] == "-":
                new_string += "x^" + str(self.list_of_exponent[0])
            elif str(self.list_of_exponent[0]) == '1':
                new_string += "x"    
            elif str(self.list_of_exponent[0]) == '0':
                pass
            else:
                new_string += "x^" + str(self.list_of_exponent[0])
            for i  in range(1,len(self.list_of_coefficient)):
                if str(self.list_of_coefficient[i])[0] == "-":
                    new_string += " - "+ str(self.list_of_coefficient[i])[1:]   
                elif (self.list_of_coefficient[i]) == 1:
                    new_string += ' + '
                elif (self.list_of_coefficient[i]) == -1:
                    new_string += ' - '
                else:
                    new_string += " + " + str(self.list_of_coefficient[i])
                if str(self.list_of_exponent[i])[0] == " - ":
                    new_string += "x^" + str(self.list_of_exponent[i])
                elif str(self.list_of_exponent[i])[0] == '1':
                    new_string += "x" 
                elif str(self.list_of_exponent[i])[0] == '0':
                    pass
                else:
                    new_string += "x^" + str(self.list_of_exponent[i])                   
        return (new_string)

        
    def add_term(self, coefficient, exponent):
        if exponent in self.list_of_exponent:
            self.list_of_coefficient[self.list_of_exponent.index(exponent)] += coefficient
            if 0 in self.list_of_coefficient:
                index= (self.list_of_coefficient.index(0))
                self.list_of_exponent.remove(self.list_of_exponent[index])
                self.list_of_coefficient.remove(0)
        else:
            self.list_of_coefficient.append(coefficient)
            self.list_of_exponent.append(exponent)              

    def __add__(self, other):
        result = Polynomial ()
        for i in range(len(other.list_of_exponent)):
            result.add_term(other.list_of_coefficient[i],other.list_of_exponent[i])
        for i in range(len(self.list_of_coefficient)):
            result.add_term(self.list_of_coefficient[i],self.list_of_exponent[i])  
        return result

    def get_degree(self):
        return max(self.list_of_exponent)
            
    def add(self, other):
        for i in range(len(other.list_of_exponent)):
            self.add_term(other.list_of_coefficient[i],other.list_of_exponent[i])

    def evaluate(self, x):
        answer = 0
        for i in range(0, len(self.list_of_coefficient)):
            answer = answer + (self.list_of_coefficient[i] * (x ** self.list_of_exponent[i]))
        return answer
    def scale(self, x):
        for i in range(len(self.list_of_coefficient)):
            self.list_of_coefficient[i] *= x

    def collapse(self):
        coefficient_list = []
        exponent_list = []
        exponent_list.append(sum(self.list_of_exponent))
        coefficient_list.append(sum(self.list_of_coefficient))
        self.list_of_exponent = exponent_list
        self.list_of_coefficient = coefficient_list

class Car:

    def __init__(self, plate, row, col, d_row, d_col):
        self.plate = plate
        self.row = row
        self.col = col
        self.d_row = d_row
        self.d_col = d_col
    def get_position(self):
        return (self.row,self.col)
    
    def __str__(self):
        return str(self.get_plate()) + "_" + str(self.row) + "_" + str(self.col)

    def get_plate(self):
        return self.plate

    def collides(self, other):
        if self.get_position()== other.get_position():
            return True
        else:
            return False

    def move(self, max_x, max_y):
        self.col = self.col +self.d_col
        self.row = self.row + self.d_row
        if self.col > (max_y -1):
            self.col = 0
        if self.row > (max_x - 1):
            self.row = 0
        if self.col < 0:
            self.col = max_y 
        if self.row < 0:
            self.row = max_x

        

class Traffic:

    def __init__(self, grid_size_rows, grid_size_cols):
        self.new_list = []
        self.grid_size_rows = grid_size_rows
        self.grid_size_cols = grid_size_cols
        
    def __str__(self):
        string = ''
        for item in self.new_list:
            string = string + str(item) + " "
        return string.strip()

    def add_car(self, car):
        car_plate = car.get_plate()
        none_method = None
        car_location = car.get_position()
        for item in self.new_list:
            if item.get_plate() == car_plate:
                none_method = item
        for item in self.new_list:
            if item.get_position() == car_location:
                raise ValueError
        if none_method is not None:
            self.new_list.remove(none_method)
        self.new_list.append(car)

    def get_plates(self, x, y):
        pass


    def execute(self, steps):
        if steps > 0:
                new_cofficeient = self.get_collisions()
                steps -= 1               
                for item in self.new_list:
                    if item.get_position() not in new_cofficeient:
                        item.move(self.grid_size_rows,self.grid_size_cols)
    def get_collisions(self):
        new_list_of_items = []
        dict_new = {}       
        for item in self.new_list:
            tuple_list = (item.get_position())
            if tuple_list in dict_new.keys() and tuple_list not in new_list_of_items:
                new_list_of_items.append(tuple_list)
            else:
                dict_new[tuple_list] = True
        return new_list_of_items

    def get_location(self, plate):
        for item in self.new_list:
            if item.get_plate() == plate:
                return item.get_position()

   

    

