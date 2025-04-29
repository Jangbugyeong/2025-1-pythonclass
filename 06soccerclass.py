#2025.4.29
#객체지향 프로그래밍 실습



class SoccerPlayer(object):
    # 생성자 constructor
    # 객체 object가 생성될 때 자동 실행
    def __init__(self,name,position,back_number):
        self.name=name
        self.position=position
        self.back_number=back_number
        print('init 함수가 실행됨')
    def change_back_number(self,new_number):
        print(f'선수 번호 변경: {self.back_number} => {new_number}')
        self.back_number = new_number


# soccerplayer 클래스가 jh 오브젝트를 생성함
# 클래스의 생성함수 constructor가 실행
jh=SoccerPlayer('김종현','mf',10)

# jh 객체 출력
print(jh)

# jh 객체의 name을 출력
print(jh.name)

#백넘버 교체 실행
jh.change_back_number(5)

#교체된 백넘버 확인
print(f'{jh.back_number=}')