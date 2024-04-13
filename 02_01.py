#지역변수, 전역변수
'''
def func1():
    a = 10  # 지역변수
    print('func1에서 a값 %d' % a)

def func2():
    print('func2에서 a값 %d' % a) # 전역변수 a 출력, 전역변수 a 가 없으면 에러

a = 20 # 전역변수

func1()
func2()
'''
#
'''
def func1():
    global a #a를 전역변수로 바꾼다.
    a = 10 
    print('func1에서 a값 %d' % a)
# 전역변수 a값을 10으로 변경하므로
# func1()과 func2() 함수에서 모두 전역변수 a 값을 10으로 출력

def func2():
    print('func2에서 a값 %d' % a) 

global a
a = 20 # 전역변수

func1()
func2()
'''
#---------------------------
# 반환값
'''
def func1(): #반환값이 있는 경우
    result = 100
    return result
def func2(): #반환값이 없는 경우
    print("반환값이 없는 함수 실행")

hap = 0

hap = func1() #반환값이 100
print('func1에서 돌려준 값 => %d' % hap)

func2() #반환값이 없는 함수인 func2()를 호출하면 반환 않음
'''
#---------------------------
# return이 없는 경우
'''
def 지역변수사용시(x):
    x += 1
    print('x가 1증가했습니다.')   # return이 없는 경우
    
a = 10
지역변수사용시(a)
print(a)   # return이 없어서 a = 11이 아닌 a = 10이 출력된다.
'''
#---------------------------
# return이 있는 경우
'''
def 지역변수사용시(x):
    x += 1
    return x
    print('x가 1증가했습니다.')

a = 10
print(지역변수사용시(a))
'''
#---------------------------
# return을 사용안하고 global을 사용하는 경우
'''
def 전역변수사용시(x): #매개변수로 글로벌변수를 사용할 수 없다.
    global a
    a += 1
    print('x가 1증가했습니다.')

a = 10
전역변수사용시(a)
print(a)
'''
#---------------------------
# 반환값이 여러개인 함수
'''
def multi(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1) # 리스트에 값을 추가
    retList.append(res2)
    return retList # 리스트 반환

myList = []
hap, sub = 0,0

myList = multi(100,200) # 반환한 리스트의 값을 각 변수에 대입 
hap = myList[0]
sub = myList[1]

#print('multi()돌려준값 -> %d, %d' % (hap, sub))
print(f'multi()돌려준값 -> {hap}, {sub}')
'''
# ----------------------------
#아래내용을 보면 함수가 비슷한게 두개.. 이걸 합치는 방법은?
'''
def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0
hap = para2_func(10,20)
print('매개변수가 2개인 함수를 호출한 결과 -> %d' %hap)
hap = para3_func(10,20, 30)
print('매개변수가 3개인 함수를 호출한 결과 -> %d' %hap)
'''
# ----------------------------
#위에 함수두개를  한개로 합쳐보자
'''
def para4_func(v1, v2, v3=0):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0
hap = para4_func(10,20)
print('매개변수가 2개인 함수를 호출한 결과 -> %d' %hap)
hap = para4_func(10,20, 30)
print('매개변수가 3개인 함수를 호출한 결과 -> %d' %hap)
'''
# ----------------------------
#그런데, 위에서 매개변수가 10개인 경우?
'''
def para_func(v1, v2, v3=0, v4=0, v5=0, v6=0, v7=0, v8=0, v9=0, v10=0):
    result = 0
    result = v1 + v2 + v3 + v4 + v5+ v6 + v7 + v8 + v9 + v10
    return result

hap = 0
hap = para_func(10,20)
print('매개변수가 2개인 함수를 호출한 결과 -> %d' %hap)
hap = para_func(10,20,30,30,30,30,30,30,30,30)
print('매개변수가 3개인 함수를 호출한 결과 -> %d' %hap)
'''
# ----------------------------
#그런데, 위에서 매개변수가 10개인 경우? 아래와 같이 가능
'''
def para_func(*para):  #(*para)로 매개변수 설정.
                       #매개변수에 *를 붙이면 여러 개의 입력값(인자)를 하나의
                       #튜플로 받을 수 있다. 이러한 함수를 가변인자함수라고 한다.
    result = 0
    # result = v1 + v2 + v3 + v4 + v5+ v6 + v7 + v8 + v9 + v10 이 부분을 for 문으로.
    for num in para:
        result += num
    return result

hap = 0
hap = para_func(10,20)                             #(10,20)형식의 튜플로 전달
print('매개변수가 2개인 함수를 호출한 결과 -> %d' %hap)
hap = para_func(10,20,30,30,30,30,30,30,30,30)     #(10,20, ~~~)형식의 튜플로 전달
print('매개변수가 3개인 함수를 호출한 결과 -> %d' %hap)
'''
# ----------------------------
# 함수를 호출할 때 dictionary 형식의 매개변수를 키-값 형식으로 사용
'''
def dic_func(**para): # dictionary data는 **로 시작한다. * 1개는 tuple, *2개는 dict
    for k in para.keys():
        print('%s --> %d입니다.' %(k, para[k])) #키와 값의 형식으로 출력(k->키, para[k]->값)

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이=4, 블랙핑스 =4)
# 이렇게 하면 키:값의 dict 타입으로 **para로 전달
# 근데 이 경우 첨부터 dict로 주고, **para에서 **를 빼면 어케 되나?
'''
# 즉 {트와이스:9, 소녀시대:7, 걸스데이:4, 블랙핑스:4}
# ----------------------------
# 첨부터 dict type으로 해보는 것..(내가 개인적으로 하는 거임)
'''
def dic_func(para): # dictionary data는 **로 시작한다.
    for k in para.keys():
        print('%s --> %d입니다.' %(k, para[k])) #키와 값의 형식으로 출력(k->키, para[k]->값)

group = {트와이스:9, 소녀시대:7, 걸스데이:4, 블랙핑스:4}
dic_func(group)
'''
# 파이썬에서는 {키워드:인자}를 전달하는 함수도 생성할 수 있다
# 키워드 인자일 경우 매개변수명 앞에 **(별표2개)를 붙이면 된다.
# 키워드 인자로 전달하면 함수 내에서 딕셔너리로 인식한다.
# ----------------------------
# 로또 추첨(6개의 숫자를 출력)
# 크기순으로 정렬
# 난수발생(1~45) randrange(1,46)을 함수(getNumber)로 정의
# lotto = []
# 발생한 난수를 집어넣을 곳 list : lotto
# 변수의 숫자  : num, num= 0
# print(** 로또 추첨을 시작합니다. **
# 무한반복으로 숫자(6개)생성, (중복숫자 제외)
# 중복확인 lotto.count(num) == 0 이면 리스트에 추가
# 갯수 확인 후 무한반복 탈출
# 추첨번호 크기순으로 일렬 출력
'''
# 이건 내가 작성한것 
import random
lotto = []
while len(lotto) < 6:
    num = random.randrange(1,45)
    if lotto.count(num) == 0:
        lotto.append(num)
lotto1 = sorted(lotto)
print(lotto1)
'''
#강사 정답
import random
def getNumber():
    return random.randrange(1,46)
