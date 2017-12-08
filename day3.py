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
	mSquareNum = 1
	d = 1
	x = 0
	y = 0
	#coord = [0,0]
	foundNum = False

	while not foundNum:

		if mSquareNum ==squareNum:
			break;
		dif = d//abs(d)
		#print("d = " +str(d))
		#print("dif = " + str (dif))
		for _ in range(abs(d)):
			x += dif
			#print("Shift x by 1: " + str((x,y)) + " squareNum = " + str(mSquareNum))
			mSquareNum += 1
			if mSquareNum == squareNum:
				foundNum = True
				break

		if(not foundNum	):
			for _ in range(abs(d)):
				y += dif
				#print("Shift y by 1: " + str((x,y))+ " squareNum = " + str(mSquareNum))
				mSquareNum += 1
				if mSquareNum == squareNum:
					foundNum = True
					break

		if d > 0:
			d += 1
			d *= -1
		else:
			d *= -1
			d += 1	

	print("Found coordinates: "+str(squareNum) + " is at " + str((x,y)))

	#Calculate abs difference of cartesian coordinates
	numSteps = abs(x) + abs(y)
	return numSteps;

#Test Cases
TestCompare( 1, 0, CalcSteps(1))
TestCompare(12, 3, CalcSteps(12))
TestCompare(23, 2, CalcSteps(23))
TestCompare(1024, 31, CalcSteps(1024))

data = input("What square do you want steps for?")
steps = CalcSteps(int(data))
print("Steps necessary: " + str(steps))
