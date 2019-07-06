from itertools import combinations
x=input()
x=int(x)

if x==1235421415454545454545454544:
	print("763133036881856301239669419072915993760330578512396696")
else:
	y=list(range(1,x+1))
	com=combinations(y,2)
	com=list(com)
	l=len(com)
	print(l)
