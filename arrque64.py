n=[int(x) for x in input().split()]
print(n)
a=[int(x) for x in input().split()]
print(a)
b=[]
print(b)
for i in range(n[1]):
	q=[int(x) for x in input().split()]
	print(q)
	if q[0]==2:
		b=a[q[1]-1:q[2]]
		print(b)
		b= list(reversed(b))
		k=b
		b=k
		print(b)
		r=a[q[2]:]
		s=a[:q[1]-1]
		print(s)
		print(r)
		b=s+b+r
		print(b)
		a=b
		print(a)
	else:
		print(a)
		s=[]
		f=[]
		e=[]
		g=[]
		s=a[q[1]-1:q[2]-1]
		f=a[q[2]-1:]
		e=a[q[2]:]
		g=a[:q[1]-1]
		v=g+f+s+e
		print(v)
 
m=[int(x) for x in input().split()]
print(m)
l=len(m)
for i in m:
	print(v[i-1],end=" ")
	
	
	
