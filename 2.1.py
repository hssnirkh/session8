def isPrime(num):
	counter = 0
	for i in range(1,num+1):
		if(num % i == 0):
			counter+=1
	if(counter == 2):
		return 1
	else:
		return 0

for i in range(1,6):
	num = int(input("enter {0} : ".format(i)))
	print(isPrime(num))
