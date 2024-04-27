# 동전게임
# 동전의 앞과 뒤를 발생시키는 프로그램
# coin의 앞을 0, 뒤를 1
'''
import random
from tkinter import *
coin = random.randint(0,1)

window = Tk()

if coin == 0:
    t1 = '앞면입니다.'
else:
    t1 = '뒷면입니다.'

window.title('coin flip game')
window.geometry('400x600')

label2 = Label(window, text = t1)
label3 = Label(window, text = 'game over')

label2.pack()
label3.pack()
'''
#--------------------------------------
# 축구게임
# 사용자로부터 아이디를 받아서 프로그램에 저장된 아이디와
# 일치하는지 여부를 출력하는 프로그램
# 사용자(user) : 수비
# 컴퓨터(computer) : 공격(왼쪽, 중앙, 오른쪽 랜덤하게 선택되게..)
'''
import random

defence = input('left(L), center(C), right(R) ; ')
offence = random.choice(['L','C','R'])

if defence == offence:
    print(f'defence is {defence}, offence is {offence}, user win')
else:
    print(f'defence is {defence}, offence is {offence}, computer win')
'''
#--------------------------------------
# N을 랜덤으로 받고, 사용자에게 '홀','짝'을 입력받은 뒤,
# 사용자가 맞았는지, 틀렸는지 구분하는 프로그램을
'''
import random

user = input('사용자 선택: ')
n = random.randint(10,99)

if (n % 2 == 0) & (user == '짝'):
    print(f'user : {user}, computer : {n}, user win')
elif (n % 2 == 1) & (user == '홀'):
    print(f'user : {user}, computer : {n}, user win')
else:
    print(f'user : {user}, computer : {n}, computer win')
'''
# 강사 작성
# 지금 뭔가 틀림, 강사의 짝수와 홀수를 내가 바꿨더니 값이 틀리게 나옴.
'''
import random

while True:
    n = random.randint(10,99)
    user = int(input('사용자 선택(짝수 : 0, 홀수 : 1): '))

    if n % 2 == 1:         # 컴퓨터 : 홀수
        if user == 0:      # user   : 짝수
            print('wrong1')
        else:
            print('correct1')
    else:                  # 컴퓨터 : 짝수
        if user == 0:      # user   : 짝수
            print('correct2')
        else:
            print('wrong2')

    print('컴퓨터의 숫자는 %d 이었습니다.' % n)
    print('='*80)
'''
#--------------------------------------
# 게임적인 요소 첨가
# 생명(life) 5개(틀리면 -1), life == 0 이면 game over 메시지와 종료
# 점수(score) 0점(맞으면 +100), 게임 종료 후 점수 출력
# 출력문장 : 현재 점수와 라이프 숫자
# 게임오버시 총점수
''' 아래와 같이 해도 되고..
import random

life  = 5
score = 0

while life > 0:
    n = random.randint(10,99)
    user = int(input('사용자 선택(짝수 : 0, 홀수 : 1): '))

    if n % 2 == 1:         # 컴퓨터 : 홀수
        if user == 0:      # user   : 짝수
            print('wrong1')
            life -= 1
        elif user == 1:
            print('correct1')
            score += 100
    else:                  # 컴퓨터 : 짝수
        if user == 0:      # user   : 짝수
            print('correct2')
            score += 100
        elif user == 1:
            print('wrong2')
            life -= 1

    print('컴퓨터의 숫자는 %d 이었습니다.' % n)
    print(f'점수는 {score}, life는 {life}')
    print('='*80)

print(f'최종 점수는 {score}')
'''
#--------------------------------------
# 홀짝게임 아래와 같이 하나씩 추가
# 프로그램을 만들때, 첨부터 거창하게 만드는 것이 아닌 간단하게 만들어서
# 하나씩 업그레이드 시켜나가는 것임
'''
import random
import time
import os

life  = 5
score = 0

while True:
    if life == 0:
        print('game over')
        break

    n = random.randint(10,99)
    print('현재 life', life, ', 현재점수', score)
    user = int(input('사용자 선택(짝수 : 0, 홀수 : 1): '))

    if n % 2 == 1:         # 컴퓨터 : 홀수
        if user == 0:      # user   : 짝수
            print('wrong1')
            life -= 1
        elif user == 1:
            print('correct1')
            score += 100
    else:                  # 컴퓨터 : 짝수
        if user == 0:      # user   : 짝수
            print('correct2')
            score += 100
        elif user == 1:
            print('wrong2')
            life -= 1    
    print('컴퓨터의 숫자는', n, '이었습니다.')
    print()
    time.sleep(1)
    os.system('cls')
'''
#--------------------------------------
# up-down 게임.
# 두자리 숫자로 하나의 수를 랜덤으로 받고, 사용자에게 수를 입력
# 사용자의 대답에 따라 up, down, correct 세가지의 상황을 판별하는 프로그램
'''
import random
import time
import os

computer = random.randint(10,99)
count = 0

while True:
    user     = int(input('두자리 숫자 입력: '))
    if computer > user:
        print('your number is low')
        count += 1
    elif computer < user:
        print('your number is high')
        count += 1
    else:
        print('correct')
        count += 1
        print(f'{count}번만에 맞추었습니다.')
        break
    print('-'*30)
    time.sleep(0.5)
    os.system('cls')
'''
#--------------------------------------
# 연산게임
# random 두수 a, b(컴퓨터)의 덧셈을 맞추는 프로그램을 작성하세요.
# -> 결과는 변수c(컴퓨터 정답), user(사용자답)
# 예) 77+66=145
# 맞았습니다.(맞았습니다. 틀렸습니다.) 둘중에 하나 출력
# 2단계 : 
'''
import random

a = random.randint(10,99)
b = random.randint(10,99)
c = a + b
count = 0
print(f'{a} + {b}의 합은?')

while True:
    user = int(input('정답: '))
    count += 1
    if c == user:
        print(f'correct, {count}번 만에 맞춤')
        break
    else:
        print('wrong')
'''
#--------------------------------------
# 2단계 :
# 위 문제를 맞추면 점수(score)를 획득하고, 틀리면 라이프가 깎이에
# life 5개가 0일때 게임종료(시스템 종료)
# 점수는 맞출때마다 +100
# 정답제출 1초 뒤에 1문제씩 추가
# 현재 목숨과 점수가 문제시작할때 출력
# 무한반복 조건에 문제마다 현재목숨, 현재점수

