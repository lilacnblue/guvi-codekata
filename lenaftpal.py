import sys
def lps(st):
	n=len(st)
	table=[[0 for x in range(n)]for y in range(n)]
	maxl=1
	i=0
	while(i<n):
		table[i][i]=True
		i+=1

	start=0
	i=0
	while i < n-1:
		if(st[i]==st[i+1]):
			table[i][i+1]=True
			start=i
			maxl=2
		i+=1

	k=3
	while k<=n:
		i=0
		while i<(n-k+1) :
			j=i+k-1
			if(table[i+1][j-1]and st[i]==st[j]):
				table[i][j]=True
				if(k>maxl):
					start=i
					maxl=k
			i=i+1

		k=k+1
	return maxl

p=input()
q=int(len(p))
z=lps(p)
z=int(z)
print(q-z)