numbers = []
length = 100

for i in range(length, 0, -1):
    numbers.append(i)

for _ in range(length):
    for i in range(length - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(numbers)