# 요건 내가 푼것
'''
import random
import time

count = 0
life = 5
score = 100
    
while True:
    if life ==0:
        break

    a = random.randint(10,99)
    b = random.randint(10,99)
    c = a + b
    

    print(f'{a} + {b}의 합은?')
    
    user = int(input('정답: '))
    count += 1
    print(f'life : {life}, score: {score}')
    if c == user:
        print(f'correct, {count}번 만에 맞춤')
        score += 100
        break
    else:
        print('wrong')
        life -= 1
    time.sleep(0.5)
    print('-'*30)
'''
# 요건 강사 답
'''
import random
import time
import os

life = 5
score = 0
while True:
    if life == 0:
        break
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(f'life = {life}, score = {score}')

    print(a, "+", b, "=", end = '')
    c = a + b

    user = int(input())
    if c == user:
        score += 100
        print('correct')
    else:
        life -= 1
        print('wrong')
    time.sleep(0.5)
    print()
    os.system('cls')
'''
# 요건 강사 답
'''
import random
import time
import os

life = 5
score = 0
while True:
    if life == 0:
        break
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(f'life = {life}, score = {score}')

    print(a, "+", b, "=", end = '')
    c = a + b

    user = int(input())
    if c == user:
        score += 100
        print('correct')
    else:
        life -= 1
        print('wrong')
    time.sleep(0.5)
    print()
    os.system('cls')
# 3단계 : 객관식으로(이건 나중에 내가 해볼 것)
'''
#--------------------------------------
# 위 문제에서 다양한 연산(-) 문제가 나오도록
# op (연산자변수 0(+), 1(-) 랜덤하게 선택되도록
'''
import random
import time
import os

life = 5
score = 0
while True:
    if life == 0:
        break
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(f'life = {life}, score = {score}')

    op = random.choice(['plus','minus'])

    if   op == 'plus':
        c = a + b
    elif op == 'minus':
        c = a - b

    print(a, op, b, "=", end = '')
    
    user = int(input())
    if c == user:
        score += 100
        print('correct')
    else:
        life -= 1
        print('wrong')
    time.sleep(0.5)
    print()
    os.system('cls')
print(f'final score is {score}')
'''
#--------------------------------------
# 위 문제에서 1/5확률로 200점짜리 문제와 메시지가 출력되고
# 1/4 확률로 life가 2개 걸린 문제와 메세지가 출력되도록
# 1/5확률 같은건 변수 5개 중 한개를 골라서 그게 되면 1/5로 하는 방법을 쓰면 됨.
import random
import time
import os

life = 5
score = 0
while True:
    if life == 0:
        break
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(f'life = {life}, score = {score}')

    op = random.choice(['plus','minus'])

    if   op == 'plus':
        c = a + b
    elif op == 'minus':
        c = a - b

    print(a, op, b, "=", end = '')
    
    user = int(input())
    if c == user:
        score += 100
        print('correct')
    else:
        life -= 1
        print('wrong')
    time.sleep(0.5)
    print()
    os.system('cls')
print(f'final score is {score}')

#--------------------------------------
# 10초 안에 푸는..
# time.time 을 이용하여 푼다.
# start_time = time.time

# time.time - start_time()
