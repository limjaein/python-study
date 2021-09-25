numbers = [1, 0, 3, 2, 4, 3, 2, 2, 1, 1, 1, 1, 5, 3, 3, 4, 5]
k = 5
counts = []
result = []

length = len(numbers)
counts = [0] * length

for num in numbers:
    counts[num] += 1

for num, cnt in enumerate(counts):
    for _ in range(cnt):
        result.append(num)

print(result)