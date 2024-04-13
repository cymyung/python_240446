# 객체지향 프로그래밍
# 1. 클래스
# 클래스란 : 객체이다. 설계도이다. 붕어빵틀이다.
# 붕어빵이 아니라 붕어빵 틀이다.
# 자동차가 아니라 자동차를 만들기 위한 설계도이다.
# 건물이 아니라 건물을 만들기 위한 설계도이다.
# 현실세계 사물을 프로그램 안에서 구현하려고 고안된 개념이다.
# 속성과 특징 : 속성은 필드, 특징은 메소드
# 클래스의 결과물 : 인스턴스

# 2. 생성자

# 3. 인스턴스 변수와 클래스변수
# 4. 클래스의 상속
# 5.

# ----------------------------------------
# 클래스(객체지향 프로그램)
'''
class Car:            # Car 클래스의 정의
    color = ''        # 자동차의 색상과 속도 필드 정의
    speed = 0
    # 변수가 아닌 속성이라고 한다. field


    # method : 클래스 안에서 존재하는 함수
    # upSpeed, downSpeed 두개의 method가 있는 것으로 한다.
    def upSpeed(self, value): # 매개변수로 추가속도(value)를 받아 현재속도(self, speed) 증가 또는 감소
        self.speed += value   # self.speed는 위행의 speed 의미 즉 자신의 클래스에 있는 speed 변수
        
    def downSpeed(self, value):
        self.speed -= value

# 이제 클래스를 통해서 인스턴스를 만든다.

myCar1 = Car()  #-> 괄호가 필요하다.
myCar1.color = 'red'
myCar1.speed = 0

myCar2 = Car()
myCar2.color = 'blue'
myCar2.speed = 0

myCar3 = Car()
myCar3.color = 'yellow'
myCar3.speed = 0

myCar1.upSpeed(30)
print('자동차1의 색상은 %s, 현재속도는 %d' % (myCar1.color, myCar1.speed))
myCar2.upSpeed(50)
print('자동차2의 색상은 %s, 현재속도는 %d' % (myCar2.color, myCar2.speed))
myCar3.upSpeed(0)
print('자동차3의 색상은 %s, 현재속도는 %d' % (myCar3.color, myCar3.speed))
'''
'''
클래스의 개념
클래스의 모양과 생성
class 클래스명:
    이 부분에 관련 코드 구현

의미 : 현실세계의 사물을 컴퓨터 안에서 구현하려고 고안된 개념

자동차 클래스의 개념을 실제 코드로 구현
자동차의 속성은 지금까지 사용한 변수처럼 생성(필드)
자동차의 기능은 지금까지 사용한 함수 형식으로 구현
클래스 안에서 구현된 함수는 함수라고 하지 않고 메서드라고 함.

class 자동차명:
    # 자동차의 속성
    색상
    속도
    # 자동차의 기능
    속도올리기
    속도내리기

클래스 사용순서
    1단계. 클래스 생성
    2단계. 인스턴스 생성
    3단계. 필드나 메소드 사용
'''


