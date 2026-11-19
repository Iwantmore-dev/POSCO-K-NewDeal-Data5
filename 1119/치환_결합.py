#replace 사용연습
line = '======================'
print(" 정 상 가 동".replace(" ", "-"))
print(" 정 상 가 동".replace(" ","")) #모든 공백 제거


print("fault".replace("fault","고장"))

# '3,000' -> 숫자 3000으로 바꾸기

print(int('3,000'.replace(",","")))
# 010 -1234 5678 -> 01012345678

print('010-1234 5678'.replace("-","").replace(" ",""))


#문자열.split(생략구분자)
list = [10, 20, 30, "hello", False]

print(list[3])
print(list[1])


coffee = '에스프레소 카페라테 아메리카노'
print(coffee.split()) #['에스프레소', '카페라테', '아메리카노']

coffee_list = coffee.split() #공백기준으로 잡아줌. 공백 한칸을 기준으로 하는것은 아님

print(coffee_list[2])

print('사과,배,감'.split(","))
print('사과,배,감'.split(',')[2])

date = '2025-01-15'
day = date.split('-')[2] #date.split('-')을 하면 리스트화 되어서['2025','01','15']가 되고 이 리스트의 2번항목이므로 0,1,2에서 15

print(day) #15


print(coffee.split(" ",1)) #['에스프레소','카페라테 아메리카노']

'''
#① '설비 정상 가동' 저장 → ② '정상'을 '점검'으로 바꿔 출력
#① 'PUMP A 03' 저장 → ② 공백 기준 분리하여 리스트 출력
#① 'a,b,c,d' 저장 → ② ','을 기준으로 분리
#① 'a,b,c,d' 저장 → ② 첫 번째 ','을 기준으로 한 번만 나누기
'''

test = '설비 정상 가동'
print(test.replace('정상','점검')) #설비 점검 가동
test2 = 'PUMP A 03'
print(test2.split()) #['PUMP', 'A', '03']
test3 = 'a,b,c,d'
print(test3.split(',')) #['a', 'b', 'c', 'd']
print(test3.split(',',1)) #['a', 'b,c,d']

# 구분자가 될 문자열 .join([리스트])
list1 = ['2026','11','19']
# 2026-11-19, 2026.11.19

print('-'.join(list1))
print('.'.join(list1))

'''
#1. ① ['2025','01','15'] 준비 → ② '-'으로 연결하여 합치기

#2. 2025·1·15 를 '-' 와 ','로 총 2가지 방법을 사용해 이어서 출력

# 3. ① '2025/01/15' 저장 → ② '/'을 기준으로 나눈 후 '-' 으로 합치기

#4. ① '1, NORMAL ,25.3' 저장
② ',' 기준으로 나누어 1번 인덱스를 공백 제거와 소문자로 변환해 출력
'''
print(line)

#1
list_t1 = ['2025','01','15']
print('-'.join(list_t1))
print(line)
#2
date_test = '2025·1·15'
print(date_test.replace('·','-'))
print(date_test.replace('·',','))

print(','.join(date_test.split('·')))
print(line)
#3
test4 = '2025/01/15'
print('-'.join(test4.split('/')))
print(line)
#4
prac4 = '1, NORMAL ,25.3'
prac4 = prac4.split(',') #스플릿 되어 리스트형태가 되었음.prac4
print(prac4[1].strip().lower())

