# 상속
'''
class Car:
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value

        print('현재 속도(부모클래스): %d' %self.speed)


# sedan 과 truck 두 자식을 만든다.

class Sedan(Car):  # 부모클래스(Car)로부터 상속 받은 자식 클래스(Sedan)
    speed = 0
    
    def upSpeed(self, value):  
        self.speed += value

        if self.speed > 150:  # 부모가 물려준 메서드를 자식이 다시 재정의
            self.speed = 150  # 이를 메서드 overriding 이라고 한다.
                              # 서브클래스(sedan)의 upspeed()메서드 다시 만듦
                              # (메서드오라이딩)

        print('현재 속도(자식클래스): %d' %self.speed)


class Truck(Car):   #서브클래스(Truck)에는 아무런 내용없어 수퍼클래스의 메서드를 그대로 상속
    pass            # 트럭 자식은 부모를 그대로 물려받는.. 의미

sedan1, truck1 = None, None     # 코드를 읽을때 이 부분부터 먼저 읽는다.

truck1 = Truck()
sedan1 = Sedan()

print('트럭 =>', end = '')
truck1.upSpeed(200)   # Truck 인스턴스의 upSpeed() 호출하면 부모 클래스의 upspeed 메서드 호출

print('승용차 =>', end = '')
sedan1.upSpeed(200)  # Sedan 인스턴스의 upSpeed() 호출하면 위행에서 재정의된 upSpeed() 메서드를 호출
'''
#---------------------------------------------------
'''
상속의 개념
    클래스의 상속(Inheritance) : 기존 클래스에 있는 필드와 메서드를
                                 그대로 물려받는 새로운 클래스를 만드는 것
    공통된 내용을 자동차 클래스에 두고 상속을 받음으로써 일관되고 효율적인 프로그래밍 가능
    상위 클래스인 자동차 클래스를 슈퍼 클래스 또는 부모 클래스,
    하위의 승용차와 트럭 클래스는 서브 클래스 또는 자식 클래스 라고 한다.
메서드 오버라이딩
    상위 클래스의 메서드를 서브 클래스에서 재정의
'''
#---------------------------------------------------
'''
class Line:
    length = 0
    def __init__(self, length): # instance를 생성할때 자동호출
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다.')
    def __del__(self):         # instance를 삭제할때 자동호출
        print(self.length, '길이의 선이 제거되었습니다.')
    def __repr__(self):        # instance를 프린트문으로 실행할때 생성
        return '선의 길이:' + str(self.length)
    def __add__(self, other):  # instance 사이의 덧셈이 일어날때 
        return self.length + other.length
                               # 아래 두개는 비교 메소드
    # 비교메서드 : __lt__(), __le__(), __gt__() 등
    # 인스턴스 사이의 ㅂ교 연산자(<, <=, >, >=, ==, != 등) 사용할때 호출
    # lt, gt, le, ge, eq, ne 메서드는 DataFrame의 크기 비교를 수행하는 메소드
    # 각각 >,<,>=, <=, ==, != 와 용도가 같다, 그리고 각 메서드는 사용법이 동일
    # 각각 less than, greater that, less equal, grater equal, equal, not equal 을 뜻함.
    def __lt__(self, other):   
        return selflength < other.length
    def __eq__(self, other):
        return self.length == other.length

myLine1 = Line(100)
myLine2 = Line(200)
print(myLine1)

print('두 선의 길이 합: ', myLine1 + myLine2)
'''
#---------------------------------------------------
# 추상메서드
# 서브클래스에서 메서드를 오버라이딩 : 수퍼클래스에서는 빈 껍질의 메서드만 만들어 놓고,
#                                      내용은 pass로 채움 
'''
class SuperClass:    # SuperClass  상속받은 subclass1과 subclass2를 만듦
    def method(self):
        pass        # 이와 같이 부모 클래스에서 아무것도 안만드는 것(pass)을 추상메서드라고 한다.
    
class SubClass1(SuperClass):   # 자식이 이 method를 오버라이딩하는 것.
    def method(self):
        print('SuperClass에서 method()를 오버라이딩함')

class SubClass2(SuperClass):
    pass   # 부모가 pass하면 자식이 메서드 오버라이딩을 해줘야 한다.
           # 그렇지 않으면 오류는 아니지만 심각한 문제 발생

sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()
'''
#---------------------------------------------------
# 아래와 같이 하면 동시출발이 아님. 1초간격으로 순차적으로 출발
'''
import threading
import time

class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + '~~달립니다.\n'
            print(carStr, end = '')
            time.sleep(1) # 0.1초 멈춤

# 메인코드 부분
car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')

car1.runCar()
car2.runCar()
car3.runCar()

#th1 = threading.Thread(target = car1.runCar)
#th2 = threading.Thread(target = car2.runCar)
#th3 = threading.Thread(target = car3.runCar)

#th1.start()
#th2.start()
#th3.start()
'''
#-----------------------------
# 동시출발은 아래와 같이..
import threading
import time

class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + '~~달립니다.\n'
            print(carStr, end = '')
            time.sleep(1) # 0.1초 멈춤

# 메인코드 부분
car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()
