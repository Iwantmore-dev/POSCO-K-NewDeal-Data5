# +문자열 잇기 *문자열 반복
print('설비'+'점검') # 설비점검
print('설비'+ ' ' + '점검') # 설비 점검
line = '='*20
print(line) # 구분선을 =======로 변수로 선언한 다음 매번 print내에 작성할 필요없이 함수를 이용하여 구분선으로 터미널 가시성을 올림.

#####문자열과 관련된 함수
#len('문자열'): 문자열의 길이를 반환함.

print(len('python')) #python이므로 6자
print(len('strawberry moon ~!')) #공백 포함 18글자

phone = '01012341234'
phonelength = len(phone)
print(phonelength)

print(line)

# in, not in은 함수는 아님.

has_word = '고장' in '설비 고장을 예측하는 ~~' #T
has_word2 = '고장' not in '설비 고장을 예측하는 ~~' #F
print(has_word, has_word2)
print(line)

#중간실습

messege = '고장' in '설비 고장 발생'
messege2 = '정상' in '설비 고장 발생'
print(messege, messege2)

# count(), find(), index()
#작성 방식은 문자열.count('문자열') : 앞쪽 문자열에 '문자열'이 몇 개 들어있는지 숫자값 변환
#문자열A.find(문자열B): 문자열 A에 문자열 B가 언제 처음 등장하는지 ->인덱스를 반환해줌.
# - 문자열A에 문자열 B가 없으면 -1을 반환함
#문자열A.index(문자열B): find와 동일하지만 문자열B가 등장하지 않으면 Error발생

print("banana".count('a')) #3
print("banana".count("na")) #2

email = 'hong@company.com'
print("@의 인덱스 번호: ", email.find('@')) #4. index number이므로 01234
print('@의 인덱스 번호: ', email.index('@')) #4. 동일함.
print('@의 인덱스 번호: ', email.find('!')) # -1이므로 존재x
#print('@의 인덱스 번호: ', email.index('!')) # 존재하지 않기때문에 error발생. value error
print(line)

#실습문제 1. sensor-01-temp 저장후 count()로 -의 개수 출력
sens = 'sensor-01-temp'
print(sens.count('-')) #2


#실습문제 2. temp_2024 저장 후 find('_')로 첫 위치, 없는 글자(z)는 -1이 나오는지 확인
sens2 = 'temp_2024' #4, -1
print(sens2.find('_'), sens2.find('z'))
print(line)

#startswith /endswith
#문자열A. startswith(문자열b)
#문자열A. endswith(문자열B)

print("EQP-001".startswith("EQP"))
print("data.csv".endswith("csv"))
print(""==" ") #빈 문자열과 공백은 다른것
print("noraml" == "NORMAL") # 대소문자도 구별되는것임.

