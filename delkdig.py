x,n=input().split()
k=int(n)
if k==0:
	print(x)
else:	
	y=min(x)
	z=x.find(y)
	l=x[0:z]
	r=x[z:]
	n=r+l
	n=n[:-k]
	print(n)
 
