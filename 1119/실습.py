'''log = " [WARNing] " →"WARNING"
sensors = "temp,pressure,vibration"  → "VIBRATION / PRESSURE / TEMP"
data = " EQP-01 , NORMAL , 85.5 " → "normal"
text = " ###[ PUMP-07 ]### " → "pump_07"
data = " TEMP / Pressure | vibration " → "temp,pressure,vibration"
'''
line = "===================="
#1
#log = " [WARNing] " →"WARNING"

log = " [WARNing] "
print(log.strip().replace("[","").replace("]","").upper())

#2
#sensors = "temp,pressure,vibration"  → "VIBRATION / PRESSURE / TEMP"
sensors = "temp,pressure,vibration"
print(' / '.join(sensors.upper().split(',')[::-1]))

#3
data = " EQP-01 , NORMAL , 85.5 "
print(data.split(',')[1].lower().strip())

#4
#text = " ###[ PUMP-07 ]### " → "pump_07"
text = " ###[ PUMP-07 ]### "
print(text.strip(' #[]').replace('-','_').lower())


#5
#data = " TEMP / Pressure | vibration " → "temp,pressure,vibration"
data = " TEMP / Pressure | vibration "
print(data.replace(" ","").replace('/',',').replace('|',',').lower())

print(line)
#####심화실습1. 두 시점의 센서 데이터 비교 분석#####
# 두 데이터를 구분자에 맞춰 분리
# 설비 코드 대문자 통일 및 - -> _로 변경
# 온도 단위 제거 후 실수형으로 변환
# 상태 데이터를 소문자로 통일
data1 = "pump-07 | 08:30 | TEMP=085.5C | STATUS=normal"
data2 = "PUMP_07,09:00,92.0C,WARNING"

#구분자 맞춰 분리
test1 = data1.split(" | ")
test2 = data2.split(",")

#대문자 통일 및 하이픈을 언더바로
test1[0] = test1[0].upper().replace("-",'_')
test2[0] = test2[0].upper()

# 온도를 실수형으로 변환, 단위 제거
test1[2] = float(test1[2].replace("TEMP=","").replace("C", ""))
test2[2] = float(test2[2].replace("C", ""))

# 상태를 소문자로 통일
test1[3] = test1[3].replace("STATUS=", "").lower()
test2[3] = test2[3].lower()


      

#설비 코드 일치 여부 확인 및 최초 측정, 최근 측정
print(f'설비코드:{test1[0]}')
print("설비 코드 일치여부 확인 :", test1[0]==test2[0])
print(f'최초 측정: {test1[1]}/{test1[2]}/{test1[3]}')
print(f'최근 측정: {test2[1]}/{test2[2]}/{test2[3]}')

#온도 차이 및 최초 온도 대비 상승률(%) 계산
print(f'온도차이 : {float(test2[2]) - float(test1[2])}')
print(f'최초 온도 대비 상승률 : {(float(test2[2])-float(test1[2])) / float(test1[2])*100:.2f}%')
#동일 설비이고 온도 6도 이상 상승했는지 판별

print(f'온도 급상승 여부: {test1[0] == test2[0] and test2[2] - test1[2] >= 6}')

print(line)
####실습2. 설비 작업 완료 예정 시간 계산
# 주어진 데이터 log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09"

#로그에서 날짜, 시작 시각, 소요시간, 설비 코드 추출
log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09"
print(log.replace("|","").split())
log = log.replace("|","").split()

#시작 시각을 시분초로 나눠서 정수 추출
time = log[1].split(":")
print(time)
hours = int(time[0])
minutes = int(time[1])
sec = int(time[2])

#delay에서 135추출
delay = int(log[2].replace("DELAY=", "").replace("s", ""))

