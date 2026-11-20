line = '==========================='
#리스트
#변수하나에 하나값을 저장하면 100개의 값은 100개의 변수가 필요함 >> 불편

# 변수와 달리 여러 값을 한 목록에 보관

#순서가 중요함. 담은 순서가 그대로 유지돼 나중에 찾기 쉬움.
#리스트는 대괄호로 작성함.


#리스트에 담기는 값은 종류를 가리지 않는다.
# len함수를 이용하면 리스트에 담긴 값이 몇개인지 알려줌.

# 인덱스 번호로 값을 가져올 수 있음.
temps = [25, 26, 24, 28, 27]
print(temps[1]) #26
print(type(temps[1])) #int, 저장된 데이터에 따라 타입다름.
print(type(temps)) #list

# 인덱스 범위를 벗어나면 IndexError가 나오므로 주의해야함
# 슬라이싱으로 리스트의 범위를 일부만 가져오기 가능함
print(temps[1:4]) # [26, 24, 28], 슬라이싱으로 인덱스를 가져오면 무조건 list로 가져옴, [::2]처럼 스텝도 적용되고 기본적인 슬라이싱의 문법이 그대로 적용됨

temps[2] = 99 #인덱스의 2번 값을 99로 변경
print(temps) #[25, 26, 99, 28, 27]

#값이 있는지를 in으로 확인 가능
print(99 in temps) #위에서 99넣었으므로 True

#append는 리스트 전용 함수. 리스트 맨끝에 값 하나를 추가해준다.
temps.append(100)
print(temps) # [25, 26, 99, 28, 27, 100]

#remove는 값을 제거함.
#pop은 위치로 꺼내며 제거함.
#del은 인덱스로 삭제하되 값을 돌려주지 않는다.
temps.remove(100)
del temps[2] #슬라이싱으로 구간 삭제도 가능.
# sort()는 정렬
# reverse()는 순서 뒤집기. 슬라이싱으로도 바꿀 수 있지만 원본은 변경x였으나 reverse는 원본을 뒤집어버림
# count, index는 세고 찾는 용도, count는 몇번 나오는지 index는 처음 나오는 위치 >> 기존에 사용하던 것 그대로 사용가능.


print(line)

#리스트 연습
numbers = [25,80, 30, 50, 11, 12]
machines = ['펌프', '모터', '압축기']

mixed = [True, False, "문자열", 100, [1,2,3]] #리스트 안에는 데이터 형식이 어떻던지 다 가능함.

print(numbers)
print(machines)
print(mixed)

#####len(리스트) : 리스트의 요소의 개수 확인

print(f'numbers의 요소 개수 확인 : {len(numbers)}') #6
print(f'machines의 요소 개수 확인 : {len(machines)}') #3
print(f'mixed의 요소 개수 확인 : {len(mixed)}') #5

print(f'비어있는 리스트의 개수 확인 : {len([])}') #0

print(line)

#리스트의 인덱싱과 슬라이싱

numbers = [25, 80, 30, 50, 11, 12]
print(numbers[3]) #50이라는 숫자를 가지고 오고 싶을때 50
print(mixed[1:4]) #슬라이싱으로 범위를 가져오고 싶을때 [False, '문자열', 100]
print(mixed[-2]) #음수 인덱싱 확인용 100
print(mixed[-1][0]) #리스트 안의 리스트에서 1을 뽑고 싶을때 1 >>>이중 리스트로 접근 가능

#30~11까지 슬라이싱으로 뽑아보기
print(numbers[2:5])
print(numbers[::-1])

print(line)
### 리스트의 데이터 변경하기 (인덱싱을 통해 값 변경)
numbers = [25, 27, 30, 32, 34, 36]
numbers[2] = 100

print(numbers) # [25, 27, 100, 32, 34, 36]
print(line)

#### in, not in
machines = ['펌프', '모터', '압축기']
print("펌프"in machines) # True
print("펌프 "in machines) # False
print('실린더' not in machines) # True
print(line)
#실습2 인덱스로 값 꺼내기
temps = [22, 10, 27, 36, 40, 55]
print(temps[0]) #22
print(temps[2]) #27
print(temps[-1]) #55
print(line)
#라인 생산량 6개 리스트로 저장, 첫 값과 마지막 값을 각각 인덱스로 꺼내 변수에 담기
#두 값을 더한 합을 출력, 두 값을 더해 2로 나눈 중간값을 출력

line_h = [12,25,67,23,58,76]
first = line_h[0]
last = line_h[-1]
print(first + last) #88
print((first + last)/2) #44.0
print(line)

#### 리스트의 함수 사용해보기
#list.index()
print(numbers.index(34)) #4

####리스트.append(값)
###리스트의 맨 뒤에 원하는 값을 추가하는 함수이다.
data = [25, 26, 27] 
data.append(28) 
print(data) #[25, 26, 27, 28]

# data = [25, 26, 27]
# data.append(28)
# print(data.append(28)) 이렇게 하면 append가 기존 리스트에 28 추가하긴 하지만 추가한 값이나 변경된 리스트를 반환하지 않는다.
#즉 print는 반환값을 출력하므로 반환값 없음 >> none 출력함.

