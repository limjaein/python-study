numbers = []
length = 100

for i in range(length, 0, -1):
    numbers.append(i)

for idx, num in enumerate(numbers):
    min_idx = idx
    for n_idx in range(idx + 1, length):
        if numbers[n_idx] < numbers[min_idx]:
            min_idx = n_idx
    numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(numbers)