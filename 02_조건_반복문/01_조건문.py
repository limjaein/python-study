# 조건문
# 파이썬은 들여쓰기로 코드의 블록을 설정한다
# tab 1번 == space bar 4번 (표준)

# 논리 연산자 and/or/not
# c++, java 에서 사용하던 ! 개념은 없음
flag = False
# print(!flag)
print(not flag)

# 기타 연산자 in/not in
# 리스트, 튜플, 문자열, 사전 자료형에서 사용 가능
str = 'jaein'
print('in' not in str)

# 조건부 표현식
score = 85
result = "success" if score >= 80 else "fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)