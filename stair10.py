n=int(input())
x=[int(i) for i in input().split()]
s=0
c=0
for i in range(1,n):
	if x[i-1]<x[i]:
		(c)=(c)+x[i-1]
		(s)=(s)+(c)
print(s)
		
