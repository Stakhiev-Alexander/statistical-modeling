import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

n = 10
size = 100000
mu = 10
N = 10
p = 0.5
ILOW = 1
IUP = 100

def cumulative_dist_function_graph(arr):
  kwargs = {'cumulative': True}
  sns.distplot(arr, bins=20, hist_kws = kwargs, kde_kws=kwargs)

def probability_density_function_graph(arr):
  sns.distplot(arr, bins=20, kde=True)



def ravn(ILOW, IUP,size):
  arr = []
  for i in range(size):
    arr.append((IUP - ILOW + 1)*random.random() + ILOW)
  return arr


def bin_general(size, n, p):
  pk = [math.factorial(n) / math.factorial(r) / math.factorial(n - r) * p ** r * (1 - p) ** (n - r) for r in range(n)]
  arr = []
  for i in range(size):
    r = random.random()
    for j in range(n):
      r -= pk[j]
      if r <= 0:
        arr.append(j)
        break
  return arr


def bin_rekur(size,n,p):
  arr = []
  for i in range(size):
    pk = (1 - p) ** n
    r = random.random()
    for j in range(n):
      r -= pk
      if r <= 0:
        arr.append(j)
        break
      pk = pk*((n - j) / (j + 1)) * (p / (1 - p))  
  return arr


def rekur_geom1 (size,p):
  arr = []
  for i in range(size):
    pk = p
    r = random.random()
    j=1
    while r > 0:
      r -= pk
      if r <= 0:
        arr.append(j)
        break
      pk = pk*(1-p)
      j = j + 1
  return arr


def rekur_geom2 (size,p):
  arr = []
  for i in range(size):
    j=1
    while True:
      r = random.random()
      if r <= p:
        arr.append(j)
        break
      j = j + 1
  return arr


def rekur_geom3 (size,p):
  arr = [math.floor(math.log(random.random())/math.log(1-p)+1) for i in range(size)]
  return  arr


def puas1(size,mu):
  arr = []
  for i in range(size):
    pk = math.e ** (-mu)
    r = random.random()
    j = 1
    while True:
      r -= pk
      if r <= 0:
        arr.append(j)
        break
      pk = pk*mu/j
      j = j + 1
  return arr


def puas2(size,mu):
  arr = []
  for i in range(size):
    pk = math.e ** (-mu)
    r = random.random()
    j = 1
    while True:
      if r <= pk:
        arr.append(j)
        break
      r = r*random.random()
      j = j + 1
  return arr


def log(size,p):
  arr = []
  alpha = 1 / math.log(p)
  q = 1 - p
  for i in range(size):
    j = 1
    pk = -alpha*q**j/j
    r = random.random()
    while True:
      r -= pk
      if r <= 0:
        arr.append(j)
        break
      j = j + 1
      pk = -alpha*q**j/j
  return arr



def M(arr):
  M = sum(arr)/len(arr)
  return M


def D(M,arr):
  D = 0
  for i in arr:
    D += (i - M)**2

  D /= len(arr)
  return D


print("Uniform:")
mat = M(ravn(ILOW, IUP, size))
dis = D(mat,ravn(ILOW, IUP, size))
print('M = ' + str(mat) + '  M = 50.5 ' + '  M = ' + str(mat-50.5))
print('D = ' + str(dis) + '  D = 833.25 ' + '  D = ' + str(dis-833.25))

print("Binominal general:")
mat = M(bin_general(size, n, p))
dis = D(mat,bin_general(size, n, p))
print('M = ' + str(mat) + '  M = 5.0 ' + '  M = ' + str(mat-5.0))
print('D = ' + str(dis) + '  D = 2.5 ' + '  D = ' + str(dis-2.5))

print("Binominal rekur:")
mat = M(bin_rekur(size, n, p))
dis = D(mat,bin_rekur(size, n, p))
print('M = ' + str(mat) + '  M = 5.0 ' + '  M = ' + str(mat-5.0))
print('D = ' + str(dis) + '  D = 2.5 ' + '  D = ' + str(dis-2.5))

print("Geometric rekur1:")
mat = M(rekur_geom1(size, p))
dis = D(mat,rekur_geom1(size, p))
print('M = ' + str(mat) + '  M = 2.0 ' + '  M = ' + str(mat-2.0))
print('D = ' + str(dis) + '  D = 2.2 ' + '  D = ' + str(dis-2.2))

print("Geometric rekur2:")
mat = M(rekur_geom2(size, p))
dis = D(mat,rekur_geom2(size, p))
print('M = ' + str(mat) + '  M = 2.0 ' + '  M = ' + str(mat-2.0))
print('D = ' + str(dis) + '  D = 2.2 ' + '  D = ' + str(dis-2.2))

print("Geometric rekur3:")
mat = M(rekur_geom3(size, p))
dis = D(mat,rekur_geom3(size, p))
print('M = ' + str(mat) + '  M = 2.0 ' + '  M = ' + str(mat-2.0))
print('D = ' + str(dis) + '  D = 2.2 ' + '  D = ' + str(dis-2.2))

print("Poisson alg1:")
mat = M(puas1(size, mu))
dis = D(mat,puas1(size, mu))
print('M = ' + str(mat) + '  M = 10.0 ' + '  M = ' + str(mat-10.0))
print('D = ' + str(dis) + '  D = 10.0 ' + '  D = ' + str(dis-10.0))

print("Poisson alg2:")
mat = M(puas2(size, mu))
dis = D(mat,puas2(size, mu))
print('M = ' + str(mat) + '  M = 10.0 ' + '  M = ' + str(mat-10.0))
print('D = ' + str(dis) + '  D = 10.0 ' + '  D = ' + str(dis-10.0))

print("Logarithmic:")
mat = M(log(size, p))
dis = D(mat,log(size, p))
print('M = ' + str(mat) + '  M = 1.44270 ' + '  M = ' + str(mat-1.44270))
print('D = ' + str(dis) + '  D = 0.80402 ' + '  D = ' + str(dis-0.80402))


plt.subplot(5, 5, 1)
cumulative_dist_function_graph(ravn(ILOW, IUP, size))
plt.subplot(5, 5, 2)
probability_density_function_graph(ravn(ILOW, IUP, size))


plt.subplot(5, 5, 6)
cumulative_dist_function_graph(bin_rekur(size, n, p))
plt.subplot(5, 5, 7)
probability_density_function_graph(bin_rekur(size, n, p))


plt.subplot(5, 5, 11)
cumulative_dist_function_graph(rekur_geom3(size, p))
plt.subplot(5, 5, 12)
probability_density_function_graph(rekur_geom3(size, p))


plt.subplot(5, 5, 16)
cumulative_dist_function_graph(puas2(size, mu))
plt.subplot(5, 5, 17)
probability_density_function_graph(puas2(size, mu))


plt.subplot(5, 5, 21)
cumulative_dist_function_graph(log(size, p))
plt.subplot(5, 5, 22)
probability_density_function_graph(log(size, p))

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
