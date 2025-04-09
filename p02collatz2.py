#2025.4.9 우박수 프로젝트 2 : 기본 통계량 구하기
#numpy list 두 가지 방식으로 시험
#구하는 통계량 : 평균,중앙값,표준편차,최빈값,최대값
import statistics
import numpy as np
import time
from p02collatzfunc import collatz
from p02collatz import ncount

MAXNUM=100



#list방식

start=time.time()
ncountl = []

for n in range(1,MAXNUM):
    ncount=collatz(n)
    ncountl.append(ncount)

print(sum(ncountl)/len(ncountl))
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl):.5f}')
#print(f'최빈값={statistics.mode(ncountl):.5f}')
print(f'표준편차={statistics.pstdev(ncountl):.5f}')
print(f'최대값={max(ncountl)}')
end = time.time()
print(f'{end-start:.5f} 초가 걸렸습니다.')

#numpy방식
start2=time.time()

ncounta=np.zeros(MAXNUM-1)
for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncounta[n-1]=ncount

print(f'평균={ncounta.mean():.5f}')
print(f'중앙값={np.median(ncounta):.5f}')
print(f'표준편차={np.std(ncounta):.5f}')
print(f'최대값={np.max(ncounta)}')
end2=time.time()
print(f'{end2-start2:.5f} 초가 걸렸습니다.')
#print(f'최빈값={np.bincount(ncounta).argmax(ncounta)}')

#print(sum(ncountl)/len(ncountl))
#print(f'평균={statistics.mean(ncountl):.5f}')
#print(f'최대값={max(ncountl)}')
