temp = 25
#temp에 25라는 값이 들어갔음.
name = "센서 A"
#name에 "센서 A"라는 문자열이 들어갔음.
#변수_이름 = 할당할 값 의 형태임.
print(temp)
print(name)


x = 10
print("처음 할당 후의 x:", x)

x = 15
print("재할당된 후의 x:",x)

x =  x + 5
print("x에 5를 더한 후의 x:", x)

#무한루프에 걸릴것 같지만 그렇지 않음. 재할당을 한번 하는것과 같음.


##변수 이름 규칙
# 숫자로 시작 불가, 특수문자는 언더바(_)만 가능, 공백 불가, 한글도 가능하지만 권장하지 않음.
# python에서는 snake_case를 권장함. (단어와 단어 사이를 언더바로 연결하는 방식)
# 2sensor는 불가, sensor_2는 가능, sensor-2는 불가, sensor 2는 불가, 센서2는 가능하지만 권장하지 않음.
sensorCount = 3
sensor_count = 3 # camelcase는 권장하지 않음. (단어와 단어 사이를 대문자로 연결하는 방식)

print(sensor_count, sensorCount)

#if for  false 같은 변수명은 사용 불가
#대소문자도 변수명에서 구분됨
temp = 10
Temp = 100
print("temp, Temp:", temp, Temp)

score = 50
score = 70
score = 90
print("score:", score)

#다른 변수의 값 담기
a = 10
b = a
print("a:", a, "b:", b)
a = 11
print("a:", a, "b:", b)
# alt shift + 방향키를 누르면 여러줄을 동시에 편집할 수 있음. (한번에 여러줄을 선택하고 편집하는 것과 동일한 효과)

## 변수 선언 ,로 여러개 하기

width, height = 4, 3
print("가로 : ", width, "세로 : ", height, "넓이 : ", width * height)
# x, y = 1,2,3 으로 설정하면 valueError가 발생함. 변수의 개수와 값의 개수가 일치해야함.
#nameerror
value = 99

print(value)




