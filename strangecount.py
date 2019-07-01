from math import ceil,log2
t=input()
t=int(t)
n=ceil(log2(t/3+1))
start= 3 * (1 << (n-1))
ind = (t - 3 )*((1 << n-1) - 1) -1
print(range(start, 0, -1)[ind])
