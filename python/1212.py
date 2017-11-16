'''
Children are taught to add multi-digit numbers from right-to-left 
one digit at a time. Many find the "carry" operation - in which a 
1 is carried from one digit position to be added to the next - to 
be a significant challenge. Your job is to count the number of carry 
operations for each of a set of addition problems so that educators 
may assess their difficulty.

INPUT

Each line of input contains two unsigned integers less than 10 digits. 
The last line of input contains 0 0.

OUTPUT

Output

For each line of input except the last you should compute and print 
the number of carry operations that would result from adding the two 
numbers, in the format shown below.
'''

'''
VERSION 1

40% WRONG

def get_greatest_value(number1, number2):
	return number1 if (len(number1) > len(number2)) else number2

def get_smallest_number(number1, number2):
	return number1 if (len(number1) < len(number2)) else number2

def get_number_of_carry_operations(number1, number2):
	if(len(number1) != len(number2)):
		number1 = get_greatest_value(number1, number2)
		number2 = get_smallest_number(number1, number2)		

	number_of_carry_operations = 0

	hasToCarry = False
	for i in reversed(range(0, len(number2))):
		result = int(number2[i]) + int(number1[i])

		if(hasToCarry):
			result += 1
			if(result > 9):
				number_of_carry_operations += 1
				hasToCarry = True
		else:
			if(result > 9):
				number_of_carry_operations += 1
				hasToCarry = True

	return number_of_carry_operations

while True:
	user_input = raw_input().split(" ")

	number1 = user_input[0]
	number2 = user_input[1]

	if(number1 == "0" and number2 == "0"):
		break
	else:
		number_of_carry_operations = get_number_of_carry_operations(number1, number2)

		if(number_of_carry_operations == 0):
			print "No carry operation."
		else:
			if(number_of_carry_operations == 1):
				print "1 carry operation."
			else:
				print "%d carry operations." % (number_of_carry_operations)
'''

'''
O resto da divisão um número por 10 é igual ao número referente as unidades.
Ex.: 123 % 10 = 3.

Dividir um número por 10 é igual a remover o número referente as unidades.
Ex.: 123 / 10 = 12

'''
def get_number_of_carry_operations(number1, number2):
	carry, number_of_carry_operations = 0

	return number_of_carry_operations

while True:
	user_input = raw_input().split(" ")

	number1 = user_input[0]
	number2 = user_input[1]

	if(number1 == "0" and number2 == "0"):
		break
	else:
		number_of_carry_operations = get_number_of_carry_operations(number1, number2)

		if(number_of_carry_operations == 0):
			print "No carry operation."
		else if(number_of_carry_operations == 1):
			print "1 carry operation."
		else:
			print "%d carry operations." % (number_of_carry_operations)