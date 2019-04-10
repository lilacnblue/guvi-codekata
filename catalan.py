n=int(input())

for i in range(n):
	print(c(i),end=" ")

def c(n):
	if n <= 1:
		return 1
	r=0
	
	for i in range(n):
		r+=c(i)*c(n-i-1)
	
	return r 	
	
	
	
