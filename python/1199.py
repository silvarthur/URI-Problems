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
	for i in reversed(range(0, len(str(number)))):
		output += (int(str(number)[i]) * (16 ** power))
		power += 1

	return output

while(True):
	user_input = raw_input()

	if(user_input == "-1"):
		break
	elif(user_input[0:2] == "0x"):
		print hex_to_dec(int(user_input[2:]))
	else:
		print "0x" + dec_to_hex(int(user_input))