####리스트.insert(위치 인덱스, 값)
###리스트의 특정 위치인덱스에 원하는 값을 추가
data.insert(1,24)
print(data) #[25, 24, 26, 27, 28]

####리스트1.extend(리스트2)
###리스트1에 리스트2를 붙여주는 함수
data.extend([99,100])
print(data) #[25, 24, 26, 27, 28, 99, 100]

#실습7측정값 추가하기
list_empty = []
list_empty.append(30)
list_empty.insert(0,28)
list_empty.extend([31, 32])
print(list_empty) #[28, 30, 31, 32]
list_empty.insert(-1,50) #인서트의 경우 범위에 없는 인덱스를 넣어도 에러 안나고 뒤에 붙기만 함.
print(list_empty) #[28, 30, 31, 50, 32] #insert(-1, 50)은 마지막에 추가하는 것이 아니라, 마지막 요소 바로 앞에 삽입한다.


#리스트 간 + 기호 연결시 리스트 2개가 하나로 합쳐짐. list 자체는 문자열로 취급
print(line)

data = [ 25, 26, 27, 28, 29, 30]
#### 리스트.remove(값)
data.remove(25)
print(data) #[26, 27, 28, 29, 30]

### 리스트.pop(인덱스번호)
# pop의 경우 반환값이 존재하므로 제거되는 값을 따로 저장가능
print(data.pop(0)) #26, 위에서 25제거되었고 data원본 리스트도 변화하였음. 따라서 0번인 26을 리스트에서 제외하고 이것을 print에 반환한것.


### del 리스트[인덱싱 or 슬라이싱]
del data[0]
print(data) #26은 pop으로 지워졌음. 따라서 del로 27을 지우면 [28, 29, 30]
del data[1:3]
print(data) # 슬라이싱을  통해 0,1,2 중 1부터 2까지 지우면 0만 남게됨 즉, 28
print(line)

#실습8 잘못된 값 제거하기
#목표 : remove, pop, del을 기준(값, 위치)에 맞게 사용해 값을 제거하기
# 1. 이상값 999가 있는 리스트 저장
# 2.remove로 이상값을 값 기준으로 제거
# 3. pop으로 특정 위치 값을 꺼내며 제거해 꺼낸 값 출력
# 4. del로 첫번째 값을 삭제하고 전체 출력


# 1. 이상값 999가 있는 리스트 저장
temps = [25,26,999,24,28,26]
# 2.remove로 이상값을 값 기준으로 제거
temps.remove(999)
print(temps) #[25, 26, 24, 28, 26]
# 3. pop으로 특정 위치 값을 꺼내며 제거해 꺼낸 값 출력
print(temps.pop(1)) #26 >>>pop은 특정 위치 꺼낸 다음 그 숫자를 반환하기때문에 print로 바로 작성 가능
# 4. del로 첫번째 값을 삭제하고 전체 출력
del temps[0]
print(temps) #[24, 28, 26]

####리스트 탐색, 정렬
#리스트.sort() 기본적으로 오름차순 정렬, 괄호안에 reverse = True 옵션 작성시 내림차순 정렬

####리스트.reverse() = 리스트의 순서를 거꾸로 뒤집어 줌. (원본 리스트 변경함)
#### 리스트.count(값), 리스트.index(값)
data = [27, 24, 30, 22, 26]
data.sort()
print(data) #내림차순 정렬되고 있음. [22, 24, 26, 27, 30]
data.sort(reverse=True)
print(data) #오름차순 정렬 [30, 27, 26, 24, 22]

data =[27, 24, 30, 22, 26]
data.reverse() #[26, 22, 30, 24, 27] 순서가 뒤집어서 나오게 됨.
print(data)

raw_data = ['정상', '이상', '이상', '정상', '이상',]
#정상 개수 세기
print(raw_data.count('정상')) #2

#이상이 처음 등장하는 인덱스 출력
print(raw_data.index('이상')) #1 즉, raw_data[1]부터 이상 등장


#실습9
temps = [24,22, 24, 26, 28, 27, 30]
temps.sort()
print(temps) #[22, 24, 24, 26, 27, 28, 30]
temps.reverse()
print(temps) #[30, 28, 27, 26, 24, 24, 22]

#24의 개수
print(temps.count(24)) #2
#index로 찾은 24의 첫 위치
print(temps.index(24)) #4

####if문의 기본 구조
temp = 85
if temp >80:    
    print("온도 주의")#참일경우
    print("점검 필요")
print("측정 종료")

#조건은 TF판단이 되는걸로 보통 함. : 반드시 기입해야함. :이후 tab으로 전환 필요
#else로는 나머지경우를 처리한다.
# if조건이 거짓인 경우에는 else를 사용

score = 75
if score >= 60:
    print("합격")
else:
    print("불합격")

# elif로 여러 갈래를 판단한다. 갈림길이 셋 이상일때 중간 조건을 추가하는것. 앞 조건이 거짓인 경우에만 다음 elif를 조사
score = 82
if score >= 90: print('우수')
elif score>= 70: print('보통')
else: print('미흡')

