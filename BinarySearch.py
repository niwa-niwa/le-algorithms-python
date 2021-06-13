from typing import List


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> int:
    def _binary_search(numbers: List[int], value: int, left: int, right: int) -> int:
        print("left = ", left, "right = ", right)
        while left <= right :
            mid = (left + right) // 2
            print("mid = ", mid)
            if numbers[mid] == value :
                return mid
            elif numbers[mid] > value:
                return _binary_search(numbers, value, left, mid-1)
            else:
                return _binary_search(numbers, value, mid+1, right)
        return -1
    
    return _binary_search(numbers, value, 0, len(numbers)-1)



nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]

import random
nums = [random.randint(10, 20) for _ in range(10)]

print(nums)
value = 20
result = linear_search(nums, value)
print("linear search result = ", result)

result = binary_search(nums, value)
print("binary search result = ", result)


def my_binary_search(numbers, value):
    def _binary_search(numbers, value, left, right):
        while left <= right :
            mid = (left + right) // 2
            if numbers[mid] == value :
                return mid
            elif numbers[mid] < value :
                return _binary_search(numbers, value, mid+1, right)
            else :
                return _binary_search(numbers, value, left, mid-1)
        return -1
    return _binary_search(numbers, value, 0, len(numbers)-1)
print(my_binary_search(nums, value))


def second_binary_sort(numbers, value):
    def _binary_sort(numbers, value, left, right):
        if left <= right :
            print(left, right)
            mid = (left + right)//2
            if numbers[mid] == value :
                return mid
            elif numbers[mid] < value :
                return _binary_sort(numbers, value, mid+1, right)
            else :
                return _binary_sort(numbers, value, left, mid-1)
        return -1
    return _binary_sort(numbers, value, 0, len(numbers)-1)
        
print(second_binary_sort(nums, value))