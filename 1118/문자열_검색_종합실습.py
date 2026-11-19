#주어진 문자열은 NORMAL-WARNING-NORMAL_ERROR-WARNING이다.
#1.WARNING은 몇번?
prob1 = 'NORMAL-WARNING-NORMAL-ERROR-WARNING'
print(prob1.count('WARNING')) #2
#2.NORMAL은 몇번?
print(prob1.count('NORMAL')) #2
#3.ERROR는 몇번?
print(prob1.count('ERROR')) #1
#4.첫 번째 WARNING의 시작 위치는?
print(prob1.find('WARNING')) #7
#5.두 번째 WARNING의 시작 위치를 구하기
print(prob1.find('WARNING',8)) #28
#6첫 번째 WARNING의 끝 위치와 두 번째 WARNING의 시작 위치 사이에 몇 글자가 있는가?
prob1 = 'NORMAL-WARNING-NORMAL-ERROR-WARNING'

first = prob1.find('WARNING')        # 7
second = prob1.find('WARNING', 8)    # 28
#rfind로도 찾을 수 있다.

print(second - (first + len('WARNING'))) #14
#7.두 WARNING 사이에 들어있는 문자열만 추출
middle = prob1[first + len('warning'): second]
print(middle) #-NORMAL-ERROR-

#8.7번에서 추출한 문자열에 ERROR가 포함되어있는가?
print('ERROR' in middle)
