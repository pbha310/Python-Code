import Asst2

def welcome_message():
    print('COMPSCI 105, Summer 2016')
    print('Marking program for Assignment Two\n')
    print('This program is a similar format to the actual marking')
    print('so please check your work using this program before')
    print('submitting.\n')
    
def formatted_test_result(question, expected, got):
    print('  Test Q' + str(question) + ' : ', end = '')
    if expected == got:
        print('  PASS :-)  ', got)
    else:
        print('  FAIL :-(')
        print('    - the expected output = ', expected)
        print('    - the actual output =   ', got)
    
def q1_test(infix, expected):
    try:
        result = Asst2.generate_postfix(infix)
    except:
        result = 'an exception occurred'
    formatted_test_result(1, expected, result)

def q2_test(n, expected):
    try:
        result = []
        c = Asst2.generate_prime_chain(n)
        while c != None:
            result.append(c.get_data())
            c = c.get_next()
    except:
        result = 'an exception occurred'
    formatted_test_result(2, expected, result)

def q3_test(n, expected):
    try:
        result = []
        c = Asst2.generate_prime_chain(n)
        Asst2.back_to_front_chain(c)
        while c != None:
            result.append(c.get_data())
            c = c.get_next()
    except:
        result = 'an exception occurred'
    formatted_test_result(3, expected, result)

## convert_tree_to_list() function from Binary Tree lecture (slide 35)
def convert_tree_to_list(t):
    if t == None:
        return None
    else:
        result = []
        result.append(t.get_data()) 
        result.append(convert_tree_to_list(t.get_left()))
        result.append(convert_tree_to_list(t.get_right()))
        return result

def q4_test(flat_list, nested_list):
    try:
        t1 = Asst2.create_tree_from_flat_list(flat_list)
        t2 = Asst2.create_tree_from_nested_list(nested_list)
        result1 = convert_tree_to_list(t1)
        result2 = convert_tree_to_list(t2)
    except:
        result1 = 'an exception occurred'
        result2 = 'an exception occurred'
    formatted_test_result(4, nested_list, result1)
    formatted_test_result(4, nested_list, result2)

def q5_test(nested_list, expected):
    try:
        t = Asst2.create_tree_from_nested_list(nested_list)
        result = Asst2.sum_tree(t)
    except:
        result = 'an exception occurred'
    formatted_test_result(5, expected, result)

def q6_test(nested_list, expected1, expected2, expected3):
    try:
        t = Asst2.create_tree_from_nested_list(nested_list)
        result1 = Asst2.pre_order(t)
        result2 = Asst2.in_order(t)
        result3 = Asst2.post_order(t)
    except:
        result1 = 'an exception occurred'
        result2 = 'an exception occurred'
        result3 = 'an exception occurred'
    formatted_test_result(6, expected1, result1)
    formatted_test_result(6, expected2, result2)
    formatted_test_result(6, expected3, result3)

def q7_test(nested_list, expected):
    try:
        t = Asst2.create_tree_from_nested_list(nested_list)
        result = Asst2.is_binary_search_tree(t)
    except:
        result = 'an exception occurred'
    formatted_test_result(7, expected, result)

def q8_test(nested_list, n, expected):
    try:
        t = Asst2.create_tree_from_nested_list(nested_list)
        result = Asst2.insert_position_in_bst(t, n)
    except:
        result = 'an exception occurred'
    formatted_test_result(8, expected, result)

def q9_test(keys, table_size, probe_type, expected):
    try:
        result = Asst2.hash_with_probing(keys, table_size, probe_type)
    except:
        result = 'an exception occurred'
    formatted_test_result(9, expected, result)


def test_question_one():
    print('\nTesting Question One\n--------------------')
    q1_test('2 ^ ( 4 < 6 ) - 3 / 3 * 1', '2 4 6 < ^ 3 3 / 1 * -')
    q1_test('( 1 + ( 1 + ( 1 + ( 1 + ( 1 + 1 ) ) ) ) * 2 )', '1 1 1 1 1 1 + + + + 2 * +')
    q1_test(') 555 (', 'imbalanced brackets')
    q1_test('7 * 2 ^ ( 8 + 4 / 2 > 1 ( - 15 / 4', 'imbalanced brackets')
    q1_test('6 ! 7 + 6', 'invalid symbol')
    q1_test('7 * 2 ^ ( 8.8 + 4 / 2 > 1 ) - 15 / 4', 'invalid symbol')
    q1_test('555 + 555 +', 'too many operators')
    q1_test('( 1 + ( 1 + ( * 1 + ( 1 + ( 1 + 1 ) ) ) ) * 2 )', 'too many operators')
    q1_test('7 * 2 ( 8 + 4 / 2 > 1 ) - 15 / 4', 'too few operators')
    q1_test('555 + 555 555', 'too few operators')

def test_question_two():
    print('\nTesting Question Two\n--------------------')
    q2_test(3, [2, 3, 5])
    q2_test(170, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013])

def test_question_three():
    print('\nTesting Question Three\n----------------------')
    q3_test(2, [2, 3])
    q3_test(170, [2, 1013, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009])

def test_question_four():
    print('\nTesting Question Four\n---------------------')
    q4_test([None, 10, 5], [10, [5, None, None], None])
    q4_test([None, 10, 5, 15, None, None, 11, 22], [10, [5, None, None], [15, [11, None, None], [22, None, None]]])

def test_question_five():
    print('\nTesting Question Five\n---------------------')
    q5_test([10, [5, None, None], None], 15)
    q5_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], 63)

def test_question_six():
    print('\nTesting Question Six\n--------------------')
    q6_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], [10, 5, 15, 11, 22], [5, 10, 11, 15, 22], [5, 11, 22, 15, 10])

def test_question_seven():
    print('\nTesting Question Seven\n----------------------')
    q7_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], True)
    q7_test([12, [6, [3, None, None], [13, None, None]], [25, None, None]], False)

def test_question_eight():
    print('\nTesting Question Eight\n----------------------')
    q8_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], 3, 'left of 5')
    q8_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], 13, 'right of 11')
    q8_test([12, [6, [3, None, None], [11, None, None]], [25, None, None]], 100, 'right of 25')
    q8_test([12, [6, [3, None, None], [11, None, None]], [25, None, None]], 10, 'left of 11')

def test_question_nine():
    print('\nTesting Question Nine\n---------------------')
    q9_test([26, 54, 94, 17, 31, 77, 44, 51], 13, 'linear', [26, 51, 54, 94, 17, 31, 44, None, None, None, None, None, 77])
    q9_test([26, 54, 94, 17, 31, 77, 43, 25], 13, 'quadratic', [26, None, 54, 94, 17, 31, None, None, 43, None, None, 25, 77])

    
welcome_message()

test_question_one()
test_question_two()
test_question_three()
test_question_four()
test_question_five()
test_question_six()
test_question_seven()
test_question_eight()
test_question_nine()


