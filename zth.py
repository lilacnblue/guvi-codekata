t=int(input())
y=[]
c=0
b=0
while(b<t):
	i=[int(x) for x in input().split()]
	y.append(i)
	b=b+1
for a in y:
	
		a[0]=a[0]-1
		if (a[0]%a[1])==0:
			a[0]=a[0]/a[1]
		c=c+1
	print(c)		