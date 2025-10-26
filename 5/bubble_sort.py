def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [5, 3, 8, 4, 2]
print("Исходный массив:", numbers)
bubble_sort(numbers)
print("Отсортированный массив:", numbers)
