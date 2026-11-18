'''
0. 아이디, 비밀번호, 이메일을 받아서 계정 검증을 하는 프로그램.
1. 아이디 길이는 6자 이상 12자 이하입니다.
2. 아이디는 user_로 시작해야 합니다.
3. 비밀번호는 8자 이상이어야 합니다.
4. 비밀번호에는 ! 또는 @ 중 하나 이상이 포함되어야 합니다.
5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
6. 이메일은 @가 정확히 한 번 등장해야 합니다.
7. 이메일은 .com으로 끝나야 합니다.
모든 조건을 만족해야 최종 회원가입 가능 여부가 True가 됩니다.
'''


User_ID = input("아이디를 입력해주세요: ")
password = input("비밀번호를 입력해주세요: ")
email = input("이메일을 입력해 주세요: ")

#User_ID 조건 1. 6~12자 길이 2. user_로 시작할것.
#and를 사용하여 조건을 묶는다.
id_length = len(User_ID) >=6 and len(User_ID) <= 12 #ID의 길이를 알려줌.
print("비밀번호가 6~12자입니까?", id_length)
id_start = User_ID.startswith("user_")
print("user_로 아이디가 시작합니까??", id_start)

#3. 비밀번호는 8자 이상이어야함.
pw_length = len(password) >= 8
print("비밀번호 8자 이상?", pw_length)
#4. 비밀번호에는 !또는 @중 하나 이상이 포함되어야 함.
pw_word = ('!' in password) or ('@' in password)
print("!나 @가 있는가?", pw_word)
#5. 비밀번호에 아이디 전체가 포함되어 있으면 안 됩니다.
pw_no_id = User_ID not in password
print("비밀번호에 아이디 전체가 포함되어 있습니까?", pw_no_id) #다만 확인 결과 user_1234가 아이디이고 비밀번호가 user_123이라면 True로 나옴.

#이메일 조건
#6. 이메일은 @가 정확히 한 번 등장해야 합니다.
email_at = email.count('@') ==1
print("이메일에 @가 한번만 들어가는지?", email_at)
#7. 이메일은 .com으로 끝나야 합니다.
email_end = email.endswith('.com')
print("이메일이 .com으로 끝나는지?", email_end)

isSignUp = (id_length and id_start and pw_length and pw_word and pw_no_id
            and email_at and email_end)
print("회원가입 가능?", isSignUp)
