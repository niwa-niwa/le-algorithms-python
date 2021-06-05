from typing import List

# TODO : it should be written by myself
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low -1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    print('index = ', i, "numbers = ", numbers)
    return i+1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        print('low = ', low, 'high = ', high)
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


import random
nums = [random.randint(0, 1000) for _ in range(10)]
print(nums)
print(quick_sort(nums))
