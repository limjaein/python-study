numbers = []
length = 100

for i in range(length, 0, -1):
    numbers.append(i)


def quickSort(start, end):
    global numbers

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # left 는 pivot 보다 큰 값 탐색
        while left <= end and numbers[left] <= numbers[pivot]:
            left += 1
        # right 는 pivot 보다 작은 값 탐색
        while right > start and numbers[right] >= numbers[pivot]:
            right -= 1

        # 엇갈린 경우 작은 데이터와 Pivot 교체
        if left > right:
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:   # 엇갈리지 않았다면 left 와 right 교체
            numbers[left], numbers[right] = numbers[right], numbers[left]

    quickSort(start, right - 1)
    quickSort(right + 1, end)

quickSort(0, length - 1)


print(numbers)