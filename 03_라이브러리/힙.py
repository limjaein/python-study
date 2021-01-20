# heap 기능을 위해 heapq 라이브러리를 사용
# heapq는 우선순위 큐 기능 구현을 위해 사용, PriorityQueue 보다 빠름
import heapq

def heapsort(values):
    h = []
    result = []
    for value in values:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 기본 최소 힙이며 최대 힙을 제공하지 않음
# 부호 변경으로 최대 힙 구현