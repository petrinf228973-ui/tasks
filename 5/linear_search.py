def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 25, 30, 45, 50]
x = 30

print("Массив:", numbers)
result = linear_search(numbers, x)
if result != -1:
    print(f"Элемент {x} на позиции {result}")
else:
    print(f"Элемент {x} не найден")
