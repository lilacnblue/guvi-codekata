x=[x for x in input().split()]
a=x[0]
n=len(a)
b=x[1]
m=len(b)
t=min(n,m)
c=0
for i in range(t):
	if x[0][i]==x[1][i]:
		c=c
	elif x[0][i]!=x[1][i]:
		c=c+1
r=abs(m-n)+c
print(r)
