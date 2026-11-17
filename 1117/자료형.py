#int 정수형
#float 실수형
#str 문자열형
#bool 논리형


count = 3 #int
temp = 25.5 #float
name = "센서 A" #str
empty = "" #str
ok = True #bool, True는 반드시 대문자로 시작해야함.
no = False #bool, False는 반드시 대문자로 시작해야함.

print(count > temp) #False
print(count < temp) #True

#### type()함수 사용해보기 - 자료형 확인
print(type(25)) #<class 'int'>
print(type(temp)) #<class 'float'>
print(type(name)) #<class 'str'>
print(type(25>24)) #<class 'bool'>

print(type(temp<count)) #<class 'bool'>

###문자열, 숫자형의 더하기 연산자 사용

print(80+70) #150
print("80"+"70") #8070
#print("80"+70) #TypeError: can only concatenate str (not "int") to str
print(type(80+70)) #<class 'int'>
print(type("80"+"70")) #<class 'str'>


####실수형의 더하기
print(0.1+0.2) #0.30000000000000004
print(round(0.1+0.2,2)) #0.3 유효숫자 2개까지 허용


##### 숫자와 문자열의 계산
a = 100
print(a+10) #110
#print(a+"10") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10/2) #5
print(type(10/2)) # <class 'float'> 5라는 정수가 나오더라도 나누기를 하면 float가 됨.





