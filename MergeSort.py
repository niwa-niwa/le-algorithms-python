
nums = [5, 4, 1, 8, 7, 3, 2, 9]

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0


    print(numbers)

merge_sort(nums)