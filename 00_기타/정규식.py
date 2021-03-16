import re

# 원하는 정규식으로 re.compile
p = re.compile('[a-z]+')

# match : 문자열의 처음부터 정규식과 매치되는지 체크
m = p.match("123 haha")
print(m)

# search : 문자열 전체를 검색하여 정규식과 매치되는지 체크
m = p.search("123 haha")
print(m)

# findall : 정규식과 매치되는 모든 문자열을 리스트로 리턴
m = p.findall("python 123 haha")
print(m)

# finditer : 정규식과 매치되는 모든 문자열 반복가능한 객체로 리턴
m = p.finditer("python 123 haha")
print(m)

print("--------------------------------------------------")

m = p.search("python 123 haha")

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
