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


	#Calculate abs difference of cartesian coordinates




	numSteps = 0
	return numSteps;

#Test Cases
TestCompare( 1, 0, CalcSteps(1))
TestCompare(12, 3, CalcSteps(12))
TestCompare(23, 2, CalcSteps(23))
TestCompare(1024, 31, CalcSteps(31))

data = input("What square do you want steps for?")
steps = CalcSteps(int(data))
print("Steps necessary: " + str(steps))