# random.randrage(시작값, 끝값)함수는 시작값~끝값-1 중에 임의의 숫자 1개를 추출,
# 이 함수를 사용하려고 import random을 입력
'''
lotto = []
num = 0
print('**로또추첨을 시작합니다.**\n')

while True:          # 무한반복으로 함수 호출
    num = getNumber()
    if lotto.count(num) == 0: #중복숫자 확인
        lotto.append(num)
    if len(lotto)>=6:
        break

print('추첨된 로또 번호 ==> ',end = '')
lotto.sort()

for i in range(0,6):
    print('%d' % lotto[i], end = ',')
'''
# ----------------------------
# 어떤 함수들이 시스템에 있는가?
'''
import sys
print(sys.builtin_module_names) # 파이썬 제공 표준 모듈의 목록
# 모듈안에 있는 함수들의 목록은? ex) math 함수
import math
dir(math)
'''
# ----------------------------
# 아래내용을 콘솔창에서 친다. (함수내 함수 설명)
'''
def outFunc(v1, v2):
    def inFunc(num1, num2):
        return num1 + num2
    return inFunc(v1,v2)

print(outFunc(10,20)) # 이거는 된다. 즉 이중함수도 가능하다.
                      # 근데, 함수 안에 있는 inFunc를 함수 밖에서 호출하면 에러가 난다.
print(inFunc(10,20))  # 즉 이거는 오류..
'''
# ----------------------------
'''
def hap(num1, num2):
    res = num1 + num2
    return res

print(hap(10,20))
'''
#이상의 내용을 람다함수로 만든다.
'''
hap2 = lambda num1, num2 : num1 + num2
hap2 = lambda num1, num2 : num1 + num2
print(hap2)
print(hap2(11,22))
hap3 = lambda num1 = 10, num2 = 20 : num1 + num2
print(hap3)
print(hap3())
print(hap3(100,200))
'''
# ----------------------------
'''
myList = [1,2,3,4,5]
def add10(num):
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])

    
print(myList)
[11, 12, 13, 14, 15]
'''
# ----------------------------
# 바로 위에 있는 걸, lambda와map 함수로 간단하게 표현
'''
myList = [1,2,3,4,5]
add10 = lambda num: num + 10
myList = list(map(add10, myList))
print(myList)
'''
# 이걸 더 간단하게..
'''
myList = [1,2,3,4,5]
myList = list(map(lambda num: num + 10, myList))
print(myList)
'''
# 이걸 더 간단하게..
print(list(map(lambda num: num + 10, [1,2,3,4,5])))
# 이건 lambda 함수를 이용하면 간단하게 표현할 수 있음을 보여주는..



