#2025.03.19
#파이썬 수업, 조건문

grade = "아직 모름"
score = int(input("점수를 입력하세요:"))
if score > 60:
    grade = "합격"
else:
    if score > 50:
        grade = "임시 합격"
    else:
       grade = "불합격"
print(grade)

if score>=90:
    grade='A'
if score>=80:
    grade='B'
if score >= 70:
    grade = 'c'

else:
    grade = 'f'
    print(grade)

    score = int(input("Enter your score: "))

    if score >= 90:
        grade = 'A'  # 90 이상일 경우 A
    elif score >= 80:
        grade = 'B'  # 80 이상일 경우 B
    elif score >= 70:
        grade = 'C'  # 70 이상일 경우 C
    elif score >= 60:
        grade = 'D'  # 60 이상일 경우 D
    else:
        grade = 'F'  # 모든 조건에 만족하지 못할 경우 F

    print(grade)
