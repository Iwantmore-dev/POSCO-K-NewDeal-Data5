# # 실습.4

# # 온도, 진동, 전류를 받아 저장
# # 온도 > 80 또는 진동 > 4.0이면 즉시 '위험: 즉시 정지' 출력
# # 위험이 아닐 때, 전류 > 60 and 온도 > 70이면 '주의: 부하 점검'
# # 진동 > 2.5면 '주의: 진동 관찰', 아니면 '정상'
# # 78/3.2/52를 넣어 확인

# temp = 78
# vib = 3.2
# current = 52

# if temp > 80 or vib > 4.0:
#     print('위험: 즉시 정지')
# elif current > 60 and temp > 70:
#     print('주의: 부하 점검')
# elif vib > 2.5:
#     print('주의: 진동 관찰')
# else:
#     print('정상')
# #결과값 >> 주의: 진동 관찰


# #심화실습.1 #count()를
# # 정수 5개를 공백으로 구분하여 입력을 받고, 중복을 제외한 두 번째로 큰 숫자 출력
# # 단, max()와 반복문은 사용 불가, 서로 다른 숫자가 최소 2개 존재.

# numbers = input('정수 5개 입력: ').split() #공백이 아니게 입력하면
# #print(numbers)

# #문자열을 정수로 변환
# numbers = [int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3]), int(numbers[4])]
# #print(numbers)

# numbers.sort(reverse=True) # 큰 숫자부터 오게 하였음. 내림차순
# #print(numbers)

# test1 = numbers.count(numbers[0]) #두 번째 큰 숫자의 인덱스 번호
# print('두 번째 큰 숫자: ', numbers[test1])

# # ####심화실습2 계산기 만들기

# # # 사칙연산 계산기 만들기, match case 이용할것.

# # #사용자가 선택한 연산에 따라 계산하거나 오류를 안내하는 프로그램을 만들어야함.
# # #숫자 2개와 연산자(+-*/)를 입력받아 계산 결과를 출력할것.
# # #0으로 나누거나 지원하지 않는 연산자를 입력하면 오류 메시지 출력할 것.

# num_1 = float(input('숫자를 입력하세요: ').strip())
# calc = input('연산자(+,-,*,/)를 입력하세요: ').strip()
# num_2 = float(input('숫자를 입력하세요: ').strip())

# match calc:
#     case '+':
#         print(num_1 + num_2)
#     case '-':
#         print(num_1 - num_2)
#     case '*':
#         print(num_1 * num_2)
#     case '/':
#         if num_2 == 0:
#             print('ERROR: 0으로 나눌 수 없습니다.')
#         else:
#             print(num_1 / num_2)
#     case _:
#         print('지원하지 않는 연산자입니다.')


# # ### 심화 실습3. ATM 출금 가능 여부 판정
# #1.목표: 여러 출금 조건을 검사하여 성공 또는 실패 사유를 출력
# #2.현재 잔액과 출금 금액을 입력받아 출금 가능 여부를 판정
# #3.출금액은 1,000원 단위이면서 1,000~100,000원이어야하고, 잔액을 넘을 수 없음.
# #4.성공하면 남은 잔액을, 실패하면 그 이유를 출력해야함.

# current_money = int(input('현재 잔액을 알려주세요: ')) #2-1. 현재 잔액 input 처리
# withdrawl = int(input('출금할 금액을 알려주세요: ')) #2-2. 출금 금액 input 처리
# if withdrawl < 1000:
#     print('출금은 최소 1,000원 부터 가능합니다!') # 3-1 출금액은 최소값은 1000원 부터, 4.실패한 경우 이유 출력
# elif withdrawl > 100000:
#     print('1회 출금 한도는 100,000원입니다!') # 3-2 출금액 한도는 100000원, 4.실패한 경우 이유 출력
# elif withdrawl % 1000 != 0:
#     print('출금은 1,000원 단위로만 가능합니다!')# 3-3출금액 단위는 1000원, 4.실패한 경우 이유 출력
# elif withdrawl > current_money:
#     print(f'잔액이 부족합니다. 현재 잔액은 {current_money}원입니다.') # 3-4 잔액 넘기기 불가, 4.실패한 경우 이유 출력
# else:
#     current_money = current_money - withdrawl
#     print(f'출금에 성공했습니다. 남은 잔액은 {current_money}원입니다.') #4. 성공한 경우


