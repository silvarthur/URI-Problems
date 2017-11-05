number_of_leds_by_num = {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}

n = input()

for i in range(0,n):
	output = 0
	value = raw_input()
	for j in value:
		output += number_of_leds_by_num[j]
	print "%d leds" % (output)