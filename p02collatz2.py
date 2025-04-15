#2025.4.9 우박수 프로젝트 2 : 기본 통계량 구하기
#numpy list 두 가지 방식으로 시험
#구하는 통계량 : 평균,중앙값,표준편차,최빈값,최대값
import statistics
from audioop import reverse
from operator import index

import numpy as np
import time

from PyQt6.sip import delete
from numpy.ma.core import argsort

from p02collatzfunc import collatz, find_max,second_largest
from p02collatz import ncount

MAXNUM=100



#list방식

start=time.time()
ncountl = []

for n in range(1,MAXNUM):
    ncount=collatz(n)
    ncountl.append(ncount)


nmax=0
print(sum(ncountl)/len(ncountl))
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl):.5f}')
#print(f'최빈값={statistics.mode(ncountl):.5f}')
print(f'표준편차={statistics.pstdev(ncountl):.5f}')
print(f'최대값={max(ncountl)}')
print(f'해당숫자={ncountl.index(max(ncountl))+1}')
print('두 번째로 큰 값 = ',sorted(ncountl, reverse=True)[1])
print(f'해당 숫자 = {ncountl.index(sorted(ncountl, reverse=True)[1])+1}')
print('세 번째로 큰 값 = ',sorted(ncountl, reverse=True)[2])
print(f'해당 숫자 = {ncountl.index(sorted(ncountl, reverse=True)[2])+1}')
end = time.time()
print(f'{end-start:.5f} 초가 걸렸습니다.')

#numpy방식
start2=time.time()

ncounta=np.zeros(MAXNUM-1)
for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncounta[n-1]=ncount
ncounta_sorted=np.argsort(ncounta)
unique = np.unique(ncounta)
if unique.size >= 2:
    second_largest = unique[-2]
    third_largest = unique[-3]
print(f'최대값 해당숫자={np.argmax(ncounta)+1}')
print(f'평균={ncounta.mean():.5f}')
print(f'중앙값={np.median(ncounta):.5f}')
print(f'표준편차={np.std(ncounta):.5f}')
print(f'최대값={np.max(ncounta)}')
print(f'두 번째로 큰 값 = {second_largest}')
print(f'해당 숫자 = {ncounta_sorted[-2]+1}')
print(f'세 번째로 큰 값 = {third_largest}')
print(f'해당 숫자 = {ncounta_sorted[-3]+1}')
end2=time.time()
print(f'{end2-start2:.5f} 초가 걸렸습니다.')
#print(f'최빈값={np.bincount(ncounta).argmax(ncounta)}')

#print(sum(ncountl)/len(ncountl))
#print(f'평균={statistics.mean(ncountl):.5f}')
#print(f'최대값={max(ncountl)}')
