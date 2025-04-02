#2025.4.2 파이썬 수업 프로젝트 2
#콜라츠의 추측, 우박수

#규칙: n이 짝수라면 n/2 n이 홀수라면 3배+1

i=0
n=99
for n in range(1,100):
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














