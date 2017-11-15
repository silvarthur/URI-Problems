def numberOfDaysToEatAllFood(foodSupply):
	result = 0

	while(foodSupply > 1):
		foodSupply /= 2
		result += 1

	return result

n = input()

for i in range(0,n):
	x = input()
	print "%d dias" % (numberOfDaysToEatAllFood(x))