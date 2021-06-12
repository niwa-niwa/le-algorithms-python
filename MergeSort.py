import random

nums = [5, 4, 1, 8, 7, 3, 2, 9]
nums = [random.randint(0, 1000) for _ in range(10)]

def merge_sort(numbers):
    if len(numbers) == 1:
        return 

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_index = right_index = merge_index = 0

    while left_index <= len(left)-1 and right_index <= len(right)-1:
        if left[left_index] < right[right_index]:
            numbers[merge_index] = left[left_index]
            left_index += 1
        else:
            numbers[merge_index] = right[right_index]

            right_index += 1

        merge_index += 1

    while right_index < len(right):
        numbers[merge_index] = right[right_index]
        right_index += 1
        merge_index += 1

    while left_index < len(left):
        numbers[merge_index] = left[left_index]
        left_index += 1
        merge_index += 1

    return numbers

print(merge_sort(nums))


def my_merge_sort(numbers):
    if(len(numbers) <= 1):
        return

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    left_index = right_index = total_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            numbers[total_index] = left[left_index]
            left_index += 1
        else:
            numbers[total_index] = right[right_index]
            right_index += 1
        total_index += 1

    while left_index < len(left):
        numbers[total_index] = left[left_index]
        total_index += 1
        left_index += 1

    while right_index < len(right):
        numbers[total_index] = right[right_index]
        total_index += 1
        right_index += 1

    return numbers

print(my_merge_sort(nums))


def fast_merge_sort(numbers):
    if len(numbers) <= 1 :
        return

    partition = len(numbers) // 2
    left = numbers[:partition]
    right = numbers[partition:]

    left_index = right_index = total_index = 0
    if left_index < len(left) and right_index < len(right) :
        if left[left_index] <= right[right_index] :
            numbers[total_index] = left[left_index]
            left_index += 1
        else:
            numbers[total_index] = right[right_index]
            right_index += 1
        total_index += 1
    
    if left_index < len(left):
        numbers[total_index] = left[left_index]
        left_index += 1
        total_index += 1

    if right_index < len(right):
        numbers[total_index] = right[right_index]
        right_index += 1
        total_index += 1

    return numbers

print(fast_merge_sort(nums))