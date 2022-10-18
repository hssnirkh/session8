
def strReverse(str):
	k = len(str)
	for i in range(0,k):
		for j in range(0,i+1):
			print("*" , end=" ")
		print()
	return

strReverse(input("str : "))
