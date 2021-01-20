# collections 라이브러리 중 deque와 Counter를 주로 사용
# 1. deque : 스택/큐 구현
# 리스트는 가장 뒤쪽 원소 기준이기 때문에 뒤로 삽입/삭제 시 O(1), 다른 곳은 최대 O(N)
# 하지만 deque는 모든 삽입/삭제가 O(1)
# 인덱싱, 슬라이싱은 사용할 수 없음

# 첫번째 원소 제거 popleft(), 마지막 원소 제거 pop()
# 첫번째 원소 삽입 appendleft(x), 마지막에 원소 삽입 append(x)
from collections import deque, Counter

data = deque([2, 3, 4, 4, 4, 4])
data.appendleft(1)
data.pop()
print(data)

# Counter는 원소 등장 횟수를 세는 기능 제공
counter = Counter(data)
print(counter[4])
print(dict(counter)) # 사전 자료형으로 변환