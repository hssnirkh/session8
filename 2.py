import math
def isPrime(num): 
	sq =int(math.sqrt(num))
	if(num > 1):
		for i in range(2,sq + 1):
			if((num % i) == 0):
				#print("NO {0} is not Prime num".format(num))
				return 0
				break
		else:
			print("YES {0} is Prime num ".format(num))
			return 1
	else:
		#print("no")
		return -1

for i in range(0,10):
	x = isPrime(int(input("Pls Enter Num {0}: ".format(i))))
	#if(x == 1):
	#	print(x)

