from math import ceil,log2
t=int(input())
n = ceil(log2((t+3)/6.0))
diff = t - 3*(2 ** n -1) -1
print(3 * 2 ** n - diff)
  
  
