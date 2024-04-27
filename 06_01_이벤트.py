# 마우스 왼쪽 버튼을 클릭했을때 처리하는 방법
'''
from tkinter import *
from tkinter import messagebox
window = Tk()

def clickLeft(event):  # 마우스 이벤트가 발생할때 작동할 함수 정의
    messagebox.showinfo('mouse','mouse 왼쪽버튼이 클릭됨')

window.bind('<Button-1>', clickLeft)
# window.bind() 함수에는 마우스 왼쪽 버튼 클릭할 때 발생하는 이벤트인 <Button-1> 설정하고
# 위행의 clickLeft 함수명을 지정
# <Button-1>은 이벤트 코드라고 한다. 

window.mainloop()
'''
#-----------------------------------
# <Button>   -> 모든 버튼 공통
# <Button-1> -> 왼쪽버튼
# <Button-2> -> 가운데버튼
# <Button-3> -> 오른쪽버튼

'''
from tkinter import *
from tkinter import messagebox
window = Tk()

def clickImage(event):  # 마우스 이벤트가 발생할때 작동할 함수 정의
    messagebox.showinfo('mouse','토끼에서 마우스가 클릭됨')

window.geometry('400x400')
photo = PhotoImage(file ="img/rabbit.gif")  
label1 = Label(window, image=photo)   # image 대신 img입력해서 오류남, # image 클릭할때만 이벤트 처리
label1.bind('<Button>', clickImage)   # window bind가 아니다. 지정된 위젯이므로..
                                      # <button> 이벤트를 사용했기 때문에 어떤 마우스 버튼 눌러도 메시지창 표시

label1.pack(expand=1, anchor= CENTER) # center는 대문자 이거 틀려서 에러남
                                      # expand = 0 또는 1, (0은 상단, 1은 가운데) 
window.mainloop()
'''
#-----------------------------------
# 왼쪽, 오른쪽 어느 마우스가 클릭되었는지를 알려주는
# event 매개 변수를 활용한 마우스 이벤트 처리
# 마우스를 클릭할 때마다 어떤 마우스가 클릭되었는지 보여주고 클릭한 좌표 출력
'''
from tkinter import *

def clickMouse(event): # 마우스를 클릭했을 때 실행될 이벤트 함수 선언
    txt = ''
    if   event.num == 1: # event.num 값은 마우스 왼쪽버튼 클릭했을때 1값을 가지고,
                         # 마우스 오른쪽 버튼 클릭했을 때 2값 가짐
        txt += '마우스 왼쪽 버튼('
    elif event.num == 3:
        txt += '마우스 오른쪽 버튼('
        
    txt += str(event.y) + ","+ str(event.x) + ')에서 클릭됨'  #event.x와 event.y는 클릭한 위치의 좌표를 가짐
    label1.configure(text=txt)   # 화면에 표시한 레이블의 글자 변경

window = Tk()
window.geometry('400x400')

label1 = Label(window, text = '이곳이 바뀜')
window.bind('<Button>', clickMouse)  # 마우스 클릭하면 함수 호출

label1.pack(expand=1, anchor= CENTER)

window.mainloop()
'''
#-----------------------------------
# 키보드 이벤트 처리
# 키보드 이벤트는 위젯에서 키보드가 눌리면 발생
'''
from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo('키보드 이벤트', '눌린키: '+ chr(event.keycode))
#키보드가 눌릴때 작동하는 함수 선언
#event.keycode에는 눌려진 키의 숫자 값이 들어 있으므로 chr()함수를 사용하면 문자로 변환
    
window = Tk()

window.bind('<Key>', keyEvent)  # <key> 이벤트를 윈도창에 사용
window.mainloop()
'''
#-----------------------------------
# 메뉴와 대화상자
# [파일]메뉴 아래에 [열기]와 [종료] 하위 메뉴가 있는 코드
'''
from tkinter import *
window = Tk()

mainMenu = Menu(window)  #Menu(부모윈도)로 mainMenu 변수 생성, '메뉴 자체'를 나타내는 변수
window.config(menu = mainMenu) # 생성한 메뉴 자체를 윈도창의 메뉴로 지정

fileMenu = Menu(mainMenu)  # 상위메뉴인[파일] 생성, 메뉴 자체에 부착 [파일]메뉴는
                           # 선택하고 끝나는 것이 아니라, 아래에 다른 메뉴가 확장되어야 하므로 
                           # add_cascade() 함수 사용
mainMenu.add_cascade(label='파일', menu = fileMenu)   # cascade에서 점선을 그려주는 것으로 보임. 
fileMenu.add_command(label='열기')  # [파일]메뉴의 하위에 [열기] 메뉴 준비
fileMenu.add_separator()            # 메뉴 사이에 구분선 넣음      # 점선은 default로 나오는 것임, 다른것을 다 막아보면 알 수 있음. 
fileMenu.add_command(label='종료')  # 같은 방식으로 하위 메뉴 생성

window.mainloop()
'''
#-----------------------------------
# 위에서 [열기]를 눌렀을때, 그리고 [종료]버튼을 눌렀을때.. 이벤트 생성
# 메뉴를 선택하면 작동할 수 있도록 코드 추가
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

