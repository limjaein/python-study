numbers = []
length = 100

for i in range(length, 0, -1):
    numbers.append(i)

for idx, num in enumerate(numbers):
    for n_idx in range(idx, 0, -1):
        if numbers[n_idx] > numbers[n_idx - 1]:
            numbers[n_idx], numbers[n_idx - 1] = numbers[n_idx - 1], numbers[n_idx]
        else:
            break

print(numbers)