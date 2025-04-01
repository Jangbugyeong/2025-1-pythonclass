#파이값구하기 오일러공식 이용

pi=1
n=1
pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2

n=2
pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2

print(pi*4)

pilist = [

]

pi=1

for n in range(1,1000):
    pi=pi*((2 * n + 1) ** 2 - 1) / (2*n + 1) ** 2
  #  print(pi*4, ',')
    pilist.append(pi*4)

print(pi*4)


import matplotlib.pyplot as plt
plt.plot(pilist)
plt.show()



