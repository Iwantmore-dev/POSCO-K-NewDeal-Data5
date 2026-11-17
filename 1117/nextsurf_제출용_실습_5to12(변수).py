#실습5
x = 10
print(x) #10
x = x+5
print(x) #15

#실습6
a = 100
b = a
a = 999
print(a) # 999
print(b) # 100, b = a로 b에는 100이 할당되었고 a에는 999를 재할당했기때문.

#실습7
#print(temp) # NameError: name 'temp' is not defined 확인 완료 후 주석처리함.
temp = 25
score = 90
#print(Score) # NameError: name 'Score' is not defined. Did you mean: 'score'? score 대문자로 오류. 주석처리함.
print(temp) # 25
print(score) # 90

#실습8
temp = 25 #온도(섭씨)
count = 3 #센서 개수
#temp = 100 25번 라인 주석처리용
print(temp) #25 출력됨, 100은 주석처리되었기 때문

#실습9
x = 5
x = 10
x = x+1
print(x) #11나올것으로 예상. 실제로도 11

#실습10
name = "machine A"
temp = 40
print("machine A") #machine A
print(name), print(temp) # machine A 40

#실습11
a, b = 25, 3 #a가 무엇인지 b가 무엇인지 모르겠음.
temp, count = 25, 3 #온도가 25도, 개수가 3임을 알 수 있음.
#여러 단어를 사용해야하는경우
device_temp = 25
fatality_count = 3 #snake_case
print(device_temp), print(fatality_count) #25, 3

#실습12
x,y,z = 1,2,3 # x=1, y =2, z = 3
width, heigth = 4,3 # width =4, height = 3
print(width) #4
print(heigth) #3
print("삼각형의 넓이:",width*heigth) #12
