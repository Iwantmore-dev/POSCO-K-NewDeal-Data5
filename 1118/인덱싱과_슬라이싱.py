word = 'PYTHON'
print(word[0],word[2],word[5]) #PTN
print(word[-6], word[-4],word[-1]) #PTN
print("python"[2])

word = "Strawberry Moon ~!"
#Son!
print(word[0],word[12],word[14],word[17])
#실습1
word = "SIGNAL"
print(word[0]+word[2]+word[5])
#print(word[6]) # IndexError: string index out of range

word2 = "안녕하세요!"
#안녕!을 음수로
print(word2[-6]+word2[-5]+word2[-1])

####슬라이싱
word = 'python'
print(word[0:5]) #pytho
print(word[:4]) #pyth
print(word[1:]) #ython
print(word[1:100]) #ython, 슬라이싱은 범위 밖 번호를 지정해도 error가 발생하지 않는다.
print(word[:]) #python

#음수 인덱스를 통한 슬라이싱
print(word[-3:]) # hon word[-3:-1]을 한 경우 -1은 미포함이므로 ho가 됨.
print(word[:-1]) # pytho

#문자열[시작:끝:간격]
print(word[::2]) #pto

#실습3. 구간 자르기
word = 'signal'
print(word[:3]+'/'+word[2:5])

#추가 실습
#1.temp_sensor 저장 후 앞 4글자 추출, 2.temp_sensor에서 _이후 모든 글자 추출, 3.icecream 저장 후 슬라이싱만 이용하여 crm추출
word = 'temp_sensor'
print(word[:4])
print(word[5:])
word2 = 'icecream'
print(word2[1::3])
