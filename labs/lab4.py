import math
import random
import numpy as np


def lfrs(x):
  t = 8760
  return ((((x[0] > t) & (x[1] > t)) | ((x[2] > t) & (x[3] > t))) &
          ((x[4] > t) & (x[5] > t)) &
          ((x[6] > t) | (x[7] > t) | (x[8] > t)) &
          ((x[9] > t) | (x[10] > t)))


def pt(L):
  N = 47500  # alpha = 0.95, eps = 0.001
  n = [4, 2, 3, 2]
  m = 4
  lam = [40 * 10 ** (-6), 10 * 10 ** (-6), 80 * 10 ** (-6), 30 * 10 ** (-6)]

  d = 0
  for k in range(N):
    x = []
    for i in range(m):
      t = []
      for j in range(n[i]):
        alpha = random.random()
        t.append(- math.log(alpha) / lam[i])
      for j in range(L[i]):
        l = np.argmin(t)
        t[l] -= math.log(random.random()) / lam[i]
      for j in range(n[i]):
        x.append(t[j])
    if not lfrs(x):
      d += 1
  return 1 - d / N


p0 = 0.995
L = [0] * 4
n_reserve = 4
for i in range(n_reserve - 2, n_reserve + 1):
L[0] = i
for j in range(n_reserve - 2, n_reserve + 1):
  L[1] = j
  for k in range(n_reserve - 2, n_reserve + 1):
    L[2] = k
    for t in range(n_reserve - 2, n_reserve + 1):
      L[3] = t
      p = pt(L)
      if p > p0:
        print("p =", round(p, 3), "  L =", L, "with sum =", sum(L))

