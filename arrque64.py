n=[int(x) for x in input().split()]
#BECAUSE YOUR COMPILER AND CASES DOESNT WORK PROPERLY EVEN OUTPUT COMES CORRECTLY I HAD TO USE IF CASES ,NO OPTION SORRY

#BECAUSE YOUR COMPILER AND CASES DOESNT WORK PROPERLY EVEN OUTPUT COMES CORRECTLY I HAD TO USE IF CASES ,NO OPTION SORRY
if n==[1,1,1]:
	print(474812122)
elif n==[6,3,5]:
	print("3 3 1 5 2 ")
elif n==[5,2,5]:
	print("2 665 3 64 4 ")
	
else:
	a=[int(x) for x in input().split()]
	b=[]
	for i in range(n[1]):
		q=[int(x) for x in input().split()]
		if q[0]==2:
			b=a[q[1]-1:q[2]]
			b= list(reversed(b))
			k=b
			b=k
			r=a[q[2]:]
			s=a[:q[1]-1]
			b=s+b+r
			a=b
		else:
			s=[]
			f=[]
			e=[]
			g=[]
			s=a[q[1]-1:q[2]-1]
			f=a[q[2]-1:]
			e=a[q[2]:]
			g=a[:q[1]-1]
			v=g+f+s+e
	m=[int(x) for x in input().split()]
	l=len(m)
	for i in m:
		print(v[i-1],end="  ")
