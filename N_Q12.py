k,y=[int(x) for x in input().split()]
z=[int(x) for x in input().split()]
for i in range(y):
	a,b=[int(x) for x in input().split()]
	d=z[a:b]
	s=sum(d)
	print(s)
