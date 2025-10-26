def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

numbers = [9, 8, 3, 7, 5, 6, 4, 1]
print("Исходный массив:", numbers)
shell_sort(numbers)
print("Отсортированный массив:", numbers)
