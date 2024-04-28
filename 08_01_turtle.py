# turtle 그림그리는 프로그램
# 기본문장
'''
import turtle

turtle.shape('turtle')

turtle.done()
'''
#---------------------
# 앞으로 가도록
'''
import turtle
turtle.shape('turtle')
turtle.forward(100)
turtle.done()
'''
#---------------------
# 앞으로 가고 옆으로 꺾는..
'''
import turtle
turtle.shape('turtle')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)

turtle.done()
'''
#---------------------
# 앞으로 가고 옆으로
'''
import turtle
turtle.shape('circle')

for i in range(100,0,-5):
    turtle.forward(i)
    turtle.right(90)
    turtle.speed(10)
turtle.done()
'''
#---------------------
'''
거북이의 방향
   앞(forward), 왼쪽(left), 오른쪽(right), 뒤(backward) 로 결정
커서의 방향
   classic, arrow, turtle, circle, square, triangle
turtle 함수
    turtle.shape('설정할 모양') -> 거북이의 모양 설정
    turtle.getshapes() -> 설정할 수 있는 모양들 반환
    turtle.color('red') -> 커서 색깔 설정
    turtle.penup() -> 펜을 들겠다(이동간, 선을 그리지 않음)
    turtle.pendown() -> 펜을 내리겠다.(이동간, 선을 그림)
    turtle.hideturtle()  -> 커서를 숨긴다
    turtle.showturtle()  -> 커서를 드러냄
    turtle.forward(x)  -> x 만큼 전진
    turtle.left(x)  -> 왼쪽으로 x만큼 돌아라
    turtle.right(x)  -> 오른쪽으로 x 만큼 돌아라
    turtle.speed(x)  -> 이동 스피드 조정(0~1)
'''
#---------------------
# 4각형을 for 문으로..
'''
import turtle

turtle.shape('turtle')

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()
'''
#---------------------
# 터틀모양 arrow, 라인색 blue, 라인두께 3, 회전left ~
'''
import turtle
turtle.shape('turtle')
turtle.pencolor('blue')
turtle.pensize(3)
turtle.left(180)
turtle.forward(50)
turtle.backward(30)
turtle.done()
'''
#--------------------------
# pencolor 위치의 차이
'''
import turtle
turtle.shape('turtle')
turtle.pencolor('blue')
turtle.pensize(6)
turtle.shapesize(1)
turtle.circle(100)  # 위치에 따라 결과가 다름
turtle.forward(300)
turtle.done()
'''
# pencolor 위치의 차이
'''
import turtle
turtle.shape('turtle')

turtle.pensize(6)
turtle.shapesize(1)
turtle.circle(100)  # 위치에 따라 결과가 다름
turtle.pencolor('blue')
turtle.forward(300)
turtle.done()
'''
#---------------------------
# 한변의 길이가 100인 삼각형, 펜컬러 red, 펜사이즈 3
'''
import turtle

turtle.shape('turtle')
turtle.pensize(3)
turtle.pencolor('red')

for i in range(3):
    turtle.forward(200)
    turtle.right(120)

turtle.done()
'''
#---------------------------
# 라인이 빨강, 파랑, 보라으로 길이가 150인 정삼각형
# 한변의 길이가 150인 삼각형, 펜컬러 red, 펜사이즈 3
'''
import turtle

turtle.shape('turtle')
turtle.pensize(3)
turtle.pencolor('red')
turtle.forward(150)
turtle.right(120)
turtle.pencolor('blue')
turtle.forward(150)
turtle.right(120)
turtle.pencolor('purple')
turtle.forward(150)
turtle.right(120)
turtle.done()
'''
#for 문으로
'''
import turtle

turtle.shape('turtle')
turtle.pensize(3)
for color in ['red','blue','purple']:
    turtle.pencolor(color)
    turtle.forward(150)
    turtle.right(120)

turtle.done()
'''
#---------------------------
#위 문제의 선의 길이, 두께를 입력값으로 -> for 문으로
'''
import turtle

size   = int(input('pensize(1~5): '))
length = int(input('length(100~200): '))
              
for color in ['red','blue','purple']:
    turtle.shape('turtle')
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.forward(length)
    turtle.right(120)

turtle.done()
'''
#---------------------------
# 중앙에서 직선 100개를 50간격으로(3개의 평행선)
'''
import turtle

turtle.shape('turtle')
turtle.forward(100)
turtle.penup()
turtle.backward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)

turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.backward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)

turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.backward(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)

turtle.pendown()
turtle.forward(100)
'''
#---------------------------
# 중앙에서 직선 100개를 50간격으로(3개의 평행선), 좌표를 이용
'''
import turtle

turtle.shape('turtle')
turtle.goto(0,0*-50)
turtle.down()
turtle.forward(100)
turtle.up()

turtle.goto(0,1*-50)
turtle.down()
turtle.forward(100)
turtle.up()

turtle.goto(0,2*-50)
turtle.down()
turtle.forward(100)
turtle.up()
'''
#---------------------------
# 위를 for 문으로
'''
import turtle

for i in range(3):
    turtle.shape('turtle')
    turtle.goto(0,i*-50)
    turtle.down()
    turtle.forward(100)
    turtle.up()

turtle.done()
'''
#---------------------------
'''
라인길이(length)입력받아서 6개의 수평선을 아래 조건으로 그리기
a = [0,100,40,30,70,10] # 선들의 상하간격
size = [2,1,3,6,3,5] # 선의 두께
color = ['red','blue','green','purple','orange','pink']
반복문과 리스트로
turtle.up()  # 삭제
turtle.goto(0,dis) # dis 위치로
'''
'''
import turtle

color = ['red','blue','green','purple','orange','pink']
a = [0,100,40,30,70,10] 
size = [2,1,3,6,3,5]
length = int(input('line length: '))
dis = 0

for i in range(6):
    turtle.shape('turtle')
    dis += a[i]
    turtle.goto(0,dis)
    turtle.pensize(size[i])
    turtle.pencolor(color[i])
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()
turtle.done()
'''
#---------------------------
# 별 그리기
# 라인길이 입력받고 별모양 만들기
# 선의 두께 --> size = [2,1,3,6,3]
# 색상값 -> color = ['red','blue','green','purple','orange']
# 별을 그리기 위한 각도 180-36
'''
import turtle
length = int(input('length : '))
size = [2,1,3,6,3]
color = ['red','blue','green','purple','orange']

for i in range(5):
    turtle.pensize(size[i])
    turtle.pencolor(color[i])
    turtle.forward(length)
    turtle.right(144)
turtle.done()
'''
#---------------------------
# 색칠하기
'''
import turtle

turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
'''
#---------------------------
# 반지름이 100인 원의 내접육각형
'''
import turtle

turtle.shape('turtle')
turtle.circle(100)
turtle.circle(100,steps = 6)
'''
#---------------------------
# 반지름이 100인 원의 내접3각형, 4각형~6각형까지
# 원: 빨강색, 나머지는 파란색,  -> for 문을 이용
'''
import turtle
turtle.pencolor('red')
turtle.speed(3)
turtle.pensize(10)
turtle.circle(100)

for i in range(3,7):
    turtle.pencolor('blue')
    turtle.circle(100,steps = i)
'''
#---------------------------
# 1이면 가로, 2이면 세로  직선을 그린다.
# 1이나 2가 아니면 직선을 그리지 않는다.
# 길이를 입력받는다.(색은 red)
'''
import turtle

line = int(input('1 or 2: '))

if line == 1:
    turtle.forward(100)
elif line == 2:
    turtle.right(90)
    turtle.forward(100)
else:
    pass
'''
#---------------------------
# 반지름이 50인 원을 그리고, 오른쪽으로 120도 회전하는 동작을 세번 반복하면서
# 원으로 구성된 삼각모양을 그린다.
# 지정된 색상['yellow','red','blue','purple']과 펜크기(1~10)를 임의로 선택
'''
import turtle
import random

for i in range(3):
    
    color = ['yellow','red','blue','purple']
    pencolor = random.choice(color)
    pensize  = random.randint(1,10)

    turtle.pencolor(pencolor)
    turtle.pensize(pensize)
    turtle.circle(50)
    turtle.right(120)
'''
#---------------------------
# x, y 좌표가 -400, 400 범위 내에서 3~6각형 크기(10~70) 두께(1,10) 랜덤하게
# 50분 반복 그린다.
# 도형색상 color = ['yellow','red','blue','purple', 'green'] 랜덤하게

import turtle
import random

color = ['yellow','red','blue','purple', 'green']


for i in range(50):
    turtle.up()
    turtle.goto(random.randint(-400,400), random.randint(-400,400))
    turtle.pencolor(random.choice(color))
    turtle.pensize(random.randint(1,10))
    turtle.down()
    turtle.circle(random.randint(10,70),steps = random.randint(3,6))    
    
