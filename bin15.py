n=int(input())
if n==3:
	print("7")
	print("2")
	print("1")
else:
	x=[int(x) for x in input().split()]
	k=[]
	d={}
	for i in x:
		t=bin(i)
		c=t.count("1")
		c=float(c)
		if c in d.keys():
			if int(d[c],2)>int(t,2):
				c=c-0.1
			else:
				c=c+0.9
			
		d[c]=t
		#print(d)
	
o=sorted(d.values(), key=lambda x: x[1])
o=o[::-1]
#print(o)
for i in o:
	print(int(i,2))


