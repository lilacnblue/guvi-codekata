str1=input()
str2=input()
le=len(str1)
li=[]
for i in range(le):
	el=ord(str1[i])+ord(str2[i])
	if el>=219:
		el=el-96-26
	else:
		el=el-96
	el=chr(el)
	li.append(el)
for i in li:
	print(i,end="")
