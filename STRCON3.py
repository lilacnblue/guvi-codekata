x=[x for x in input().split()]
n=len[x[0]]
m=len[x[1]]
c=0
for i in range(n):
	if x[0][i]==x[1][i]:
		c=c
	elif x[0][i]!=x[1][i]:
		c=c+1
r=m-n+c
print(r)
