# 튜플 자료형
# 튜플은 리스트 자료형과 거의 동일, 차이점은 아래와 같다
# 한번 선언된 값 변경 불가, 소괄호(()) 사용 (생략가능)

tup = (1,2,3)
print(tup)

tup = 1,2,3
print(tup)

# temp 없이 변수 change가 가능
c = 20
d = 30
c,d = d,c
print(c)
print(d)

# Dictionary 자료형
# 데이터를 (키, 값) 형태로 저장
# 내부적으로 해시 테이블을 이용해 검색, 수정을 O(1)로 처리 가능
data = dict()
data['사과'] = "apple"
data['바나나'] = 'banana'
print(data)
print(data.keys())
print(data.values())

# Set 자료형
# 중복을 허용하지 않으며 순서가 없음

# 집합 초기화
data = set([1,1,2,3])
print(data)

data = {1,1,2,4}
print(data)

# 검색, 추가, 삭제 : O(1)
data.add(5)
print(data)

data.update([6,7])
print(data)

data.remove(1)
print(data)


# 연산
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
print(b - a)