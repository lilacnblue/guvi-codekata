n,k=input().split()
k=int(k)
arr=[int(x) for x in input().split()]
val=int(input())
p=val-(sum(arr)-arr[k])/2
if(p==0):
	print("Bon Appetit")
else:
	assert val==sum(arr)/2
	print(int(p))
