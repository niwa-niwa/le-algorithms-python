
nums = [5, 4, 1, 8, 7, 3, 2, 9]

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