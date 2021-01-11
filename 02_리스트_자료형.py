
# 리스트 자료형
# 내부적으로 연결리스트 자료구조 채택
# 리스트 혹은 배열 혹은 테이블이라고 불림

# 리스트 초기화
lists = []
print(lists)

lists = list()
print(lists)

lists = [0] * 10
print(lists)

# 리스트 컴프리헨
# 대괄호 안에 조건문과 반복문을 넣어 리스트를 초기화화는 방법
# 1과 2가 동일하게 초기화된다.
# 코딩테스트에서 2차원 배열 초기화에 효과적으로 사용됨

# ver 1
lists = []
for i in range(1, 20):
    if i % 2 == 1:
        lists.append(i)
print(lists)

# ver 2
lists = []
lists = [i for i in range(1, 20) if i % 2 == 1]
print(lists)

# 2차원 배열 초기화 (O)
n = 2
m = 3
lists = []
lists = [[0] * m for _ in range(n)]
print(lists)

# 2차원 배열 초기화 (X)
# [0] * m 이 모두 같은 객체로 인식
n = 2
m = 3
lists = []
lists = [[0] * m] * n
lists[0][1] = 1
print(lists)


# 리스트의 인덱싱과 슬라이싱
# 인덱싱 : 인덱스값을 입력하여 리스트의 특정 원소에 접근하는 것
# 파이썬은 양/음의 정수 모두 사용 가능
lists = [1,2,3,4,5,6,7,8,9]
print(lists[-1])
print(lists[1])

# 슬라이싱 : 리스트에서 연속적인 위치를 갖은 원소들을 가져오는 것
# list[a:b] => a ~ b-1 까지
print(lists[1:4])

# 리스트 관련 메소드
lists = [1,2,3,4,5,6,7,8,9]
lists.append(9) # O(1)
print(lists)

lists.remove(4) # O(N)
print(lists)

print(lists.count(9))

lists.insert(0, 0) # O(N)
print(lists)

lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)

# remove all 코드
lists = [1,2,3,4,5,2,2,1]
remove_set = [1,2]
result = [i for i in lists if i not in remove_set]
print(result)

