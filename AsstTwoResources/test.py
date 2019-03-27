def function(x, y):
	result = ''
	try:
		if x < 0:
			y = 1 / y
			x = -x
			result += 'a'
		elif x is 0:
			result += 'b'
	except ZeroDivisionError:
		result += 'c'
	except TypeError:
		result += 'd'
	except:
		result += 'e'
	finally:
		result += 'f'
	print('result =', result)
function(0,0)