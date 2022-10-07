
def factor(num):
	f = 1
	for i in range(1,num+1):
		f *= i
	return f
#print(factor(int(input())))

x = int(input("num : "))
if (x % 2 != 0):
	sum = 0
	for j in range(1,x+1):
		if(j % 2 != 0):
			#print(factor(j),factor(j+1))
			sum += (factor(j) / factor(j+1))
	print("answer 1!/2!+...+n!/n+1! is {0} ".format(sum))

else:
	print("adad fard vared konid")
