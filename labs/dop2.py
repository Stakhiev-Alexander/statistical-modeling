import numpy as np
import math
import random

beta = 20
size = 10000

def expon(beta, size):
  arr = []
  for i in range(size):
    arr.append(-beta * math.log(random.random()))
  return arr

def F(lamb, x):
  if x>=0:
    return 1-math.exp(-lamb*x)
  else:
    return 0  

arr = expon(beta, size)

print(f'N = {size}')
print(f'Beta = {beta}')
print()
print(f'M = {np.mean(arr)}')
print(f'D = {np.var(arr)}')

n = len(arr)
arr.sort()
u = (2*np.arange(1, n+1) - 1)/(2*n)
F_arr = [F(1/beta, x) for x in arr]
w = 1/(12*(n**2)) + np.sum((F_arr - u)**2) / n

print(f'omega**2 = {w}')
print(f'n * omega**2 = {n * w}')