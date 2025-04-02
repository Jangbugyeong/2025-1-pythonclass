#2025.4.2 파이썬 수업 프로젝트 2
#콜라츠의 추측, 우박수
from sys import maxsize

#규칙: n이 짝수라면 n/2 n이 홀수라면 3배+1

i=0
n=99
for n in range(1,1000):
    i=0
    print(n)
    while n !=1:

        if n%2 == 0:
            n=n/2
            print(n)
            i=i+1
        else:
            n=3 * n + 1
            print(n)
            i=i+1
    print('반복수:',i)

max_i = 0

for n in range(1, 1000):
    current_n = n
    i = 0
    while current_n != 1:
        if current_n % 2 == 0:
            current_n = current_n / 2
        else:
            current_n = 3 * current_n + 1
        i += 1

    if i > max_i:
        max_i = i

print("i의 최대값:", max_i)
















