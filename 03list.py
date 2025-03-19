#2025.03.18
#파이썬 리스트 : 한 개의 변수에 여러 값을 할당



colors = ['red', 'blue', 'green']
print(colors[1]) #리스트 두번째 원소 출력
print(colors[-1]) #리스트 마지막 원소 출력
print(colors) #리스트 전체 출력
print(len(colors))#리스트 길이 출력

#슬라이싱
cities = ['서울', '부산', '인천','의정부', '대전', '강릉', '논산', '포항']
print(cities[:-1]) # 0~ -2까지
print(cities[0:5]) # cities[0:n] = 0~n-1까지 표시
print(cities[:7]) # 0~6까지 원소 출력
print(cities[3:]) # 3부터 끝까지 출력
print(cities[:]) # 전부 표시
print(cities[-4:])  # 뒤에서부터 4번째부터 표시
print(cities[:7:2]) #0부터 6번째 원소까지 2칸씩 띄워서 출력 [시작:끝:건너뛸 수 (n-1)]
print(cities[::3]) # 처음부터 끝까지 3칸씩 건너뜀
print(cities[::-1]) # 처음부터 끝까지, 거꾸로
print(cities[4::-2]) # 5번째 원소부터 처음까지, 2칸씩 건너뜀

#리스트 추가,삭제
colors = ['red', 'blue', 'green']
colors.append('while')  # 추가
print(colors[:])

colors.extend(['black', 'purple'])  # 여러 개 한 번에 추가
print(colors[:])

colors.insert(1, 'orange') # 원하는 칸에 삽입
print(colors[:])

colors.remove('purple') # 제거
print(colors[:])

colors[1] = 'sky' # 해당 칸의 원소를 바꾸기
print(colors[:])

# 패킹,언패킹
c1,_,c2,c3,_,_ = colors
print(c1,c2,c3)

#다차원 리스트
colors = ['red', 'blue', 'green']
cities = ['서울', '부산', '인천','의정부', '대전', '강릉', '논산', '포항']
combi = [colors,cities]
print(combi)
print(combi[1][2])  # 인천
#print(combi[2][3])  # 에러 발생
bigcombi = [combi, [0,2,7]]
print(bigcombi)
print(len(bigcombi))
print(bigcombi[0][1][2]) # 인천
print(bigcombi[1][-2])# 2
#퀴즈
first=['egg','salad','bread','soup','coffee']
second=['fish','lamb','pork','beef','chicken']
third=['apple','banana','orange','grape','mango']

order=[first,second,third]
john=[order[0][:-2],second[1::3],third[0]] # john=[soup,[lamb,chicken],[apple]]
del john[2] # john = [soup, [lamb,chicken]]
john.extend([order[2][0:1]]) # john = [soup, [lamb,chicken], [apple]]
print(john)