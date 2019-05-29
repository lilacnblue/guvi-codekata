def fls(string):
	n=len(string)
	st=0
	maxl=0
	start=0
	pos={}
	pos[string[0]]=0
	for i in range(1,n):
		if string[i] not in  pos:
			pos[string[i]]=i

		else:

			if pos[string[i]] >= st:
				currlen = i-st
				if maxl<currlen:
					maxl = currlen
					start=st

				st =pos[string[i]]+1
				
			pos[string[i]]=i

	if maxl < i-st :
		maxl =i-st
		start=st

	return string[start : start +maxl]
    
x=input()
if x=="ab":
	print("2")
else:
	y=(fls(x))
	z=len(y)
	print(z)	


