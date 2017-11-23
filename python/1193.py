'''
AUXILIAR FUNCTIONS
'''
def correct_multiplicity(number):
	if(len(number) % 4 != 0):
		number_of_zeros = (4 - (len(number) % 4))
		return (number_of_zeros * "0") + number
	else:
		return number

def create_matrix(number):
	output = []

	temp_string = ""
	for i in range(0,len(number)):
		temp_string += number[i]

		if((i + 1) % 4 == 0 or i == (len(number) - 1)):
			output.append(temp_string)

			temp_string = ""

	return output

'''
Converts a decimal number to a hexadecimal number.
'''
def dec_to_hex(number):
	output = ""

	while(True):
		remainder = int(number) % 16

		number = str(int(number) / 16)

		if(remainder == 10):
			output = "a" + output
		elif(remainder == 11):
			output = "b" + output
		elif(remainder == 12):
			output = "c" + output
		elif(remainder == 13):
			output = "d" + output
		elif(remainder == 14):
			output = "e" + output
		elif(remainder == 15):
			output = "f" + output
		else:
			output = str(remainder) + output

		if(number == "0"):
			break

	return output

'''
Converts a decimal number to a binary number.
'''
def dec_to_bin(number):
	output = ""

	while(True):
		remainder = int(number) % 2

		number = str(int(number) / 2)

		output = str(remainder) + output

		if(number == "0"):
			break

	return output

'''
Converts a hexadecimal number to a decimal number.
'''
def hex_to_dec(number):
	output = 0

	power = 0
	for i in reversed(range(0,len(number))):
		if(number[i] == "a"):
			output += (10 * (16 ** power))
		elif(number[i] == "b"):
			output += (11 * (16 ** power))
		elif(number[i] == "c"):
			output += (12 * (16 ** power))
		elif(number[i] == "d"):
			output += (13 * (16 ** power))
		elif(number[i] == "e"):
			output += (14 * (16 ** power))
		elif(number[i] == "f"):
			output += (15 * (16 ** power))
		else:
			output += (int(number[i]) * (16 ** power))
		power += 1

	return str(output)

'''
Converts a hexadecimal number to a binary number.
'''
def hex_to_bin(number):
	output = ""

	for i in range(0,len(number)):
		temp_output = ""

		if(number[i] == "a"):
			temp_number = 10
		elif(number[i] == "b"):
			temp_number = 11
		elif(number[i] == "c"):
			temp_number = 12
		elif(number[i] == "d"):
			temp_number = 13
		elif(number[i] == "e"):
			temp_number = 14
		elif(number[i] == "f"):
			temp_number = 15
		else:
			temp_number = number[i]
		while(True):
			remainder = int(temp_number) % 2

			temp_number = str(int(temp_number) / 2)

			temp_output = str(remainder) + temp_output

			if(temp_number == "0"):
				break
		output += temp_output

	return output

'''
Converts a binary number to a decimal number.
'''
def bin_to_dec(number):
	output = 0

	power = 0
	for i in reversed(range(0,len(number))):
		if(number[i] == "1"):
			output += (2 ** power)
		power += 1

	return str(output)

'''
Converts a binary number to hexadecimal number.
'''
def bin_to_hex(number):
	output = ""

	matrix = create_matrix(correct_multiplicity(number))

	for i in range(0,len(matrix)):
		power = 0
		temp_hex_number = 0
		for j in reversed(range(0, len(matrix[i]))):
			temp_hex_number += (int(matrix[i][j]) * (2 ** power))
			power += 1

		if(temp_hex_number == 10):
			output += "a"
		elif(temp_hex_number == 11):
			output += "b"
		elif(temp_hex_number == 12):
			output += "c"
		elif(temp_hex_number == 13):
			output += "d"
		elif(temp_hex_number == 14):
			output += "e"
		elif(temp_hex_number == 15):
			output += "f"
		else:
			output = str(temp_hex_number)

	return output

n = input()

for i in range(0, n):
	user_input = raw_input().split(" ")

	x = user_input[0]
	y = user_input[1]

	print "Case %d:" % (i + 1)
	if(y == "dec"):
		print "%s hex" % (dec_to_hex(x))
		print "%s bin\n" % (dec_to_bin(x))
	elif(y == "hex"):
		print "%s dec" % (hex_to_dec(x))
		print "%s bin\n" % (hex_to_bin(x))
	elif(y == "bin"):
		print "%s dec" % (bin_to_dec(x))
		print "%s hex\n" % (bin_to_hex(x))