#####조건문
'''
if 조건:
    조건이 참일때 실행될 문장
    조건이 참일때 실행될 문장2
    조건이 참일때 실행될 문장3
------
if 조건:
    조건이 참일때 실행 될 문장
else:
    조건이 거짓일때 실행 될 문장 #else는 조건이 없어도 됨.
    
-----
if 조건1:
    조건1이 참일때 실행될 문장
elif 조건2:
    조건2가 참일때 실행될 문장+조건1이 거짓이어야함.
elif 조건3:
    조건1,2가 거짓이고 조건3이 참일경우
    
else:
    조건n: 나머지 조건 모두 거짓일 때 실행될 문장
들여쓰기가 안된다면 조건의 참 거짓과 상관없이 실행이 무조건 적으로 됨.
'''

# score = int(input("점수를 입력해주세요(자연수로):"))
# if score >= 60:
#     print('합격입니다.')
# else:
#     print('불합격입니다.')
# print('조건문과 관련없이 실행되는 문장입니다.')

# print(line)

# #if 실습
# age = int(input('나이를 입력해주세요:'))
# if age >= 20:
#     print('성인입니다.')
# else:
#     print('미성년자입니다.')
# print('주류 및 담배는 성인에게만 판매가 되고있습니다.')

# score = int(input("점수를 입력해주세요:"))
# if score >= 90:
#     print('우수')
# elif score >= 70:
#     print('보통')
# else:
#     print('미흡')
# print(line)
'''
90점 이상일때 A
80점 이상일때 B
70점 이상일때 C
60점 이상일때 D
그 아래일때 F
'''
# score = int(input("점수를 입력해주세요:")) #int로 점수를 정수화 해야함.
# print(line)
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("c")
# elif score >= 60:
#     print('D')
# else:
#     print("F")
# print('당신의 점수에 따른 등급은 위와 같습니다.')
# print(line)
# print(line)
# temp = float(input('온도를 입력하세요: '))
# vib = float(input('진동을 입력하세요: '))
# #온도가 60초과, 진동이 3초과라면 : 위험합니다.
# #온도가 60초과, 진동이 3이하라면 : 주의하세요
# #온도가 60이하 : 정상입니다.
# #if문 중첩을 사용해서 해보자.

# if temp > 60:
#     if vib > 3:
#         print('위험합니다.')
#     else:
#         print('주의하세요')
# else:
#     print('정상입니다.')

####삼항 연산자
# #짝수인지 홀수인지 판단
# #if else 문을 통해서
# print(line)
# num = int(input('숫자를 입력해 주세요'))
# if (num%2) == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')


# result1=""
# number = 100
# if number%2 ==0:
#     result1 = '짝수'
# else:
#     result1 ='홀수'
# print(result1)
# '''
# 삼항 연산자는
# 참일때 값 if 조건 else 거짓일때 값 으로 작성한다.
# '''
# result2 = "짝수" if number % 2 ==0 else '홀수'
# print(result2)

# ### match - case 문
# color = input("red, yellow, green 중 하나를 작성해주세요.: ").strip() #strip으로 입력의 공백을 제거해줌.
# #red는 퇴장, yellow는 경고, green은 통과

# # # 위 세개에 해당하지 않으면 잘못된 값이 들어왔다고 말해줄것.

'''
match 값에 대한 변수:
    case 변수값1:
        변수==변수값1일때 실행할 문장
    case 변수값2:
        변수==변수값2일때 실행할 문장
    case 변수값3:
        변수==변수값3일때 실행할 문장
    case _:
        변수가 변수값 1,2,3 모두 아닐때 실행, if else문에서 else와 비슷함.

'''

# match color :
#     case 'red' | 'RED':
#         print('퇴장입니다.')
#     case 'yellow':
#         print('경고입니다.')
#     case 'green':
#         print('통과입니다.')
#     case _:
#         print('빨강,노랑,초록 중 하나를 골라주세요. 잘못된 값이 입력되었습니다.')

# #|를 사용해서 or의 역할을 할 수 있다.
# #color = input() 일때 .upper나 .lower로 대소문자 통일하는게 인식에는 편할듯 하다.

# data = ['PUMP-01', 85, "WARNING"]
# #[설비명, 온도, 상태]로 가정하자.

# # 설비명: 온도 ()도, 주의 상태입니다. 로 표기하고싶음.

# match data:
#     case [name, temp, 'WARNING']:
#         print(f'{name}: 온도 {temp}, 주의상태입니다.')
#     case [name, temp, 'NORMAL']:
#         print(f'{name}: 온도 {temp}, 정상상태입니다.')

# #따로 name, temp를 선언하지 않아도 리스트의 값을 자동으로 판단

# #실습3
# #올바른 아이디,비밀번호를 변수로 저장
# 사용자 입력을 각각 받아 저장할것

input_id = input('아이디를 입력해주세요: ').strip()
input_pw = input('패스워드를 입력해주세요: ').strip()

correct_id = "admin"
correct_pw = '1234'

if correct_id == input_id and correct_pw == input_pw:
    print('로그인 성공')
else:
    print('로그인 실패')
