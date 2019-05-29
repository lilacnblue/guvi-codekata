n,k=input().split()
k=int(k)
arr=[int(x) for x in input().split()]
val=int(input())
t=val-(sum(arr)-arr[k])/2
if(t==0):
	print("Bon Appetit")
else:
	assert val==sum(arr)/2
	print(int(t))
