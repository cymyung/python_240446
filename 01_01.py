#  아래와 같이 함수부분과 main code 부분으로 나누어 진다.

# 함수선언 부분
'''
def plus(v1, v2):  #def(함수를 사용자가 정의한다는 예약어) plus(함수이름, 함수는 무조건 괄호) v1, v2(매개변수), 2.함수실행
    result = 0
    result = v1 + v2
    return result  # 3. 함수반환(300의 결과값을 호출한 곳으로 반환)

# main code 부분
hap = 0
hap = plus(100,200) # 1. 함수호출(100과 200의 매개변수로 함수를 호출) 4. 함수대입(300의 결과값을 hap에 대입)
print('100과 200의 plus()의 결과는 %d' %hap)
'''
# main code 부분부터 읽는다.
# 그 다음 plus 함수가 있으므로, plus 함수로 가서 함수를 호출
# 1.함수호출 -> 2.함수실행 -> 3.함수반환 -> 4.함수대입 4단계로 이루어진다.(3,4단계는 생략가능)


# 함수의 개념과 필요성
# 함수(function) : 무엇을 넣으면 어떤것을 돌려주는 요술상자
# 메서드(method)와의 차이점 : 함수는 외부에 별도로 존재, 메서드는 클래스 안에 존재
# 함수의 형식
# 함수명 () ==> print('안녕') 함수는 함수명 뒤에 반드시 소괄호가 온다. # print()는 시스템 함수

# --------------------------------
# 덧셈,뺄셈,곱셈,나눗셈을 하는 계산기 함수를 작성
'''
def calc(v1, v2, op): #2.함수실행
    result = 0
    if   op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2

    return result #3.함수반환


var1 = int(input('첫번째 숫자를 입력: '))
var2 = int(input('두번째 숫자를 입력: '))
oper = input('계산연산자를 입력(+,-,*,/): ') # 4. 문자입력

res = calc(var1,var2,oper) #1.함수호출  #5.함수대입

print('#계산기 : %d %s %d = %d' %(var1, oper, var2, res))
'''
#-----------------------------------
#약수를 구하는 프로그램
'''
n = int(input('정수입력: '))  #정수를 입력하는 경우는 int-intput  숙어처럼 외울 것.
a = []
for i in range(1,n+1): # for 문과 if 문을 이용하여 n의 약수를 구하는 프로그램 
    if n % i == 0:     # n을 1~n으로 나누었을 때 나누어 떨어지면 (= 약수라면..)
        print(i)       # 약수출력
'''
#-----------------------------------
# a, b 두수를 입력받고 공약수를 구하는 프로그램
'''
a = int(input('첫번째 수 입력: '))
b = int(input('두번째 수 입력: '))

for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        print(i)
'''
#-----------------------------------
# a, b 두수를 입력받고 공약수를 구하는 프로그램 다른 방법
'''
a = int(input('첫번째 수 입력: '))
b = int(input('두번째 수 입력: '))

if a >= b:
    for i in range(1,b+1):
        if a % i == 0 and b % i == 0:
            x = i
            print(x)
else:
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            x = i
            print(x)
'''
#-----------------------------------
# a, b 두수를 입력받고 최대공약수를 구하는 프로그램 다른 방법
'''
a = int(input('첫번째 수 입력: '))
b = int(input('두번째 수 입력: '))
x = []
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i ==0:
      x.append(i)
print(max(x))
'''
# 위는 내가 푼 복잡한 방법이고 더 쉬운 방법은 아래와 같이.. print(x)를 앞으로 빼낸다.
'''
a = int(input('첫번째 수 입력: '))
b = int(input('두번째 수 입력: '))

if a >= b:
    for i in range(1,b+1):
        if a % i == 0 and b % i == 0:
            x = i

else:
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            x = i
print(x)
'''
#-----------------------------------
# n을 입력받고 약수의 갯수를 구하는 방법
'''
a = int(input('수 입력: '))
count = 0                   # 누적합을 구할 때 반드시 변수선언(변수초기화)를 해야 한다.
                            # 파이썬은 변수선언 할 필요가 없지만, 복잡한 코딩을 할때는 반드시 변수를 정의하는게 좋다. 
for i in range(1,a+1):
    if a % i == 0:
        count += 1
print(count)
'''
#-----------------------------------
# 위 약수의 갯수를 함수를 이용하여 .. n의 약수의 갯수를 출력하는 프로그램
'''
def 약수개수(x):      # 함수의 이름을 한글로 써도 된다.
    약수의개수 = 0    # 약수의 개수는 한글로 된 변수이름(한글 띄어쓰기는 안됨)

    for i in range(1,x+1):
        if x % i == 0:
            약수의개수 += 1
    return 약수의개수

# 이제 메인코드

x = int(input('입력수: '))
약수의개수 = 약수개수(x)
print(약수의개수)
'''
#-----------------------------------
# 입력수가 소수인지 아닌지를 판단하는 방법
'''
a = int(input('수 입력: '))
count = 0

for i in range(1,a+1):
    if a % i == 0:
        count += 1
        
if count == 2:
    print(f'{a}는 소수임')
else:
    print(f'{a}는 소수아님')
'''
#-----------------------------------
# 입력수가 소수인지 아닌지를 판단하는 방법을 함수를 써서..
# 아래는 내가 한 방법
'''
def prime_number(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
            
    if count == 2:
        return print(f'{n}는 소수임')
    else:
        return print(f'{n}는 소수아님')
'''
#-----------------------------------
# 강사의 방법  ->  이 부분에 대한 복습 필요 
def 소수판단(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a = int(input('숫자입력: '))

if 소수판단(a): print('소수')
else          : print('소수x')   
