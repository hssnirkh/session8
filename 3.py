def sum(num):
	s = 0
	while(num != 0):
		c = num % 10
		s +=c
		num //= 10
	return s

#sum(int(input("x : ")))
for i in range(0,3):
	x = int(input("x : "))
	if(sum(x) % 2 == 0):
		print(x)
