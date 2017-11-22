'''
Converts a decimal number to a hexadecimal number.
'''
def dec_to_hex(number):
	output = ""

	while(True):
		remainder = int(number) % 16

		number = str(int(number) / 16)

		if(remainder == 10):
			output = "A" + output
		elif(remainder == 11):
			output = "B" + output
		elif(remainder == 12):
			output = "C" + output
		elif(remainder == 13):
			output = "D" + output
		elif(remainder == 14):
			output = "E" + output
		elif(remainder == 15):
			output = "F" + output
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
		if(number[i] == "A" or number[i] == "a"):
			output += (10 * (16 ** power))
		elif(number[i] == "B" or number[i] == "b"):
			output += (11 * (16 ** power))
		elif(number[i] == "C" or number[i] == "c"):
			output += (12 * (16 ** power))
		elif(number[i] == "D" or number[i] == "d"):
			output += (13 * (16 ** power))
		elif(number[i] == "E" or number[i] == "e"):
			output += (14 * (16 ** power))
		elif(number[i] == "F" or number[i] == "f"):
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

		if(number[i] == "A" or number[i] == "a"):
			temp_number = 10
		elif(number[i] == "B" or number[i] == "b"):
			temp_number = 11
		elif(number[i] == "C" or number[i] == "c"):
			temp_number = 12
		elif(number[i] == "D" or number[i] == "d"):
			temp_number = 13
		elif(number[i] == "E" or number[i] == "e"):
			temp_number = 14
		elif(number[i] == "F" or number[i] == "f"):
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
	
	return output

n = input()

for i in range(0, n):
	user_input = raw_input().split(" ")

	x = user_input[0]
	y = user_input[1]

	print "Case %d" % (i + 1)
	if(y == "dec"):
		print "%s hex" % (dec_to_hex(x))
		print "%s bin\n" % (dec_to_bin(x))
	elif(y == "hex"):
		print "%s dec" % (hex_to_dec(x))
		print "%s bin\n" % (hex_to_bin(x))
	elif(y == "bin"):
		print "%s dec" % (bin_to_dec(x))
		print "%s hex\n" % (bin_to_hex(x))


