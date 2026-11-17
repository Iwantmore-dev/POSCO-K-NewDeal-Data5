#실습1
count =1
temp = 25.5
name = "machine A"
is_ok = True
print(count)
print(temp)
print(name)
print(is_ok)

#1, 25.5, machine A, True 값이 나옴.


#실습2
count = 1 #int
print(type(count)) #<class 'int'>

temp = 25.5
print(type(temp)) #<class 'float'>

name = "machine A"
print(type(name)) #<class 'str'>

is_ok = True
print(type(is_ok)) #<class 'bool'>

#실습3
#100은 정수이므로 int
print(type(100))
# <class 'int'>
#100.0은 소수점 단위이므로 float
print(type(100.0))
# <class 'float'>
#"100"은 문자열이므로 str
print(type("100"))
#<class 'str'>

#실습4
print(1+1) #2
#print("r"+1) #자료형이 다르므로 오류 예상
print("안녕"+"하세요") #안녕하세요 출력 예상

#결과 확인 완료 자료형 다른 40번 라인은 주석처리하였음.

#실습5
#print(3>2)
print(3>2)
#True
#print(5==5) 같음을 표현하기 위해선 ==사용
print(5==5)
#True
#각각의 type의 자료형을 출력하기 위해선 print(type(3>2)), print(type(5==5))
print(type(3>2))
print(type(5==5))
#<class 'bool'>
#<class 'bool'>

#실습6
x = 100 #정수 변수 x 선언
print(type(x)) #자료형 출력. <class 'int'>, 만약 x값을 알고싶다면 print만 사용
x = 100.1 #실수값으로 재할당
print(type(x)) #자료형 출력. <class 'float'>
x = "device_no.1" #숫자대신 글자로 재할당
print(type(x)) #자료형 출력. <class 'str'>

#실습7
device_temp = 40 # 장비 온도``
check_count = 10 # 체크 숫자
device_name = "device A" #장비 이름
is_normal = False # 장비 상태. 여기서는 False로 할당함.

#동일하게 변수들의 자료형 및 결과 시도하겠음.
print(device_temp)
print(check_count)
print(device_name)
print(is_normal)

print(type(device_temp))
print(type(check_count))
print(type(device_name))
print(type(is_normal))

#40, 10, device A, False, <class 'int'>,<class 'int'>,<class 'str'>,<class 'bool'>
