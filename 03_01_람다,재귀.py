# 24-04-13 (토)
# lamdba 함수에 대해서 더 해보자면..
'''
list1 = [1,2,3,4]
list2 = [10,20,30,40]

hap_list = list(map(lambda n1,n2: n1 + n2, list1, list2))

print(hap_list)
'''
# 위내용을 줄이면..
'''
hap_list = list(map(lambda n1,n2: n1 + n2, [1,2,3,4], [10,20,30,40]))
print(hap_list)
'''

# 람다함수
# lambda 인자리스트 : 표현식

# lambda는 쓰고 버리는 일시적인 함수
# 함수가 생성된 곳에서만 필요
# 즉, 간단한 기능을 일반적인 함수와 같이 정의해두고 쓰는 것이 아니고,
# 필요한 곳에서 즉시 사용하고 버림.

#-------------------------------------------
# 재귀함수 : 자신이 자신을 호출
'''
def selfCall():
    print('Z',end='')
    selfCall()  # 내 자신을 또 호출

print(selfCall())
'''
#-------------------------------------------
# 입력한 숫자를 1까지 세는 함수를 재귀함수로 가로 출력
# 10을 넣으면 10,9,8~ 1까지 출력되게
'''
def count(num):
    if num >= 1:
        print(num, end = ' ')
        count(num-1)
    else:
        return

print(count(20))
'''
#-------------------------------------------
# factorial 값을 구하는 함수 재귀함수로..
'''
def factorial1(num):
    
    if num <= 1:
        return num
    else:
        return num * factorial1(num-1)
        # fac = num-1
        # print(num, end = ' ')
        # factorial1(num -1)
print(factorial1(1))
'''
#-------------------------------------------
# 사용자에게 0부터 100사이의 하나의 숫자를 입력받아 3,6,9가 들어 있으면
# crap을 출력하고 그렇지 않으면 next number를 출력하는 함수를 만들어보자
# 이건 내가 한거, 아래에 정답
'''
num = int(input('0~100 사이의 숫자:'))

for i in range(1,num+1):
    if str(3) in str(num):
        print('crap')
    else:
        print(num)
'''
# 정답
def game(num):
    a = num // 10
    b = num % 10

    if a == 3 or a == 6 or a == 9:
        return 'crap'
    elif b == 3 or b == 6 or b == 9:
        return 'crap'
    else:
        return num

num = int(input('0~100 사이의 숫자:'))
print(game(num))
# 내가 하려고 했던 것은 1,2,crap,4,5,crap,7,8,crap,10,11,12,crap
# 이렇게 출력하려고 했던 것임. 이렇게 한번 해볼 것.

# 함수는 여기까지....




    

