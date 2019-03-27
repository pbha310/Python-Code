from Node import Node
from Stack import Stack
from Queue import Queue
from BinaryTree import BinaryTree


def evaluate_expression(infix):
    postfix_list = []
    list_infix = infix.split()
    operators = "-+/*><^"
    operation_stack = Stack()
    dictionary_values = {"^":4, "*":3, "/":3, "+":2, "-":2, "<":1, ">":1, "(":0}
    for i in list_infix:
        if i in operators:
            while (not operation_stack.is_empty()) and (dictionary_values[operation_stack.peek()] >= dictionary_values[i]):
                postfix_list.append(operation_stack.pop())
            operation_stack.push(i)
        elif i == "(":
            operation_stack.push(i)
        elif i == ")":
            i = operation_stack.pop()
            while not i == "(":
                postfix_list.append(i)
                i = operation_stack.pop()
        else:
            postfix_list.append(i)
            
    while not operation_stack.is_empty():
        postfix_list.append(operation_stack.pop()) 
    return evaluate_postfix_expression(postfix_list)

def calculation(num, num2, operator_value):
    if operator_value == "+":
        return num + num2
    elif operator_value == "-":
        return num - num2
    elif operator_value == "*":
        return num * num2
    elif operator_value == "/":
        return num // num2
    elif operator_value == "^":
        return num ** num2
    elif operator_value == ">":
        return max(num, num2)
    else:
        return min(num, num2)

def evaluate_postfix_expression(post_list):
    operators = "+-*/><^"
    expression = Stack()
    for i in post_list:
        if i in operators:
            if expression.size() > 1:
                num2 = expression.pop()
                num = expression.pop()
                result = calculation(int(num), int(num2), i)
                expression.push(result)
            else:
                pass
        else:
            expression.push(i)
    return expression.pop()

def generate_chain(start, n):
    node = Node(start)
    start = node
    for k in range(n-1):
        temp = Node(node.get_data() + sum(int(i) for i in str(node)))
        node.set_next(temp)
        node = node.get_next()
    return start

def move_node_to_end(values, value):
    previous = None
    current = values
    while current:
        if current.get_data() == value:
            break
        previous = current
        current = current.get_next()
    if previous:  
        previous.set_next(current.get_next())  
        temp = values
        while temp:
            if not temp.get_next():  
                current.set_next(None)
                temp.set_next(current)
                break
            temp = temp.get_next()

def create_tree_from_nested_list(node_list):
    if node_list[1] == None and node_list[2] == None:
        return BinaryTree(node_list[0])
    elif node_list[1] == None and node_list[2] != None:
        temp2 = create_tree_from_nested_list(node_list[2])
        temp3 = BinaryTree(node_list[0])
        temp3.set_right(temp2)
        return temp3
    elif node_list[1] != None and node_list[2] == None:
        temp1 = create_tree_from_nested_list(node_list[1])
        temp3 = BinaryTree(node_list[0])
        temp3.set_left(temp1)
        return temp3

    else:
        temp1 = create_tree_from_nested_list(node_list[1])
        temp2 = create_tree_from_nested_list(node_list[2])
        temp3 = BinaryTree(node_list[0])
        temp3.set_left(temp1)
        temp3.set_right(temp2)
        return temp3

def create_tree_from_flat_list(node_list):
    def flat_list(list_node, index_value=1):
        if index_value >= len(list_node) or list_node[index_value] is None:
            return None
        left_value = index_value * 2
        right_value = left_value + 1
        value = list_node[index_value]
        tree_value = BinaryTree(value)
        tree_value.set_right(flat_list(list_node, right_value))
        tree_value.set_left(flat_list(list_node, left_value))
        return tree_value
    return flat_list(node_list,index_value=1)

def breadth_first(a):
    result_list = []
    queue = Queue() 
    queue.enqueue(a) 
    while not queue.is_empty():
        treenode = queue.dequeue()
        if treenode is not None:
            queue.enqueue(treenode.get_left())
            queue.enqueue(treenode.get_right())
            result_list.append(treenode.get_data())
    return (result_list)

def mirror(tree):
    if tree == None:
        pass
    else:
        mirror(tree.get_right())
        mirror(tree.get_left())
        right_tree = tree.get_right()
        left_tree = tree.get_left()
        tree.set_right(left_tree)
        tree.set_left(right_tree)

def hashing(keys, table_size, probe_type, double_hash_value):
    hash_table = [None] * table_size
    
    for key in keys:
        position = key%table_size
        if hash_table[position] is None:
            hash_table[position] = key
        else:
            if probe_type == "linear":
                position =  (position +1)%table_size
                while hash_table[position] is not None:
                    position =  (position +1)%table_size    
                hash_table[position] = key
            if probe_type == "quadratic":
                i = 1
                while hash_table[(i*i + position) % table_size] is not None:
                    i += 1
                hash_table[(i*i + position) % table_size] = key

            if probe_type == "double":
                new_value = double_hash_value -(key%double_hash_value)
                position = (position + new_value) % table_size
                while hash_table[position] is not None:
                    position =  (position +new_value)%table_size    
                hash_table[position] = key
    return hash_table

#-------------------------#BONUS QUESTION---------------------------------------------------------#
def create_binary_search_tree(list):
    pass
def solve_problem(space_left,items,starting,ending):
    if can_find_time(space_left,items,starting,ending) == False:
        return space_left
    else:
        ending = ending-1
        starting = starting
        result_of_2 = solve_problem(space_left,items,starting,ending)
        result_of_1 = solve_problem(space_left-items[ending+1],items,starting,ending)
        if result_of_1 >=0 and result_of_2 >=0:
            return min(result_of_1,result_of_2)
        elif result_of_2 >=0:
            return result_of_2
        elif result_of_1 >=0:
            return result_of_1
        
        
def can_find_time(space_left,items,starting,ending):
    count = 0
    if starting == ending:
        if items[0] <= space_left:
            return True
        else:
            return False
    elif ending< 0:
        return False
    for i in items[starting:ending]:
        if i < space_left:
            count += 1
    if count == 0:
        return False
    else:
        return True
def min_waste(space_left,items):
    return solve_problem(space_left,items,0,len(items)-1)



