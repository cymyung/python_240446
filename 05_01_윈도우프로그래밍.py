# 윈도우 프로그래밍에 가장 기본이 되는 창을 띄우는 문장 3줄
'''
from tkinter import * # tkiner는 파이썬에서 GUI 관련 모듈 제공해 주는 표준 윈도 라이브러리

window = Tk() # Tk()는 기본이 되는 윈도를 반환, 이를 루트윈도 또는 베이스 윈도라고 함.
              # 실행하면 윈도창 화면에 출력

window.mainloop()  # 위 행에서 베이스 윈도를 windows 변수에 넣고
                   # 이행에서 window.mainloop() 함수 실행

# 기본 윈도우 창의 구성
# 위젯(Widget) : 윈도창에 나올 수 있는 문자, 버튼, 체크박스, 라디오버튼 등을 의미
# tkinter는 TK Interface의 약어. Tk는 Tcl/Tk라는 전통적인 GUI 인터페이스
# 윈도, 리눅스, 맥 등에서 모두 동일한 코드로 사용 가능
'''
# -------------------------------
#윈도창 조절
'''
from tkinter import *

window = Tk()

window.title('윈도창 연습')  # 윈도창에 제목 표시
window.geometry('400x100')   # 윈도창의 초기 크기를 400*100으로 지정
window.resizable(width = FALSE, height = TRUE)   #가로세로의 크기가 변경되지 않도록 지정

window.mainloop()     # 이게 title 보다 뒤로 가야 함.  앞으로 가면 title 등이 반영이 안됨.
'''
# -------------------------------
# 레이블(label) : 문자를 표현할 수 있는 위젯
'''
from tkinter import *

window = Tk()
window.title('윈도우 연습')
window.geometry('400x300')  # 띄워쓰기 하면 안됨.
window.resizable(width = None, height = None)

label1 = Label(window, text = 'Korea만세')  #Label() 함수가 레이블을 만들어 줌
label2 = Label(window, text = 'Python', font = ('궁서체',30), fg = 'blue')  # font : 글꼴과 크기 지정, fg는 글자색
label3 = Label(window, text = '재밌습니다.',  bg = 'magenta', width = 20, height = 10, anchor = SE)
#bg는 배경색, 위젯의 폭과 높이를 지정, anchor 위젯이 어느 위치에 자리잡을지 결정

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
'''
# -------------------------------
# 이미지 넣기
'''
from tkinter import *

window = Tk()
window.title('윈도우연습')
#window.geometry('600x300')

# label 대신 이미지 넣기
photo = PhotoImage(file='img/dog.gif')   # PhotoImage 함수는 gif 파일만 지원한다.(jpg. bmp 등은 지원하지 않음)
label1 = Label(window, image = photo)
label1.pack()

window.mainloop()

'''
# -------------------------------
# 버튼
# 버튼(button) : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행
# 예 : 버튼을 누르면 파이썬 IDLE 이 종료되는 코드 
'''
from tkinter import *

window = Tk()

button1 = Button(window, text='파이썬 종료', fg='red', command=quit)

button1.pack()

window.mainloop()
'''
# -------------------------------
# 이미지버튼을 눌렀을때 메시지 창이 나오게 하는 코드
# 강사는 이미지를 눌렀을때 멍멍멍 메시지박스가 나왔는데, 나는 반대...
# 이건 밑에 command=myfunction 뒤에 괄호가 있고 없고 차이인듯.
'''
from tkinter import *
from tkinter import messagebox   # messagebox 모듈사용 임포트

def myfunction():
    messagebox.showinfo('강아지버튼', '멍멍멍') # 이 함수는 messagebox.showinfo(제목, 내용) 형식으로 화면에 메시지 상자 출력

window = Tk()
photo = PhotoImage(file = 'img/dog2.gif')   # 이미지 준비하고 버튼에 글자 대신 이미지 표현
button1 = Button(window, image=photo, command=myfunction)

button1.pack()

window.mainloop()
'''
# -------------------------------
# 체크버튼
# 체크버튼(checkbutton) : 켜고 끄는 데 사용하는 위젯
# 예 : 체크버튼을 켜거나 끄면 메시지창이 열리게 하는 코드
'''
from tkinter import *
from tkinter import messagebox  

def myfunc():
    if chk.get() == 0:
        messagebox.showinfo('', '체크버튼이 꺼졌어요')
    else:
        messagebox.showinfo('', '체크버튼이 켜졌어요')

window = Tk()

chk = IntVar()
cb1 = Checkbutton(window, text='클릭하세요', variable=chk, command=myfunc)

cb1.pack()

window.mainloop()
'''
# -------------------------------
# 라디오버튼
'''
from tkinter import *
window = Tk()

def myfunc():    # myfunc()함수는 var 변수값으로 맨 아래쪽 레이블의 텍스트를 변경
    if   var.get() == 1:
        label1.configure(text = 'Python')
    elif var.get() == 2:
        label1.configure(text = 'C++')
    else :
        label1.configure(text = 'Java')

var = IntVar()   # 정수형의 변수 var 준비

rb1 = Radiobutton(window, text = '파이썬', variable = var, value = 1, command = myfunc)  # 라디오버튼을 3개 준비
rb2 = Radiobutton(window, text = '씨뿔뿔', variable = var, value = 2, command = myfunc)
rb3 = Radiobutton(window, text = '자바'  , variable = var, value = 3, command = myfunc)

label1 = Label(window, text = '선택한 언어: ', fg = 'red')

rb1.pack()
rb2.pack()
rb3.pack()

label1.pack()

window.mainloop()
'''
# -------------------------------
# 수평으로 정렬
'''
from tkinter import *
window = Tk()

button1 = Button(window, text = '버튼1')
button2 = Button(window, text = '버튼2')
button3 = Button(window, text = '버튼3')

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()
'''
# -------------------------------
# 바로 위 문장을 list와 for 문으로..
# 아래내용은 내가 한것.. 다음이 정답
'''
from tkinter import *
window = Tk()

btnList = [] * 3

for i in range(1,4):
    button = Button(window, text = f'버튼{i}')
    btnList.append(button)

print(btnList)
'''
# -------------------------------
# 정답
'''
from tkinter import *
window = Tk()

btnList = [None] * 3  # 비어 있는 리스트를 3개 준비

for i in range(0,3):    # 3회 반복하면서 버튼 생성
    btnList[i] = Button(window, text = '버튼'+str(i+1))

for btn in btnList:    # 준비한 버튼 리스트를 화면에 출력
    btn.pack(side = RIGHT)

window.mainloop()
'''
# -------------------------------
#  버튼을 세로로 쌓기, 외곽 창 사이와 여백
'''
from tkinter import *
window = Tk()

btnList = [None] * 3  # 비어 있는 리스트를 3개 준비

for i in range(0,3):    # 3회 반복하면서 버튼 생성
    btnList[i] = Button(window, text = '버튼' + str(i+1))

for btn in btnList:    # 준비한 버튼 리스트를 화면에 출력
    btn.pack(side = BOTTOM, fill=X, padx=10, pady=10)   # pad는 버튼과 외곽 창 사이의 여백

window.mainloop()
'''
# -------------------------------
#  버튼을 세로로 쌓기, 외곽 창 사이와 여백
'''
from tkinter import *
window = Tk()

btnList = [None] * 3  # 비어 있는 리스트를 3개 준비

for i in range(0,3):    # 3회 반복하면서 버튼 생성
    btnList[i] = Button(window, text = '버튼' + str(i+1))

for btn in btnList:    # 준비한 버튼 리스트를 화면에 출력
    btn.pack(side = BOTTOM, fill=X, ipadx=50, ipady=20)   # ipad는 위젯 내부의 여백

window.mainloop()
'''
# -------------------------------
#  버튼을 세로로 쌓기, 외곽 창 사이와 여백
# 내외부 여백 동시에 주기
'''
from tkinter import *
window = Tk()

btnList = [None] * 3  # 비어 있는 리스트를 3개 준비

for i in range(0,3):    # 3회 반복하면서 버튼 생성
    btnList[i] = Button(window, text = '버튼' + str(i+1))

for btn in btnList:    # 준비한 버튼 리스트를 화면에 출력
    btn.pack(side = BOTTOM, fill=X, ipadx=50, ipady=20, padx=10, pady = 20)   # ipad는 위젯 내부의 여백

window.mainloop()
'''
# -------------------------------
# 고정위치에 배치
# 위젯을 고정 위치에 배치하려면 pack() 대신 place() 함수 사용
# 그림 9개를 2차원으로 배치하는 코드
'''
from tkinter import *
from random import * # 아래 그림을 섞기 위해서.. shuffle을 사용할때 필요

btnList = ['']*9  # 버튼을 저장할 9개짜리 리스트를 준비
fnameList = ['honeycomb.gif','icecream.gif','jellybean.gif','kitkat.gif','lollipop.gif','marshmallow.gif','nougat.gif','oreo.gif.','pie.gif']
# 이미지 파일명 9개를 리스트로 준비
photoList = [None]*9  # PhotoImage()로 생성할 9개짜리 리스트
i,k = 0,0
xPos, yPos = 0,0  # xPos, yPos는 그림을 출력할 x, y 좌표로 사용
num = 0           # num은 그림의 순차 번호로 사용

window = Tk()
window.geometry('210x210') # 70짜리 3장이니까 210

shuffle(fnameList)  # 9개의 이미지를 임의로 섞어줌

for i in range(0,9):      # 9번 반복하면서 버튼을 생성
    photoList[i] = PhotoImage(file = 'img/' + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3):        # 3x3=9번 반복행에 대해서 열을 반복, 그림 9개를 2차원으로 배치하는 코드
    for k in range(0,3):
        btnList[num].place(x = xPos, y = yPos)   # 정해진 위치에 딱 고정하는 것은 pack 대신 place를 쓴다.
        num += 1
        xPos += 70   # x좌표값을 70씩 증가하면서 배치
    xPos = 0
    yPos += 70       # y좌표값을 70씩 증가하면서 배치

window.mainloop()
'''
# -------------------------------
# 사진 보기
'''
from tkinter import *
from time import *

fnameList = ['jeju1.gif','jeju2.gif','jeju3.gif','jeju4.gif','jeju5.gif','jeju6.gif','jeju7.gif','jeju8.gif','jeju9.gif']

photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = 'img/' + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file = 'img/' + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
window = Tk()
window.geometry('700x500')
window.title('사진 앨범 보기')

btnPrev = Button(window, text = '<< 이전', command = clickPrev)
btnNext = Button(window, text = '다음 >>', command = clickNext)

photo = PhotoImage(file = 'img/' + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()
'''
