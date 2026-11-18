##### 입력함수 input()

#name = input("이름을 입력해주세요. : ") #터미널에 입력이 가능하다. input만 있다면 사라지겠지만 변수 name을 선언함으로서 저장이 가능하다.
#print("제 이름은", name, "입니다.") #이때 name은 str타입이다.
#age = input("나이를 입력해주세요.")
#print("제 나이는" + age +"입니다.") #age도 결국 str이므로 +연결이 될것이다.

#alt를 누르고 라인을 방향키로 이동시킬 수 있다.

# number_A = input("덧셈 연산을 할 첫번째 숫자를 입력해주세요 : ")
# number_B = input("덧셈 연산을 할 두번째 숫자를 입력해주세요 : ")
#print(type(number_A), type(number_B))
#print(number_A + number_B) #이때 a와 b는 str형이다. 따라서 숫자1숫자2의 이어짐 형태로 표현될 것이다.
#print(int(number_A)+int(number_B))
#print(int(number_A+number_B)) # int를 number 전체에 걸어버리면 a가10,b가 5일때 105가 되고 이게 str에서 int로 변환된다.

# int(), float(), str() 사용해보기
print("==== float() 확인 ====")
print("int->float", float(25)) #25.0
print("정수형 str->float", float("25")) #25.0
print("실수형 str->float", float("25.5")) #25.5

#정상적인 출력이 나옴

print("==== int() 확인 ====")
print("float->int", int(25.8)) #25. 소수점은 버리고 정수형이 됨.
print("정수형 str->int", int("25")) #25
#print("실수형 str->int", int("25.8")) # valueError발생. 25.8이라는 str에서 int변환 불가능

print("===str()확인 ====")
print("int -> str",str(25)) #25
print("float -> str", str(25.2)) #25.2

# 형변환과 입력을 같이 써보기

#number_A = input("첫 번째 숫자를 입력해주세요")
#number_B = input("두 번째 숫자를 입력해주세요")
#number_A = int(number_A)
#number_B = int(number_B)

#print("덧셈 결과: ", number_A + number_B)

#n1 = int(input("숫자를 입력해주시오(1)"))
#n2 = int(input("숫자를 입력해주시오(2)"))

#print("n1, n2 자료형 확인", type(n1))
#print("뺄셈 결과:", n1-n2)

height = float(input("당신의 키를 입력해주세요 : ")) #float 188.5 사용시 value eror가 뜸
age = int(input("당신의 나이를 입력해주세요 : "))
print("당신의 키는",height,", 나이는", age, "입니다.")