#완료시간을 시,분,초로 재계산
total = hours * 3600 + minutes * 60 + sec + delay #계산의 편의성을 위해
end_hour = (total // 3600) % 24 # %는 나머지
end_minute = (total % 3600) // 60 # //는 몫
end_sec = total % 60

# 날짜 변경 여부
date_change = total >= 86400 #하루는 86400초


print(f'=====설비 작업 정보=====')
print(f'설비 코드:{log[3]}')
print(f'작업 날짜:{log[0]}')
print(f'작업 시작 시각:{hours}시 {minutes}분 {sec}초')
print(f'소요시간:{delay}초')

print(f"완료 시간: {end_hour}시 {end_minute}분 {end_sec}초")
print(f"날짜 변경 여부: {date_change}")

print(line)
####실습3.생산 데이터 통합 및 불량률 분석

line1 = "LOT-A | 1,200 | 36 | 8h"
line2 = "lot_a,850,17,5h"
#(두 변수 모두 - 생산라인코드, 생산량, 불량품수, 가동시간 순)

#1. 생산라인 코드를 대문자 언더바 형식으로 통일
line1 = line1.split(" | ") #['LOT-A', '1,200', '36', '8h']
line2 = line2.split(",") #['lot_a', '850', '17', '5h']
line1[0] = line1[0].replace("-","_") #['LOT_A', '1,200', '36', '8h']
line2[0] = line2[0].upper() #['LOT_A', '850', '17', '5h']
#print(line1, line2)

#2. 생산량과 불량품 수를 정수형으로 변환
prod1 = int(line1[1].replace(",","")) #line1의 생산량 1200. 1,200이므로 ,제거해야함.
prod2 = int(line2[1]) #line2의 생산량 850
#print(prod1, prod2)

fault1 = int(line1[2]) #line1의 불량품 수 36
fault2 = int(line2[2]) #line2의 불량품 수 17
#print(fault1, fault2)

#3. 가동시간 h 제거 후 정수형으로 변환
hour1 = int(line1[3].replace("h", ""))
hour2 = int(line2[3].replace("h", ""))
#print(hour1, hour2)

#4. 각 데이터의 불량률(%) 계산
rate1 = fault1 / prod1 * 100
rate2 = fault2 / prod2 * 100
#print(rate1, rate2)

#5. 2차 불량률이 1차보다 낮은지 판별
improved_second = rate2 < rate1
#print(improved_second) #true

#6. 전체 생산량 및 전체 불량품 수 계산
total_prod = prod1 + prod2
total_fault = fault1 + fault2
#print(total_prod, total_fault) #2050, 53

#7. 통합 불량률을 전체 불량품 수/전체 생산량으로 계산
total_rate = total_fault / total_prod * 100
#print(total_rate) #2.5853658536585367

#8. 가동시간 합산 후 시간당 평균 생산량 계산
avg_prod = total_prod / (hour1 + hour2)
#print(avg_prod) #157.69230769230768

#9. 두 line이 동일 라인이며 시간의 흐름에 따라 수집된 데이터라인 불량률이 개선되었는지 판단
same_line = line1[0] == line2[0]
final = same_line and improved_second
#print(same_line, final) #T, T

#10. 비율 및 평균은 소수점 둘째 자리까지 출력
print("===== 생산 데이터 분석 =====")
print(f"생산라인 코드: {line1[0]}")
print(f"라인 코드 일치: {same_line}")
print()
print(f"[1차 생산] 생산량 {prod1}개 / 불량품 {fault1}개")
print(f"불량률: {rate1:.2f}%")
print(f"[2차 생산] 생산량 {prod2}개 / 불량품 {fault2}개")
print(f"불량률: {rate2:.2f}%")
print()
print(f"[통합 분석] 생산량 {total_prod}개 / 불량품 {total_fault}개")
print(f"통합 불량률: {total_rate:.2f}%")
print(f"시간당 평균 생산량: {avg_prod:.2f}개")
print()
print(f"불량률 개선 여부: {improved_second}")
print(f"최종 판정: {final}")



# ########## 실습 4

# '''
# 1. 생산라인 코드를 대문자·언더바 형식으로 통일
# 2. 생산량과 불량품 수를 정수형으로 변환
# 3. 가동시간 h 제거 후 정수형으로 변환
# 4. 각 데이터의 불량률(%) 계산
# 5. 2차 불량률이 1차보다 낮은지 판별
# 6. 전체 생산량 및 전체 불량품 수 계산
# 7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
# 8. 가동시간 합산 후 시간당 평균 생산량 계산
# 9. 두 line이 동일 라인이며 (시간의 흐름에 따라 수집된 데이터라면 )불량률이 개선되었는지 판단
# 비율 및 평균은 소수점 둘째 자리까지 출력
# '''
# # 생산라인코드 생산략 불량품수 가동시간
# line1 = " LOT-A | 1,200 | 36 | 8h "
# line2 = "lot_a,850,17,5h"

# parts1 = line1.split('|')
# parts2 = line2.split(',')
# print(parts1, parts2)

# # 1. 생산라인 코드를 대문자·언더바 형식으로 통일
# code1 = parts1[0].strip().upper().replace('-','_')
# code2 = parts2[0].strip().upper().replace('-','_')
# print(code1, code2)

# # 2. 생산량과 불량품 수를 정수형으로 변환
# total1 = int(parts1[1].strip().replace(',',''))
# total2 = int(parts2[1].strip())
# print(total1, total2)

# defect1 = int(parts1[2].strip())
# defect2 = int(parts2[2].strip())
# print(defect1, defect2)

# # 3. 가동시간 h 제거 후 정수형으로 변환
# hours1 = int(parts1[3].strip().replace('h',''))
# hours2 = int(parts2[3].strip().replace('h',''))
# print(hours1, hours2)

# # 4. 각 데이터의 불량률(%) 계산
# rate1 = defect1 / total1 * 100
# rate2 = defect2 / total2 * 100
# print(rate1, rate2)

# # 5. 2차 불량률이 1차보다 낮은지 판별
# is_improved = rate1 > rate2
# print("불량률이 낮아졌나요?", is_improved)

# # 6. 전체 생산량 및 전체 불량품 수 계산
# total = total1 + total2
# defect = defect1 + defect2

# # 7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
# rate = defect / total * 100

# # 8. 가동시간 합산 후 시간당 평균 생산량 계산
# total_hours = hours1 + hours2
# # 평균 생산량
# hourly_avg = total / total_hours
# print(f'시간당 평균생산량: {hourly_avg:.2f}')

# # 9. 두 line이 동일 라인이며 시간의 흐름에 따라 수집된 데이터라면 불량률이 개선되었는지 판단
# is_same_code = code1 == code2
# result = is_improved and is_same_code
# print(f'같은 라인이고, 불량률이 개선되었나요? {result}')

####수정
# log = " [WARNing] " →"WARNING"
# sensors = "temp,pressure,vibration" → "VIBRATION / PRESSURE / TEMP"
# data = " EQP-01 , NORMAL , 85.5 " → "normal"
# text = " ###[ PUMP-07 ]### " → "pump_07"
# # data = " TEMP / Pressure | vibration " → "temp,pressure,vibration"
# from turtle import delay


# log = " [WARNing] "
# sensors = "temp,pressure,vibration"
# data = " EQP-01 , NORMAL , 85.5 "
# text = " ###[ PUMP-07 ]### "
# data2 = " TEMP / Pressure | vibration "
# print(log.upper()[2:9])
# print(" / ".join(sensors.split(",")[::-1]).upper())
# print(data.split(" , ")[1].lower())
# print(text[6:13].replace("-", "_").lower())
# print(data2.strip().lower().replace(" / ",',').replace(" | ", ','))

# ##### 실습2 #####
# log = " 2026/11/19 23:58:45 | DELAY=135s | EQP-09 "
# '''
# 1. 로그에서 날짜·시작 시각·소요시간·설비 코드 추출
# 2. 시작 시각을 시·분·초로 나눠 정수 변환
# 3. DELAY=135s에서 '135' 만 추출
# 4. 시작 시간을 XX시 XX분 XX초 형태로 변경
# 5. 완료 시간: 시작 시간에 소요 시간을 더한 후 자정 경과 여부 판단
# 6. 완료 시각을 시·분·초로 재계산
# 7. 완료 시각과 날짜 변경 여부를 f-string으로 출력
# 8. 날짜 자체를 다음 날로 바꿀 필요는 없음
# '''
# # 1. 정보 추출
# parts_list = log.split("|")
# print(parts_list)
# date = parts_list[0].split()[0].strip()
# start_time = parts_list[0].split()[1].strip()
# # print(date, start_time)
# delay = parts_list[1].strip() # DELAY=135s
# delay = delay.replace("DELAY=","").replace("s","")
# delay = int(delay)
# # print(delay)
# code = parts_list[2].strip()
# # print(code)

# # 2. 시작 시각을 시·분·초로 나눠 정수 변환
# time_parts_list = start_time.split(":")
# print(time_parts_list)
# hour = int(time_parts_list[0])
# min = int(time_parts_list[1])
# sec = int(time_parts_list[2])

# # 4. XX시 XX분 XX초 로 변환하여 저장
# time = f'{hour}시 {min}분 {sec}초'

# # 5. 완료 시간: 시작 시간에 소요 시간(delay)을 더한 후 자정 경과 여부 판단
# # 시작시간 23:58:45 소요시간 135초
# total_seconds = hour*(60*60) + min * 60 + sec
# # 자정이 지났으면 True
# day_changed = total_seconds + delay >= (24*60*60)
# print("자정이 지났나요?", day_changed)

# # 6. 완료 시각을 시·분·초로 재계산
# end_time = total_seconds + delay
# print(end_time)

# day_seconds = 24 * 60 * 60
# remaining = end_time % day_seconds

# end_hour = remaining // (60*60)
# remaining = remaining % (60*60)

# end_min = remaining // 60
# end_sec = remaining % 60
# print(f'최종 작업 완료 시간: {end_hour}시 {end_min}분 {end_sec}초')

# #### 실습 4

# '''
# 1. 생산라인 코드를 대문자·언더바 형식으로 통일
# 2. 생산량과 불량품 수를 정수형으로 변환
# 3. 가동시간 h 제거 후 정수형으로 변환
# 4. 각 데이터의 불량률(%) 계산
# 5. 2차 불량률이 1차보다 낮은지 판별
# 6. 전체 생산량 및 전체 불량품 수 계산
# 7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
# 8. 가동시간 합산 후 시간당 평균 생산량 계산
# 9. 두 line이 동일 라인이며 (시간의 흐름에 따라 수집된 데이터라면 )불량률이 개선되었는지 판단
# 비율 및 평균은 소수점 둘째 자리까지 출력
# '''
# # 생산라인코드 생산략 불량품수 가동시간
# line1 = " LOT-A | 1,200 | 36 | 8h "
# line2 = "lot_a,850,17,5h"

# parts1 = line1.split('|')
# parts2 = line2.split(',')
# print(parts1, parts2)

# # 1. 생산라인 코드를 대문자·언더바 형식으로 통일
# code1 = parts1[0].strip().upper().replace('-','_')
# code2 = parts2[0].strip().upper().replace('-','_')
# print(code1, code2)

# # 2. 생산량과 불량품 수를 정수형으로 변환
# total1 = int(parts1[1].strip().replace(',',''))
# total2 = int(parts2[1].strip())
# print(total1, total2)

# defect1 = int(parts1[2].strip())
# defect2 = int(parts2[2].strip())
# print(defect1, defect2)

# # 3. 가동시간 h 제거 후 정수형으로 변환
# hours1 = int(parts1[3].strip().replace('h',''))
# hours2 = int(parts2[3].strip().replace('h',''))
# print(hours1, hours2)

# # 4. 각 데이터의 불량률(%) 계산
# rate1 = defect1 / total1 * 100
# rate2 = defect2 / total2 * 100
# print(rate1, rate2)

# # 5. 2차 불량률이 1차보다 낮은지 판별
# is_improved = rate1 > rate2
# print("불량률이 낮아졌나요?", is_improved)

# # 6. 전체 생산량 및 전체 불량품 수 계산
# total = total1 + total2
# defect = defect1 + defect2

# # 7. 통합 불량률을 전체 불량품 수 / 전체 생산량으로 계산
# rate = defect / total * 100

# # 8. 가동시간 합산 후 시간당 평균 생산량 계산
# total_hours = hours1 + hours2
# # 평균 생산량
# hourly_avg = total / total_hours
# print(f'시간당 평균생산량: {hourly_avg:.2f}')

# # 9. 두 line이 동일 라인이며 시간의 흐름에 따라 수집된 데이터라면 불량률이 개선되었는지 판단
# is_same_code = code1 == code2
# result = is_improved and is_same_code
# print(f'같은 라인이고, 불량률이 개선되었나요? {result}')