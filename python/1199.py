def dec_to_hex(number):
	output = ""

	while(True):
		remainder = number % 16
		number /= 16

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

		if(number == 0):
			break

	return output

def hex_to_dec(number):
	output = 0

	power = 0
	for i in reversed(range(0, len(number))):
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

	return output

while(True):
	user_input = raw_input()

	if(user_input == "-1"):
		break
	elif(user_input[0:2] == "0x"):
		number = user_input[2:]
		print hex_to_dec(number)
	else:
		number = int(user_input)
		print "0x" + dec_to_hex(number)