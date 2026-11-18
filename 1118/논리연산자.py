# 비교 및 논리 연산자
# == 같다, != 다르다, > < >= <=
# and or not

number1 = 3
number2 = 5
print(number1 > number2) #False
print(number1 < number2) #True
print(number1 >= number2) #False
print(number1 <= number2) #True
print(number1 == number2) #False
print(number1 != number2) #True

print("==========")
print( True and True and True and False) #False
print( True or True or True or False) #True
print( not(True or True or True or False)) #False

print( (True and True) and (True or False)) #True


temp = 80
print(temp > 80 and temp < 100) # temp > 80 은 False이므로 and에 의해 전체 False
print(not(temp > 90)) # print(not(false)) True


