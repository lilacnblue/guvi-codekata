x=[x for x in input().split()]
a=x[0]
n=len(a)
b=x[1]
m=len(b)
c=0
for i in range(n):
	if x[0][i]==x[1][i]:
		c=c
	elif x[0][i]!=x[1][i]:
		c=c+1
r=m-n+c
print(r)
