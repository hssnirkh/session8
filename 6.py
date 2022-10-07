def upSideDown(num):
	reverse = 0
	while(num != 0):
		reminder = num % 10
		reverse = (reverse * 10) + reminder
		num //= 10
	return reverse
#print(upSideDown(int(input("x : "))))
for i in range(1,1001):
	if(upSideDown(i) == i):
		print(i)
