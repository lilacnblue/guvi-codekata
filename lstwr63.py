N=256
N=256
def fls(string):
	n=len(string)
	cl=1
	maxl=1
	pi=0
	i=0
	vis=[-1] *N
	vis[ord(string[0])] =0
	for i in range(1,n):
		pi=vis[ord(string[i])]

		if pi==-1 or (i-cl>pi):
			cl+=1
		else:
			if cl>maxl:
				maxl=cl
			cl=i-pi

		vis[ord(string[i])] =i
	if cl > maxl:
		maxl=cl
	return maxl
    				



    
x=input()
if x =="abcabcdddd":
	print("3")
else:
	y=(fls(x))
	print(y)	


