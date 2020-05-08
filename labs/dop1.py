import random
import numpy as np

def stirling(a, b):
    if a == b or (b == 1 and a > 0):
        return 1
    if b == 0 or a < b:
        return 0
    return stirling(a - 1, b - 1) + b * stirling(a - 1, b)

n = 10000
m = 3
t = 100
d = 2 ** m - 1
r = 2 ** m

print(f"n = {n}")
print(f"m = {m}")
print(f"t = {t}")

numbers = np.array([random.randint(0, d) for _ in range(n)])
# numbers = np.array([0, 1, 5, 0, 1, 3, 2, 2, 2, 3, 0, 1, 0, 2, 3, 1, 1, 1, 1, 1, 0, 3, 3, 3, 5, 1, 2])

k = n // t
numbers.resize(k, t) 

repetitions_list = [0 for _ in range(r+1)]
for number_list in numbers:
  (unique, counts) = np.unique(number_list, return_counts=True)
  frequencies = np.asarray((unique, counts)).T
  repetitions_list[len(frequencies)] += 1

def invFactorial(k):
  res = 1
  for i in range(1, k):
    res *= (d - i)
  return res  

p = []
for i in range(r+1):
  if repetitions_list[i] > 0:
    p.append(d*invFactorial(i)*stirling(k, i)/d**k)
  else:
    p.append(0)  

print(f'repetitions_list = {repetitions_list}')  
print(f'p = {p}')  

hi2obs = 0
for p_i, v_i in zip(p, repetitions_list):
  if v_i > 0:
    hi2obs += ((v_i - n/t * p_i)**2) / (n/t * p_i)

print(f"x**2(obs) = {hi2obs}")    
print(f"number of degrees of freedom = {r-1}")
