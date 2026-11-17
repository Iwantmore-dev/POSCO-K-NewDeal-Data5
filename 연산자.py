## 산술연산자
# +-*/
#// : 몫, % : 나머지, **: 거듭제곱

print(3+5) #8
print(3-5) #-2
print(3*5) #15
print(10/4) #2.5


print(11//3) #3
print(11 % 3) #2


print(10**3) #1000

# %2 를 사용하면 나머지가 0 or 1에 따라 홀짝 구분가능
#연산자 우선순위
# **, * / // %, + - 순서임. 괄호를 사용하여 연산자 우선순위 변경가능

print(2+5*3) #17

### 문자열 연산
print("*"*20) #********************
print("안녕"+"하세요"+"!!!") #안녕하세요!!!

###복합 할당 연산자
score = 70
score = score + 30 #100
score += 30 #130
print("score",score) #score 130

score = 70
score = score -30 #40
score -= 30 #10
print("score",score) # score 10