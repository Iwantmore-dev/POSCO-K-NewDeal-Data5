#실습1. 사칙연산 계산기
a = 17
b = 5
print(a+b,a-b,a*b,a/b) #22 12 85 3.4
print(a//b,a%b,a**b) #3 2 1419857

#실습2.평균과 도형 계산
a = 17 #가로
b = 5 #세로
c = 22 #높이
print("평균: ", (a+b+c)/3, "넓이: ", (a*b), "부피: ", a*b*c) # 평균:  14.666666666666666 넓이:  85 부피:  1870 단, 넓이의 경우 a와 b를 기준으로 하였음.

#실습5. 설비 지표 계산
'''전체500, 불량23일때 불량률 계산
    가동 21h, 전체 24h일때 가동률 계산'''

total = 500
fail = 23
fail_rate = fail/total
print(fail_rate*100,'%') #4.6%
working = 21
day_hour = 24
operating_rate = working/day_hour

print(operating_rate*100,'%') #87.5%

#실습6. 시간변환
'''500분을 시간, 분으로 변환하여 출력'''
total_minutes = 500
print(total_minutes//60,'시간',total_minutes%60,'분') #8 시간 20 분

#실습7. 프로그램 실행시간 계산해보기 (NN초를 시간으로)
#가정 : 어떤 프로그램의 실행 시간이 98765초라고 하자, 이 시간을 일/시간/분/초로 변환하여 출력해보기 (//와 %연산자 사용)
time_sec = 98765

time_minutes = (time_sec // 60) % 60
time_hour = (time_sec // 3600) % 24
time_day = time_sec // 86400
time_seconds = time_sec % 60

print(time_day, "일", time_hour, "시간", time_minutes, "분", time_seconds, "초")
#1 일 3 시간 26 분 5 초

#실습8. 정상범위와 다중센서 판정
temp = 85 #60이상, 90이하인지 비교하고 새 변수에 저장
press = 5 #3이상, 7이하인지 비교하고 새 변수에 저장
temp_new = temp>=60 and temp<=90
press_new = press >=3 and press<=7
print("온도 정상",temp_new,"압력 정상", press_new, "모두 정상", temp_new and press_new)
# 온도 정상 True 압력 정상 True 모두 정상 True
