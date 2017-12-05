# Day 2
# kgawne
import numpy as np

def TestCompare( case, expected, result):
	print('Case ' + str(case) + ': ')
	if expected == result:
		print("\tSuccess! Result: " + str(result))
		return True;
	else:
		print("\tFailed :( Expected: " + str(expected) + " Result: " + str(result))
		return False;

def ReadInMatrix( filename):
	with open(filename, 'r') as f:
		f = open (filename, 'r')
		data = []
		data = [line.split() for line in f]

		intData = ConvertStrToIntArray(data)
	return intData;

def ConvertStrToIntArray (data):
	for row in data:
		for index, string in enumerate(row):
			row[index] = int(string)
	return data;

def CalcChecksum(data):
	checksum = 0

	for row in data:
		tMin = row[0]
		tMax = row[0]

		for item in row:
			if item < tMin:
				tMin = item
			elif item > tMax:
				tMax = item

		dif = tMax - tMin
		checksum += dif

	return checksum;

def CalcDivChecksum(data):
	checksum = 0

	for row in data:
		quotient = None
		for item in row:
			for otheritem in row:
				#check for even division and not duplication!
				if (item % otheritem == 0) and (item != otheritem):
					quotient = item//otheritem
					break;
			if (quotient != None):
				break;

		checksum += quotient
	return checksum;

#Test Case
data1 = np.array([[ 5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]], dtype=object)
test1 = CalcChecksum(data1)
TestCompare(data1, 18, test1)

data2 = np.array([[ 5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]], dtype=object)
test2 = CalcDivChecksum(data2)
TestCompare(data2, 9, test2)

# Read in Data
data = ReadInMatrix( 'day2_input.txt')
test3 = CalcChecksum(data)
test4 = CalcDivChecksum(data)
print("Your checksum is: " + str(test3))
print("Your div checksum is: " + str(test4))