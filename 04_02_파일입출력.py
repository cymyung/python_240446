# 한줄씩 읽기

inFp  = None  # 입력파일
inStr = ''    # 읽어온 문자열  

# 1단계 파일열기
inFp  = open('C:/temp/data1.txt', 'r')
# 텍스트 파일 저장시 문서 인코딩을 ansi로 한다.

#2단계 읽기
# readline() 함수는 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
inStr = inFp.readline()
print(inStr, end = '') #화면에 출력

inStr = inFp.readline()
print(inStr, end = '')

inStr = inFp.readline()  # 세줄이니까 세번 반복
print(inStr, end = '')

# 3단계 닫기
inFp.close()

'''
파일입출력의 개념
    표준 입출력과 파일 입출력 함수
파일 입출력의 기본 과정
1단계 : 파일 열기
    모드(mode) : open() 함수의 마지막 매개변수
        r : 읽기모드
        w : 쓰기모드
2단계 : 파일처리
3단계 : 파일닫기
    1단계에서 open() 함수로 연 변수명
'''
#-----------------------------------
# 모든 행을 다 읽는 방법, 위에꺼 반복문으로..
# 이건 내가 푼 방법, 왜 아무런 반응이 없지? 나중에 챗GPT에 물어볼 것
# 알았음. 초기 inStr이 0이므로 .
'''
inFp  = None  # 입력파일
inStr = ''    # 읽어온 문자열  

# 1단계 파일열기
inFp  = open('C:/Temp/data2.txt', 'r')
# 텍스트 파일 저장시 문서 인코딩을 ansi로 한다.

#2단계 읽기
# readline() 함수는 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
inStr = inFp.readline()
while len(inStr) > 0:
    print(inStr, end = '')
    inStr = inFp.readline()

# 3단계 닫기
inFp.close()
'''
#---------------------
#강사의 방법
'''
inFp  = None  
inStr = ''    

inFp  = open('C:/Temp/data2.txt', 'r')

while True:
    inStr = inFp.readline()  # 파일에서 행을 1개 읽음.
    if inStr == '':
        break;
    print(inStr, end = '')

# 3단계 닫기
inFp.close()
'''
#---------------------
# 여러줄 한번에 읽기 readlines()
'''
inFp  = None  # 입력파일
inList = ''    # 읽어온 문자열  

# 1단계 파일열기
inFp  = open('C:/Temp/data2.txt', 'r')
# 텍스트 파일 저장시 문서 인코딩을 ansi로 한다.

#2단계 읽기
# readline() 함수는 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
inList = inFp.readlines()
print(inList) #화면에 출력

# 3단계 닫기
inFp.close()
'''
#---------------------
# 여러줄 한번에 읽기 readlines(),
# 근데 위에처럼 list로 보이지 않게.. 한행씩 출력, 이건 내가 푼것.
'''
inFp  = None  # 입력파일
inList = ''    # 읽어온 문자열  

# 1단계 파일열기
inFp  = open('C:/Temp/data2.txt', 'r')
# 텍스트 파일 저장시 문서 인코딩을 ansi로 한다.

#2단계 읽기
inList = inFp.readlines()

print(inList[0],inList[1],inList[2]) #화면에 출력

# 3단계 닫기
inFp.close()
'''
#--------------------------------------
# 여러줄 한번에 읽기 readlines(),
# 근데 위에처럼 list로 보이지 않게.. 한행씩 출력, 강사
'''
inFp  = None  # 입력파일
inList, inStr = [], ''    # 읽어온 문자열  

# 1단계 파일열기
inFp  = open('C:/Temp/data2.txt', 'r')
# 텍스트 파일 저장시 문서 인코딩을 ansi로 한다.

#2단계 읽기
inList = inFp.readlines()

for inStr in inList:
    print(inStr, end = '')

# 3단계 닫기
inFp.close()
'''
#-------------------------------------
# win.ini 파일에 있는 내용을 불러오기
'''
inFp  = None  
fName, inList, inStr = '', [], ''   

fName = input('file name: ')  #c:/Windows/win.ini
inFp  = open(fName, 'r')

inList = inFp.readlines()

for inStr in inList:
    print(inStr, end = '')

inFp.close()
'''
#-------------------------------------
# win.ini 파일에 있는 내용을 불러오기, 경로가 안맞아도 에러 메시지가 안뜨게..
'''
import os

inFp  = None  
fName, inList, inStr = '', [], ''   

fName = input('file name: ')  #c:/Windows/win.ini
if os.path.exists(fName):
    inFp = open(fName, 'r')

    inList = inFp.readlines()

    for inStr in inList:
        print(inStr, end = '')

    inFp.close()

else:
    print('%s 파일이 없슴다.' %fName)
'''
#--------------------------------------
# 파일 만들기(표준입력으로 파일로 저장)
'''
outFp  = None
outStr = ''

outFp = open('c:/Temp/data3.txt','w')   # 파일열때 쓰기모드인 w 사용

while True:   # 무한반복
    outStr = input('input: ')
    if outStr != '':
        outFp.writelines(outStr + '\n')
    else:
        break
# while 문은 while true에 밑에서 if, else로 끝내는 구조를 많이 쓰는듯..

outFp.close()
print('===== 정상적으로 파일에 씀 ====')
'''
#--------------------------------------
# 파일을 불러와서 파일로 저장하는 방법
'''
inFp, outFp = None, None
inStr = ''

inFp  = open('c:/Windows/win.ini','r')
outFp = open('c:/temp/data4.txt','w')

inList = inFp.readlines()
for inStr in inList:
    outFp.write(inStr)

inFp.close()
outFp.close()
print('---- 파일이 정상적으로 복사됨 ----')
'''
#--------------------------------------
# 보안의 기본 개념 암호화
'''
print(ord('파'))
print('*******')
print(chr(54028))
# 이를 암호화 하는 방법
num = ord('퍰')
print('*******')
print(chr(num - 100))
print('*******')
# ord(), chr() 두개 함수로 암호화 할 수 있다.
'''
#--------------------------------------
# 파일을 불러와서 암호화 해서 저장?
#1. 암호화, 암호해석 선택
#2. 입력파일명, 출력파일명 입력
#3. 저장
'''
inFp, outFp = None, None
inStr, outStr = '',''
i = 0
secu = 0

secuYN = input('1. 암호화, 2. 암호해석 중 선택: ') 
inFname = input('입력 파일명을 입력하세요 : ')
outFname = input('출력 파일명을 입력하세요 : ')

if secuYN == '1':
    secu = 100
elif secuYN == '2':
    secu = -100

inFp = open(inFname, 'r', encoding = 'utf-8')
outFp = open(outFname, 'w', encoding = 'utf-8')

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ''
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)        # 문자를 숫자로 변환 
        chNum = chNum + secu
        ch2 = chr(chNum)       # 숫자를 문자로 변환
        outStr = outStr + ch2

    outFp.write(outStr)

outFp.close()
inFp.close()
print('%s --> %s 변환완료' % (inFname, outFname))
'''
