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

    def __str__(self):
        return f'제 이름은 {self.name}, 포지션은 {self.position}, 번호는 {self.back_number} 입니다.'


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

names = ['Messi','Ramos','Ronaldo','park','son']
positions = ['mf','df','cf','wf','gk']
numbers = [10,9,8,7,1]

players = [[name,position,number] for name,position,number in zip(names,positions,numbers)]

print(players)
print(players[0])

messi = SoccerPlayer(players[0][1],players[0][1],players[0][2])
print(messi.name)

#선수들 리스트 생성
player_objects = [SoccerPlayer(name,position,number) for name,position,number in zip(names,positions,numbers)]
print(player_objects[0])

print(player_objects[0].name)

#모든 선수의 이름과 포지션 번호 출력

for player in player_objects:
    print(player)

