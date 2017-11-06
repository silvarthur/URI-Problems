from fractions import Fraction

n = input()

for i in range(0,n):
	operation = raw_input().split(" ")

	operator = operation[3]
	n1, d1 = int(operation[0]), int(operation[2])
	n2, d2 = int(operation[4]), int(operation[6])

	if(operator == "+"):
		n_res = (n1*d2) + (n2*d1)
		d_res = d1*d2
	elif(operator == "-"):
		n_res = (n1*d2) - (n2*d1)
		d_res = d1*d2
	elif(operator == "*"):
		n_res = n1*n2
		d_res = d1*d2
	elif(operator == "/"):
		n_res = n1*d2
		d_res = n2*d1

	print "%d/%d = %s" % (n_res, d_res, str(Fraction(n_res, d_res)))