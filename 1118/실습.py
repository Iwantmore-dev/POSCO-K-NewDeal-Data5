#이름을 입력받아 인사말 출력
#예시: 안녕하세요 (name)님!

#name = input("이름을 입력해주세요 : ")
#print("안녕하세요", name, "님!")


#실습1.여러 줄 문자열 만들기
#삼중 따옴표 사용
table = """가동 점검표
1.온도 확인
2.압력 확인"""

print(table)
print("======================")
#\n 사용
table = "가동 점검표 \n1.온도 확인 \n2.압력 확인"
print(table)
print("======================")

#\n과 \t 사용
table = "가동 점검표 \n1.온도\t 확인 \n2.압력\t 확인"
print(table)
print("=======================")
#실습2.설비 라벨 이어 붙이기
#print하나만 사용하여 PUMP_A/정상/2025-01-15 출력하기

code = "PUMP_A"
status = "normal"
date = "2025-01-15"

print(code + "/" + status + "/" + date)
print(code, status, date, sep=" / ")

print("처리중", end='...')