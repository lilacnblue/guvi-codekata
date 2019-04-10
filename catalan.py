def catalan(n):
	if n <= 1:
		return 1
	r=0
	
	for i in range(n):
		r+=catalan(i)*catalan(n-i-1)
	
	return r 

n=int(input())

for i in range(n+1):
	print(catalan(i),end=" ")
