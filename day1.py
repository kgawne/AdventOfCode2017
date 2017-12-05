
#Day 1
#KGawne

#Calculate Sum
def CalculateSum1( data):
	tSum = 0
	prevNum = -1

	for n in data:
		if n == prevNum:
			tSum += int(n)
		prevNum = n

	if prevNum == data[0]:
		tSum += int(prevNum);

	return tSum;

def CalculateSum2( data):
	tSum = 0
	length = len(data)

	for i in range(0, length):
		nextIndex = int((i + length/2)%length)
		#print(type(nextIndex))
		#print("cur i: " + str(i) + "; cur next: " + str(nextIndex))
		if nextIndex > length:
			nextIndex -= length
			#print("cur i: " + i + "; cur next: " + nextIndex)

		x = data[i]

		if data[i] == data[int(nextIndex)]:
			tSum += int(data[i])

	return tSum;

def TestCompare( case, expected, result):
	print('Case ' + str(case) + ': ')
	if expected == result:
		print("\tSuccess! Result: " + str(result))
		return True;
	else:
		print("\tFailed :( Expected: " + str(expected) + " Result: " + str(result))
		return False;


#Test Cases for Part 1
print( "\n***** Testing Part 1 *****")
test1 = CalculateSum1('1122')
TestCompare('1122', 3, test1)

test2 = CalculateSum1('1111')
TestCompare('1111', 4, test2)

test3 = CalculateSum1('1234')
TestCompare('1234', 0, test3)

test4 = CalculateSum1('91212129')
TestCompare('91212129', 9, test4)


#Test Cases for Part 2
print("\n***** Testing Part 2 *****")
test1 = CalculateSum2('1212')
TestCompare('1212', 6, test1)

test2 = CalculateSum2('1221')
TestCompare('1221', 0, test2)

test3 = CalculateSum2('123425')
TestCompare('123425', 4, test3)

test4 = CalculateSum2('123123')
TestCompare('123123', 12, test4)

test5 = CalculateSum2('12131415')
TestCompare('12131415', 4, test5)

#Get String Input
data = input("Input your string: ")
print(data)

iSum = CalculateSum1(data)
iiSum = CalculateSum2(data)

print ("Sum for part 1: " + str(iSum))
print ("Sum for part 2: " + str(iiSum))
