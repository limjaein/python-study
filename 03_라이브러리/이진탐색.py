# 이진 탐색 구현을 위해 bisect 라이브러리 사용
# bisect_left(a, x) : 정렬된 순서를 유지하며 리스트 a에 x를 삽입할 왼쪽 인덱스 조회
# bisect_right(b, x) : 정렬된 순서를 유지하며 리스트 b에 x를 삽입할 오른쪽 인덱스 조회
# 두 메서드 모두 O(logN)
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 두 메서드는 a <= x <= b, 즉 x의 개수를 O(logN)으로 계산 가능
# 리스트 a에서 4의 갯수
print(bisect_right(a, 4) - bisect_left(a, 4))
# 리스트 a에서 1 ~ 3의 갯수
print(bisect_right(a, 3) - bisect_left(a, 1))