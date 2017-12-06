# day 3
# kgawne

def TestCompare( case, expected, result):
	print('Case ' + str(case) + ': ')
	if expected == result:
		print("\tSuccess! Result: " + str(result))
		return True;
	else:
		print("\tFailed :( Expected: " + str(expected) + " Result: " + str(result))
		return False;

def CalcSteps(squareNum):
	#generate blocks up to square number
	n = 0
	d = 1
	x, y = 0
	coord = [0,0]
	foundNum = False

	while not foundNum:

		if n ==squareNum:
			break;
		dif = d/d

		for _ in range(abs(d)):
			print("Shift x by 1: " + str(coord))
			coord.x += dif
			++n
			if n == squareNum:
				foundNum = true
				break

		if(not foundNum	):
			for _ in range(abs(d)):
				print("Shift y by 1: " + str(coord))
				coord.y += dif
				++n
				if n == squareNum:
					foundNum = True
					break

		if d > 0:
			d += 1
			d *= -1
		else:
			d *= -1
			d += 1	

	print("Found coordinates: "+str(squareNum) + " is at " + str(coord))

	#Calculate abs difference of cartesian coordinates
	numSteps = abs(coord.x) + abs(coord.y)
	return numSteps;

#Test Cases
TestCompare( 1, 0, CalcSteps(1))
TestCompare(12, 3, CalcSteps(12))
TestCompare(23, 2, CalcSteps(23))
TestCompare(1024, 31, CalcSteps(31))

data = input("What square do you want steps for?")
steps = CalcSteps(int(data))
print("Steps necessary: " + str(steps))
