import re

print("--------------------------------------------------")

# 원하는 정규식으로 re.compile
regex = re.compile('[a-z]+')

# match : 문자열의 처음부터 정규식과 매치되는지 체크
m = regex.match("123 haha")
print(m)

# search : 문자열 전체를 검색하여 정규식과 매치되는지 체크
m = regex.search("123 haha")
print(m)

# findall : 정규식과 매치되는 모든 문자열을 리스트로 리턴
m = regex.findall("python 123 haha")
print(m)

# finditer : 정규식과 매치되는 모든 문자열 반복가능한 객체로 리턴
m = regex.finditer("python 123 haha")
print(m)

print("--------------------------------------------------")

m = regex.search("python 123 haha")

# match, search 객체의 메서드
# group : 매치된 첫 문자열 리턴
print(m.group())
# 매치된 문자열 시작 위치 리턴
print(m.start())
# 매치된 문자열 끝 위치 리턴
print(m.end())
# 매치된 문자열 (시작,끝) 튜플 리턴
print(m.span())

print("--------------------------------------------------")

# 코드 축약
regex = re.compile('[a-z]+')
m = regex.match("123 haha")
print(m)

m = re.match('[a-z]+', "123 haha")
print(m)

# 대소문자 무시
regex = re.compile('[a-z]')
print(regex.match('PYTHON'))

regex = re.compile('[a-z]', re.IGNORECASE)
print(regex.match('PYTHON'))

print("--------------------------------------------------")

text = """bingo@google.com       # 개행문자를 포함하는 문자열
hello.hello@gmail.com
olleh123@gmail.com
niceto_22@yahoo.com
niceto@yahoo111.com
niceto@yahoo.com22
notme"""

# 이메일 패턴
pattern = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, re.IGNORECASE)
print(regex.findall(text))