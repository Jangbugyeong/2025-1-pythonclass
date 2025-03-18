##2025.3.12
##파이썬 수업 - 변수,타입,출력
##타입(형태) - 정수 : int(integer)
         ## - 실수 : float(floating point)
         ## - 문자열 : str(string)
         ## - 논리값 : bool(boolean)
title = "시간계산"
sec = 3700
min = sec / 60
bigger = min > sec
print(sec,min,bigger)
print(type(title), type(sec), type(min), type(bigger))

a=int(10.9)
b=float(10.3)
c=str(10.3)
print(type(a), type(b), type(c))
print(a)

sec1 = 3100; sec2 = 120
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2
secd = sec1 / sec2
secq = sec1 // sec2
secr = sec1 % sec2
print(f'{seca=},{secs=},{secm=},{secd=},{secq=},{secr=}')
##화씨를 섭씨로 바꾸기
#tc=(tf-32)*5/9
#tf=(tc*9/5)+32
tf=100
tc=(tf-32)*5/9
print(f'{tc=}')
tc=37.7
tf=(tc*9/5)+32
print(f'{tf=}')

print(2**3,2**(1/2),2**(-1/2))
#0으로 나누는 것은 허용되지않음
print(1/0)



