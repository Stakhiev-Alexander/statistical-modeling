import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

n = 1000

def cumulative_dist_function_graph(arr):
  kwargs = {'cumulative': True}
  sns.distplot(arr, bins=20, hist_kws = kwargs, kde_kws=kwargs)



def probability_density_function_graph(arr):
  sns.distplot(arr, bins=20)


u = []
for i in range(n):
  u.append(random.random())

M = sum(u)/n

D = 0
for i in range(n):
  D += (u[i] - M)**2

D /= n
S = D ** 0.5

K = []

for f in range(1, n):
  sum1 = 0
  sum2 = 0

  for i in range(1, n-f):
    sum1 += (u[i] - M) * (u[i+f] - M)

  for j in range(1, n):
    sum2 += (u[j] - M) ** 2  

  K.append(sum1/sum2)

print(f"M = {M}") 
print(f"D = {D}") 
print(f"S = {S}") 


plt.subplot(2, 2, 1)
plt.bar(range(n-1), K)
plt.title("Кореллограмма")


plt.subplot(2, 2, 2)
cumulative_dist_function_graph(u)
plt.title("Функция распределения")


plt.subplot(2, 2, 3)
probability_density_function_graph(u)
plt.title("Плотность распределения")

# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()
plt.show(K)