name = '홍길동'
status = "정상"
code = 'EQP-001'

#3개 전부 문자열임

print(name, status, code)
sentence = "It's normal" # 문자열에 "이나 '쓸 경우 "이면 '를 쓰고 '이면 "로 감싸야함.
print(sentence)
sentence2 = '이 장비는 "정상"입니다.'
print(sentence2)

sentence3 = "'장비1'은 \"정상\"이고, '장비2'는 \"비정상\"입니다."
print(sentence3)

#역슬래시를 사용하면 예외처리

sentece4 = '"장비1"은 \'정상\'이고, "장비2"는 \'비정상\'입니다.'
print(sentece4)

sentence5 = '\'장비1\'은 "정상"이고, \'장비2\'는 "비정상"입니다.'
print(sentence5)

삼중_따옴표 = """여러줄로
작성해도
에러가 나지 않는다."""
#test = "여러줄로
# 작성하면
# 에러가 나는군요"
print(삼중_따옴표)

##이스케이프 문자 \n \t \\
#\n은 줄바꿈 \t는 탭 \\는 \를 표현하기 위한 이스케이프 문자
guide = "설비점검 하는 방법 \n 1. 전원 켜기 \n 2. 센서 확인"
print("===================")
print(guide)

print("이름\t상태")
print("설비1\t정상")

print("C:\\data\\바탕화면") #C:\data\바탕화면

print('2025', '01', '15', sep="-") #sep는 프린트에서 제공하는 매개변수임. 2025-01-15

