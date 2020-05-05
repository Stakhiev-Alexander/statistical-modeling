requiredP = 0.995
# alpha = 99% and E = 0.01
N = 5.41028 * 0.01 * 0.99 / (10 ** (-6))
print(f"N = {N}")
TOTAL_TIME = 8760
m = 4
blocks = [4, 2, 3, 2]
labmda = [40*(10^-6), 10*(10^-6), 80*(10^-6), 30*(10^-6)]

t = []

for i in blocks:
	t.append([j for j in range(i)])

print(t)


def getD(L):
	d = 0
	for