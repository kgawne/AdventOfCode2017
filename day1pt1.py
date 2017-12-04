data = input("Input your string: ")
print(data)

sum = 0
prevNum = -1

for n in data:
	if n == prevNum:
		sum += int(n)
	prevNum = n

print("This is your sum: ")
print(sum)