# 문자열 자료형

# 초기화
# 기본적으로 "(쌍따옴표)를 사용함
# 내부에 '(홑따옴표) 포함가능하며 \(백슬래시) 사용시 쌍따옴표도 가능
str = " \"'Hello'\""
print(str)

# 연산
# + 사용 시 문자열이 더해짐
# * 사용 시 문자열 곱한 만큼 더해짐
# 내부적으로 리스트와 같이 처리되어 인덱싱과 슬라이싱이 가능
str = "a" + "b" + "c"
print(str)
str = str * 3
print(str)
print(str[-1])
print(str[1:4])

# 문자열 관련 함수
# a.find(b) : a에서 찾은 b 문자열의 첫번째 인덱스 반환
print(str.find('bca'))

# a.count(b) : a에서 찾은 b 문자열의 카운트 반환
print(str.count('a'))

# a.join(b) : b(문자열/튜플/리스트) 사이에 a를 삽입하여 문자열로 반환
print(",".join("abc"))
print(",".join(['a', 'b', 'c']))
print("".join(['a', 'b', 'c']))

# 소문자/대문자 처리
print("abc".upper())
print("ABC".lower())

# 공백 처리
print(" ' a b c ' ".lstrip())
print(" ' a b c ' ".rstrip())
print(" ' a b c ' ".strip())

# 문자열 바꾸기
print("abcd".replace("c", "C"))

# 문자열 나누기
print("a:b:c:d".split(":"))

# 포맷팅
str = "i have %d apples" % 5
print(str)

str = "i have %s apples" % "five"
print(str)

str = "i have {num} apples".format(num=5)
print(str)

# 자리수.소수점아래수f 로 포맷팅 가능
num = 321.1424345678
print("{0:10.4f}".format(num))


