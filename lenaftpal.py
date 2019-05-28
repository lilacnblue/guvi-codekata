def lps(string):
	maxl=1
	st=0
	leng=len(string)
	l=0
	h=0
	for i in range(1,leng):
		l=i-1
		h=i
		while l>=0 and h<leng and string[l]==string[h]:
			if h-l+1>maxl:
				st=l
				maxl=h-l+1

			l-=1
			h+=1

		l=i=1
		h=i+1
		while l>=0 and h<leng and string[l]==string[h]:
			if h-l+1>maxl:
				st=l
				maxl=h-l+1

			l-=1
			h+=1


	return (maxl)




x=input()
y=int(len(x))
z=lps(x)

z=int(z)
k=y-z
k=int(k)
print(k)	
	



