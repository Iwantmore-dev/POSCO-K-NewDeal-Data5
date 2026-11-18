#실습-심화
#input()으로 인증 코드를 입력받기. 인증코드 형식 : SEC-2026-5832-X
#출력 조건 : 8가지 검증 항목 결과를 True, False로 출력. 모든 조건 만족 시 최종 인증을 True로 출력
''' 1. 인증 코드는 SEC-로 시작해야 합니다.
    2. 인증 코드의 전체 길이는 15자여야 합니다.
    3. 코드의 연도는 2026이어야 합니다.
    4. 마지막 문자는 X또는 Y여야 합니다.
    5. 세번째 항목의 네 자리 숫자는 1000~9999 사이여야 합니다.
    6. 하이픈(-)이 정확히 3개 등장해야 합니다.'''
#위의 모든 조건을 만족하는지 출력할것.
#SEC-2026-5832-X, SEC-2026-0833-X

#1
verification_code = input("인증 코드를 입력해 주세요 : ")
verf_start = verification_code.startswith('SEC-')
print('인증 코드가 "SEC-"로 시작합니까?', verf_start)

#2
verf_length = len(verification_code) ==15
print('인증 코드의 전체 길이는 15자 입니까?', verf_length)

#3
verf_year = verification_code[4:8] == "2026"
print("코드의 연도는 2026이어야 합니다.", verf_year)

#4
verf_end = verification_code.endswith('X') or verification_code.endswith('Y')
print('인증 코드 마지막 문자는 X 또는 Y여야 합니다.',verf_end)

#5
verf_third = int(verification_code[9:13]) >= 1000 and int(verification_code[9:13]) <= 9999
print("세 번째 항목의 네 자리 숫자는 1000에서 9999사이여야 합니다.", verf_third)

#6
verf_hype = verification_code.count('-') == 3
print("하이픈(-)이 정확히 3개 등장해야 합니다.", verf_hype)

isSignUp = (verf_start and verf_length and verf_year and verf_end and verf_third
            and verf_hype)
print("인증 가능?", isSignUp)

#SEC-2026-5832-X는 True. SEC-2026-0833-X는 False #5에 의거.