# ----------------------------------------
# 2. 생성자
# 필드값을 초기화시키는 함수
# def __init__(self)
# def __init__(self, 매개변수)    -> 두가지가 있다.
# 매개변수가 self만 있는 생성자.
'''
class Car:          
    color = ''      
    speed = 0

    def __init__(self):      # 매개변수가 self만 있는 생성자. 
        self.color = 'red'   # 이 생성자가 아래 인스턴스 생성 행에서 자동으로 값 초기화
        self.speed = 0
    
    def upSpeed(self, value):
        self.speed += value  
        
    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car()           #-> 괄호가 필요하다.
myCar2 = Car()

print('자동차1의 색상은 %s, 현재속도는 %d' % (myCar1.color, myCar1.speed))
print('자동차2의 색상은 %s, 현재속도는 %d' % (myCar2.color, myCar2.speed))
'''
'''
생성자의 개념 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수
생성자의 기본 :
    생성자의 기본 형태 : __init__()라는 이름
    tip
        __init__()는 앞뒤에 언더바가 2개씩, init는 initialize의 약자로 초기화 의미
        언더바가 2개 붙은 것은 파이썬에서 예약해놓은 것, 프로그램을 작성시 이 이름을
        사용해서 새로운 함수나 변수명을 만들지 말 것

class 클래스명:
    def __init__(self):
        #  이 부분에 초기화할 코드 입력
'''
# ----------------------------------------
# 매개변수가 self와 매개변수가 있는 생성자.
'''
class Car:          
    color = ''      
    speed = 0

    def __init__(self, value1, value2):      # 매개변수가 self만 있는 생성자. 
        self.color = value1   # 이 생성자가 아래 인스턴스 생성 행에서 자동으로 값 초기화
        self.speed = value2
    
    def upSpeed(self, value):
        self.speed += value  
        
    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car('red',30)           #-> 괄호가 필요하다.
myCar2 = Car('blue',60)

print('자동차1의 색상은 %s, 현재속도는 %d' % (myCar1.color, myCar1.speed))
print('자동차2의 색상은 %s, 현재속도는 %d' % (myCar2.color, myCar2.speed))
'''
#-----------------------------------
#
'''
class Car:
    name = ''
    speed = 0

    def __init__(self, name, speed):
        self.name  = name
        self.speed = speed

    def getName(self):    # ()안에 self를 쓰냐 안쓰냐는, 저 위에 name, speed를 쓸거냐 안쓸거냐로 결정
        return self.name

    def getSpeed(self):
        return self.speed

#car1, car2 = None, None  # 안해도 된다.

car1 = Car('Audi',  0) #name이나 speed 필드를 사용하지 않고 
car2 = Car('Benz', 30) #getName(), getSpeed()메서드를 사용해서 값을 얻어냄

print(f'{car1.getName()}의 현재속도는 {car1.getSpeed()}입니다.')
print('************')
print(f'{car1.name}의 현재속도는 {car1.speed}입니다.')
print('************')
print('%s의 현재속도는 %d입니다.' %(car1.getName(), car1.getSpeed()))
   '''   
#-----------------------------------
#매개변수가 있는 생성자
# 클래스변수, 인스턴스 변수 연습
'''
class Car:
    color = ''  # 인스턴스변수(다른 인스턴스와 값을 공유안함)
    speed = 0   # 인스턴스변수(다른 인스턴스와 값을 공유안함)
    count = 0   # 클래스변수 (인스턴스와 값을 공유) count 를 선언하고 0으로 초기화

    def __init__(self):
        self.speed = 0
        Car.count += 1 # Car.count라고 썼기 때문에 이는 클래스변수임을 알 수 있다.
                       # 생성자 안에서 클래스변수에 접근하려고 '클래스명.count'를 1 증가

    def upSpeed(self, value):
        self.speed += value  
        
    def downSpeed(self, value):
        self.speed -= value
    

myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30   # 이로 인해 speed는 인스턴스 변수임을 알 수 있다.
print('자동차1의 현재속도는 %d, 생산된 자동차는 총 %d' %(myCar1.speed,myCar1.count))
# 위는 count가 클래스변수이기 때문에 myCar1.count를 Car.count 가능, 
print('자동차1의 현재속도는 %d, 생산된 자동차는 총 %d' %(myCar1.speed,Car.count)) #위아래는 같다.
# 즉 count는 클래스변수와 인스턴스 변수가 값을 공유하므로 둘중 아무거나 써도 같다.
# 위는 Car.count를 myCar1.count 가능

myCar2 = Car()
myCar2.speed = 60
print('자동차2의 현재속도는 %d, 생산된 자동차는 총 %d' %(myCar2.speed,myCar2.count))
'''
'''
인스턴스변수
예:car 클래스 2개필드
인스턴스 안에 공간이 할당된 변수, 여러 인스턴스가 각각의 값이 인스턴스간에 공유가 안됨

클래스변수
클래스 안에 공간이 할당된 변수, 여러 인스턴스가 클래스 변수 공간 함께 사용
'''
'''
오늘 나온 용어
1. 클래스 :  설계도, 필드, 메서드
2. 인스턴스 : 클래스를 가지고 필드와 메서드를 넣어서 만드는 것
3. 생성자 : 인스턴스를 만들때 필드값을 자동으로 초기화 시키는 것 __init__(self), __init__(self, 매개변수)
self를 쓰는지 안쓰는지는 인스턴스내에 쓰냐 안쓰냐
4. 클래스변수, 인스턴스변수: 클래스는 공유하고, 인스턴스는 자기 밖에 모른다.



'''

