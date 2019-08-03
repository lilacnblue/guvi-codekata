n=int(input())
x=[int(i) for i in input().split()]
s=0
c=0
a=0
b=[0]
for i in range(1,n):
	if x[i-1]<x[i]:
		if a<x[i]:
			(c)=(c)+x[i-1]+a
			(s)=(s)+(c)
			
			
		else :
			(c)=(c)+x[i-1]
			(s)=(s)+(c)
	else :
		for k in range(len(b)):
			if x[i]<b[k]:
				c=c-b[k]
			else:
				c=(c)
		(s)=(s)+(c)
		a=x[i-1]
		b.append(a)
print(s)
		