# messagebox 누를때 이벤트 함수 생성
def func_open():  # [열기]메뉴 선택하면 간단한 메시지창 열림
    messagebox.showinfo('메뉴선택', '열기메뉴를 선택함')

def func_exit():  # [종료]메뉴 선택하면 프로그램이 종료
    window.quit()
    window.destroy()

mainMenu = Menu(window)  
window.config(menu = mainMenu) 

fileMenu = Menu(mainMenu)  
                           
                           
mainMenu.add_cascade(label='파일', menu = fileMenu)
fileMenu.add_command(label='열기', command = func_open)
#[열기]메뉴 선택하면 무언가 작동해야 하므로 add_command()함수 사용, 선택할 때 실행될 함수명을 command 값으로 사용,
#즉 [파일] 메뉴 선택하면 하위 메뉴가 확장, [열기]메뉴 선택하면 func_open() 함수가 실행

fileMenu.add_separator()           
fileMenu.add_command(label='종료', command = func_exit)  # 같은 방식으로 하위 메뉴를 생성한다.

window.mainloop()
'''
#-----------------------------------
# 대화상자
# tkinter.simpledialog 모듈을 임포트한 후 askinteger() 및 askstring() 등을 사용
'''
from tkinter import *
from tkinter.simpledialog import *  # 대화상자를 불러오는 명령 askinteger 를 불러오기 위함.

window = Tk()
window.geometry('400x100')

label1 = Label(window, text = '입력된 값') # 레이블을 하나 준비
label1.pack()

value = askinteger('확대배수', '주사위 숫자(1~6)을 입력하세요', minvalue = 1, maxvalue = 6)
# -> askinteger('제목', '내용', '옵션')함수로 정수 입력
label1.configure(text = str(value))
# -> 입력받은 숫자를 문자열로 변경해서 레이블에 씀
window.mainloop()
'''
#-----------------------------------
# 그림파일인 gif 파일을 선택하는 코드
'''
from tkinter import *
from tkinter.filedialog import *   # tkinter, filedialog 모듈 임포트

window = Tk()
window.geometry('400x100')

label1 = Label(window, text = '선택된 파일이름')
label1.pack()

filename = askopenfilename(parent = window, filetypes = (('GIF파일', '*.gif'),('모든파일', '*.*')))
# -> askopenfilename()함수 사용
label1.configure(text = str(filename))
# -> filename을 출력
window.mainloop()
'''
#-----------------------------------
# 그림파일을 골라서 여는 프로그램
from tkinter import *
from tkinter. filedialog import *

def func_open(): # [파일열기] 실행되는 함수
    filename = askopenfilename(parent = window, filetypes = (('GIF 파일', '*.gif'), ('모든 파일', '*.*')))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo) # 레이블에 이미지 표시
    pLabel.image = photo

def func_exit(): # [프로그램 종료] 실행되는 함수
    window.quit()
    window.destroy()

window = Tk()
window.geometry('400x400')
window.title('명화 감상하기')

photo = PhotoImage() # 선택한 GIF 윈도창에 출력하려고 레이블 준비 photoimage()에
                     # 별도의 매개변수 없이 빈 그림만 준비
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window) #  준비하는 메뉴는 앞에서 실습한 내용과 동일
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

window.mainloop()





