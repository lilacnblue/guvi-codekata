n=int(input("")) 
a = []
for i in range (n):
    x=input()
    a.insert(i,x)
    i+=1
lp=""
sw = min(a, key=len)
for i in range(len(sw)):
	if all ([x.startswith(sw[:i+1]) for x in a]):
		lp=sw[:i+1]
	else:
		break
print(lp)
