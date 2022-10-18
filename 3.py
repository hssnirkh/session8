def sum(num):
	s = 0
	while(num != 0):
		c = num % 10
		s +=c
		num //= 10
	return s

#print(sum(int(input("x : "))))
for i in range(0,3):
	x = int(input("x : "))
	if(sum(x) % 2 == 0):
		print(x)
#recursive way
def sumNum(num):
	if(num == 0):
		return 0
	else:
		return num % 10 + sumNum(num // 10)
#print(sumNum(int(input())))
num = int(input("num : "))
if(sumNum(num) % 2 == 0):
	print(num)
else:
	print("fard")