####실습.4 숫자 5개의 중앙값 찾기
# 문제: 숫자 5개를 입력 받아 리스트를 만들고 크기순으로 정렬했을 때 가운데 숫자 출력
# 단, 원래 입력한 리스트의 순서는 변경하지 말것.
num_list = input('숫자 5개를 입력해주세요: ').split()
#input으로 숫자를 받으면 str형이 되므로 정수형으로 변환필요.
sort_list = [int(num_list[0]), int(num_list[1]), int(num_list[2]), int(num_list[3]), int(num_list[4])]
#print(num_list)
sort_list.sort()
print(f'입력된 숫자를 정렬하면 {sort_list}입니다.')
print(f'중앙값은 {sort_list[2]}입니다.')
print(f'원본 데이터는 {num_list}입니다.')

#홀수 개를 가져오는 경우
mid_idx = len(sort_list) //2
#5면 inx는 2, 7이면 idx는3, 9이면 idx는 4
#즉 홀수일 경우에는 2로 나누었을때 몫의 값 = 중앙값 인덱스의 위치 값


########아래 내용은 리더분의 해설#########
# # ==================================================
# # 아이디 비밀번호 확인
# # ==================================================
# # 정답 아이디, 비밀번호 저장
# # 입력 아이디, 비밀번호 저장
# correct_id = "admin"
# correct_pw = "1234"
# input_id = input("로그인 아이디를 입력해주세요.")
# input_pw = input("로그인 비밀번호를 입력해주세요.")

# if correct_id == input_id and correct_pw == input_pw:
#     print("로그인 성공")
# else:
#     print("로그인 실패")


# # ==================================================
# # 실습 1. 세 값으로 설비 종합 상태 판정하기
# # ① 온도·진동·전류를 입력받아 저장
# # ② 온도>80 또는 진동>4.0이면 즉시 '위험: 즉시 정지’  출력
# # ③ 위험이 아닐 때, 전류 > 60 and 온도 > 70 이면 ＇주의: 부하 점검’,
# # 진동>2.5면 ＇주의: 진동 관찰’,  아니면 '정상’
# # ==================================================
# temp = float(input("온도 입력"))
# vib = float(input("진동 입력"))
# cur = float(input("전류 입력"))
# if temp>80 or vib>4.0:
#     print("위험: 즉시 정지")
# else:
#     if cur > 60 and temp > 70:
#         print("주의: 부하 점검")
#     elif vib>2.5:
#         print("주의: 진동 관찰")
#     else:
#         print("정상")

# # ==================================================
# # 심화 실습 1. 두 번째로 큰 숫자 찾기
# # 숫자 5개 입력: 30 50 20 50 40
# # 두 번째로 큰 숫자: 40
# # ==================================================

# data = input("숫자 다섯개 입력해주세요.").split()
# print(data)

# # data.sort()
# # print(data)

# numbers = [int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])]
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# max_count = numbers.count(numbers[0]) # 두번째 큰 숫자의 인덱스 번호
# print("두번째 큰 숫자:", numbers[max_count])

# # ==================================================
# # 심화 실습 2. 사칙연산 계산기 만들기 — match-case
# # ==================================================
# num1 = float(input("숫자를 입력해주세요"))
# num2 = float(input("숫자를 입력해주세요"))
# op = input("연산자를 입력해주세요(+ - * /)")

# match op:
#     case '+':
#         print(num1+num2)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         if num2 == 0:
#             print("0으로 나눌 수 없습니다")
#         else:
#             print(num1/num2)
#     case _:
#         print("알 수 없는 연산자 입니다!!!!!")

# # ==================================================
# # 심화 실습 3. ATM 출금 가능 여부 판정
# # ==================================================
# balance = int(input("현재 잔액:"))
# withdraw = int(input("출금하고 싶은 금액:"))

# # 출금 금액은 1000원 이상, 10만원 이하
# # 1000원단위로만 출금 가능함
# # 잔액이 부족한 경우 -> withdraw 보다 balance 가 작을 때

# if withdraw < 1000 or withdraw > 100000:
#     print("출금 실패: 출금 금액은 1000원 이상, 10만원 이하여야 합니다.")
# elif withdraw % 1000 != 0:
#     print("출금 실패: 1,000원단위로만 출금 가능함")
# elif withdraw > balance:
#     print("출금 실패: 잔액이 부족함")
# else:
#     balance = balance - withdraw
#     print(f"출금 성공: 출금액: {withdraw}, 잔액: {balance}")

# # ==================================================
# # 심화 실습 4. 숫자 5개의 중앙값 찾기
# # ==================================================
# # 1 2 3 4 55
# data = input("숫자 다섯개 입력: ").split()

# # numbers 가 원본데이터임.
# numbers = [int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])]
# sorted_numbers = numbers[:]
# sorted_numbers.sort()
# print(sorted_numbers)

# mid_idx = len(numbers) // 2
# # 5 -> idx 2
# # 7 -> idx 3
# # 9 -> idx 4

# 중앙값 = sorted_numbers[mid_idx]
# print(f"다섯개 숫자의 중앙값은 {중앙값}")