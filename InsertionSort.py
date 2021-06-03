
from typing import List
import random


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i -1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers

nums = [random.randint(0, 1000) for _ in range(10)]
print("nums = ", nums)

print(insertion_sort(nums))


def my_insertion_sort(numbers: List[int]) -> List[int]:
    length = len(numbers)
    for i in range(1, length):
        tmp = i
        j = i - 1
        while j >= 0 and numbers[j] > numbers[tmp]:
            numbers[j+1] = numbers[j]
            j-=1

        numbers[j+1] = numbers[tmp]
    return numbers

# nums = [1, 3, 5, 5, 6, 2]
print(my_insertion_sort(nums))
