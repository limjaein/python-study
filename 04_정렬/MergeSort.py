numbers = []
length = 100


for i in range(length, 0, -1):
    numbers.append(i)


def merge(start, middle, end):
    temp = []

    i, j = start, middle + 1

    while i <= middle and j <= end:
        if numbers[i] < numbers[j]:
            temp.append(numbers[i])
            i += 1
        else:
            temp.append(numbers[j])
            j += 1

    while i <= middle:
        temp.append(numbers[i])
        i += 1

    while j <= end:
        temp.append(numbers[j])
        j += 1

    for idx in range(end - start + 1):
        numbers[start + idx] = temp[idx]


def mergeSort(start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    mergeSort(start, mid)
    mergeSort(mid + 1, end)
    merge(start, mid, end)


mergeSort(0, length - 1)
print(numbers)