
line = '====================================='
name = '홍길동'
age = 25
# 만들려는 문장 : 홍길동님은 25살입니다.
#기존방식

print(name+'님은 '+str(age)+'살입니다.') #,를 찍게되면 띄어쓰기가 자동으로 들어가게 되므로 +를 사용
print(f'{name}님은 {age}살입니다.') # f_string을 사용한 경우 매우 간편하게 사용가능.

code = 'EQP-001'

print(f'설비 코드 {code} 점검 완료: 온도 {25}도') #25 처럼 숫자도 그냥 중괄호에 넣어서 처리.
hours = 3
print(f'총 가동 시간(분): {hours*60}분')

value = 3.141592

print(f'pi의 소수점 둘째 자리 까지 : {value:.2f}')
print(f'pi의 소수점 넷째 자리 까지 : {value:.4f}')

'''
# ① 설비명·온도를 변수로 저장 → ② f-string을 사용해서 예상 결과와 같이 출력

# ① 세 점수를 변수로 저장 → ② f-string을 사용하여 평균을 구하는 계산식을 사용해 출력

# ① 측정값 87.456 저장 → ② 소수점 첫 번째 자리와 두 번째 자리까지 각각 출력

# ① 문자열 '  5 , sensor_2 , WARNING , 0.78912  ' 저장
# ② strip·split 후 각 조각 정리, 소수점은 두 번째 자리까지
'''
print(line)
#1
machine_name = 'EQP-123'
temp = '40'

print(f'장비 이름: {machine_name}, 현재 온도: {temp}')
print(line)
#2
no_1 = 10
no_2 = 55
no_3 = 65

print(f'세 명의 점수 합은 {no_1+no_2+no_3}이고 따라서 평균은 {(no_1+no_2+no_3)/3:.2f}')
print(line)

#3
prac3 = 87.456
print(f'{87.456:.1f}')
print(f'{87.456:.2f}')
print(line)

#4
prac4 = '  5 , sensor_2 , WARNING , 0.78912  '
prac4 = prac4.strip().split(' , ')
print(f'{prac4[0]}, {prac4[1]}, {prac4[2]}, {float(prac4[3]):.2f}')
