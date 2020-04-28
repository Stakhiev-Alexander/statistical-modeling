import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math



def cumulative_dist_function_graph(arr):
  kwargs = {'cumulative': True}
  sns.distplot(arr, bins=20, hist_kws = kwargs, kde_kws=kwargs)


def probability_density_function_graph(arr):
  sns.distplot(arr, bins=20, kde=True)


def M(arr):
  M = sum(arr)/len(arr)
  return M


def D(M,arr):
  D = 0
  for i in arr:
    D += (i - M)**2

  D /= len(arr)
  return D


def ravn(a, b, size):
  arr = []
  for i in range(size):
    arr.append((b - a)*random.random() + a)
  return arr


def norm1(size):
  arr = []
  for i in range(size):
    rn = 0
    for j in range(12):
      rn = rn + random.random()
    z = rn - 6
    arr.append(z)
  return arr


def norm2(beta, size):
  arr = []
  for i in range(size):
    arr.append(math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random()))
  return arr


def expon(beta, size):
  arr = []
  for i in range(size):
    arr.append(-beta * math.log(random.random()))
  return arr


def hi_kv(size):
  arr = []
  for i in range(size):
    yn = 0
    for j in range(10):
      yn = yn + random.normalvariate(0,1)**2
    arr.append(yn)
  return arr


def stud(size):
  arr = []
  for i in range(size):
    yn = 0
    for j in range(10):
      yn = yn + random.normalvariate(0, 1)**2
    arr.append(random.normalvariate(0,1)/math.sqrt(yn/10))
  return arr

a = 1
b = 100
size = 100000
beta = 1

arr = ravn(a, b, size)
mat = M(arr)
dis = D(mat, arr)
print("Ravn:")
print("{:.3f}".format(mat))
print("{:.3f}".format(dis))
print("M = {:.3f}".format(mat) + '  M(teor) = 50.5  ' + '  deltaM = {:.3f}'.format(abs(mat-50.5)))
print("M = {:.3f}".format(dis) + '  D(teor) = 816.75' + '  deltaD = {:.3f}'.format(abs(dis-816.75)))

arr = norm1(size)
mat = M(arr)
dis = D(mat, arr)
print("Norm1:")
print("M = {:.3f}".format(mat) + '  M(teor) = 0.0  ' + '  deltaM = {:.3f}'.format(abs(mat)))
print("M = {:.3f}".format(dis) + '  D(teor) = 1.0  ' + '  deltaD = {:.3f}'.format(abs(dis-1)))

arr = norm2(beta, size)
mat = M(arr)
dis = D(mat, arr)
print("Norm2:")
print("M = {:.3f}".format(mat) + '  M(teor) = 0.0  ' + '  deltaM = {:.3f}'.format(abs(mat)))
print("M = {:.3f}".format(dis) + '  D(teor) = 1.0  ' + '  deltaD = {:.3f}'.format(abs(dis-1)))

arr = expon(beta, size)
mat = M(arr)
dis = D(mat, arr)
print("Expon:")
print("M = {:.3f}".format(mat) + '  M(teor) = 1  ' + '  deltaM = {:.3f}'.format(abs(mat-1)))
print("M = {:.3f}".format(dis) + '  D(teor) = 1  ' + '  deltaD = {:.3f}'.format(abs(dis-1)))

arr = hi_kv(size)
mat = M(arr)
dis = D(mat, arr)
print("Hi kv:")
print("M = {:.3f}".format(mat) + '  M(teor) = 10  ' + '  deltaM = {:.3f}'.format(abs(mat-10)))
print("M = {:.3f}".format(dis) + '  D(teor) = 20  ' + '  deltaD = {:.3f}'.format(abs(dis-20)))

arr = stud(size)
mat = M(arr)
dis = D(mat, arr)
print("Stud:")
print("M = {:.3f}".format(mat) + '  M(teor) = 0.0  ' + '  deltaM = {:.3f}'.format(abs(mat)))
print("M = {:.3f}".format(dis) + '  D(teor) = 1.25 ' + '  deltaD = {:.3f}'.format(abs(dis-1.25)))

plt.subplot(5, 5, 1)
cumulative_dist_function_graph(ravn(a, b, size))

plt.subplot(5, 5, 2)
probability_density_function_graph(ravn(a, b, size))


plt.subplot(5, 5, 6)
cumulative_dist_function_graph(norm1(size))

plt.subplot(5, 5, 7)
probability_density_function_graph(norm1(size))


plt.subplot(5, 5, 11)
cumulative_dist_function_graph(expon(beta, size))

plt.subplot(5, 5, 12)
probability_density_function_graph(expon(beta, size))


plt.subplot(5, 5, 16)
cumulative_dist_function_graph(hi_kv(size))

plt.subplot(5, 5, 17)
probability_density_function_graph(hi_kv(size))


plt.subplot(5, 5, 21)
cumulative_dist_function_graph(stud(size))

plt.subplot(5, 5, 22)
probability_density_function_graph(stud(size))



mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()
