word = 'python'
sentence = 'I love python'
line = '================================'
#대문자 upper(), 소문자 lower(), 문장의 첫 글자만 대문자로 capitalize(), 단어마다 첫 글자를 대문자로 변경 title()
print(word.upper()) #PYTHON
print(sentence.upper()) #I LOVE PYTHON 띄어쓰기가 유지된 채로 작성됨.

print(word.count('p')) # 1, 원본 문자는 변경되지 않았음.


print("normal".upper())
print("WARNING 경고".lower()) #한글은 적용되지 않음.


print("python is good. i have an apple".capitalize()) # Python is good. i have an apple
print("python is good. i have an apple".title()) # Python Is Good. I Have An Apple

print("hong gil-dong".title()) #Hong Gil-Dong

print('apple'.lower()=='APPLE'.lower()) # True

#isupper(), islower() isupper는 전체가 대문자로 이루어져있는지, islower는 전체가 소문자로 이루어져 있는지 TF판단해줌.

print('Apple'.isupper()) # False
print('Apple'.islower()) # False

print('apple'.isupper()) # False
print('apple'.islower()) # True
print(line)
#실습

''' 
1. ready 대문자로
2. WARNING 소문자로
3. kim chul soo 성과 이름 각각 대문자로
4. fault FAULT 각각 저장후 비교
5. abc ABC Abc isupper,islower 각각 검사
6. Sensor_LOG.CSV 소문자로 변경 후 sensor로 시작하는지 .csv로 끝나는지 확인
'''

#1
print('ready'.upper()) 
#2
print('WARNING'.lower())
#3
print('kim chul soo'.title())
#4
print('fault'.lower() =='FAULT'.lower())
f1 = 'fault'
f2 = 'FAULT'
print(f1.upper() == f2.upper())
#5
print('abc'.islower())
print('abc'.isupper())
print('ABC'.islower())
print('ABC'.isupper())
print('Abc'.islower())
print('Abc'.isupper())

#6
text = 'Sensor_LOG.CSV'.lower()
print(text.startswith('sensor'))
print(text.endswith('.csv'))

#결과
#READY
#warning
#Kim Chul Soo
#True
#True
#False
#False
#True
#False
#False
#True
#True
print(line)


####### 문자열 공백 처리 ######
# strip(), 전체 공백을 제거하기 위해선 strip, 앞쪽 공백은 lstrip, 뒤쪽 공백은 rstrip
# strip 안에 문자를 넣으면 특정 글자 제거


sentence = '   안녕하세요. 저는 IWM 입니다...!'

print(sentence.strip()) # 안녕하세요. 저는 IWM 입니다....!공백 제거
print(sentence.lstrip()) # 안녕하세요. 저는 IWM 입니다....! 앞쪽 공백만 제거
print(sentence.rstrip()) #    안녕하세요. 저는 IWM 입니다....! 뒤쪽 공백만 제거
print(sentence.strip("!")) #    안녕하세요. 저는 IWM 입니다....       

print("======= 절취선 =======".strip("="))

#allie를 대문자로
#앞뒤 공백 제거 후 문자 갯수를 세기
sentence = '   allie    '
print(sentence.upper())
print(sentence.upper().strip())
print(len(sentence.upper().strip()))

print(line)


''' ~11:40
7. '  가동중 ' 변수로 저장 후 -> [가동중] 출력해보기
8. ' 대기 ' 변수로 저장 후 -> [대기 ]/[ 대기] 각각 출력
9. ***경고**** 저장 후 * 제거 후 `경고`만 출력
10. '  WARNING ' -> 'warning' 체이닝으로 출력하기
'''

#7
func1 = '  가동중 '
print('['+func1.strip()+']')
#[가동중]
#8
func2 = ' 대기 '
print('['+func2.lstrip()+']')
print('['+func2.rstrip()+']')
#[대기 ],[ 대기]
#9
func3 = '***경고****'
print(func3.strip('*'))
#경고
#10
func4 = '  WARNING '
print(func4.strip().lower())
#warning