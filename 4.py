
def isStr(str,chr):
	for i in range(0,len(str)):
		if(chr == str[i]):
			return 1
			break
	else:
			return 0


print(isStr(input("STR : "),input("CHR : ")))
