#파이값구하기 오일러공식 이용

pi=1
n=1
pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2

n=2
pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2

print(pi*4)

pi=1

for n in range(1,100):
    pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2

print(pi*4)

import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()

import opencv


