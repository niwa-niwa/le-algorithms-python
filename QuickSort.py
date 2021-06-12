from typing import List

# def partition(numbers: List[int], low: int, high: int) -> int:
#     i = low -1
#     pivot = numbers[high]
#     for j in range(low, high):
#         if numbers[j] <= pivot:
#             i += 1
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
#     print('index = ', i, "numbers = ", numbers)
#     return i+1


# def quick_sort(numbers: List[int]) -> List[int]:
#     def _quick_sort(numbers: List[int], low: int, high: int) -> None:
#         print('low = ', low, 'high = ', high)
#         if low < high:
#             partition_index = partition(numbers, low, high)
#             _quick_sort(numbers, low, partition_index-1)
#             _quick_sort(numbers, partition_index+1, high)

#     _quick_sort(numbers, 0, len(numbers)-1)
#     return numbers


import random
# nums = [random.randint(0, 1000) for _ in range(10)]
# print(nums)
# print(quick_sort(nums))

def my_quick_sort(numbers):
    def _partition(numbers, low, high):
        i = low-1
        for j in range(low, high):
            if numbers[j] < numbers[high] :
                i+=1
                numbers[j], numbers[i] = numbers[i], numbers[j]
        i+=1
        numbers[high], numbers[i] = numbers[i], numbers[high]
        return i

    def _quick_sort(numbers, low, high):
        print('low = ', low, 'high = ', high)
        if low < high :
            partition = _partition(numbers, low, high)
            print('partition = ', partition)
            print(numbers)
            _quick_sort(numbers, low, partition-1)
            _quick_sort(numbers, partition+1, high)
    
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers

nums = [1,8,5,9,4,3,7]
nums = [random.randint(0, 1000) for _ in range(10)]
print(my_quick_sort(nums))

def second_quick_sort(numbers):
    def _partition(numbers, low, high):
        i = low - 1
        for j in range(low, high):
            if numbers[j] < numbers[high]:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        numbers[i], numbers[high] = numbers[high], numbers[i]
        return i

    def _quick_sort(numbers, low, high):
        if low < high:
            partition = _partition(numbers, low, high)
            _quick_sort(numbers, low, partition-1)
            _quick_sort(numbers, partition+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers

print(second_quick_sort(nums))


def new_quick_sort(numbers):
    def _partition(numbers, low, high):
        i = low-1
        for j in range(high) :
            if numbers[j] < numbers[high] :
                i+=1
                numbers[j], numbers[i] = numbers[i], numbers[j]
        i+=1
        numbers[high], numbers[i] = numbers[i], numbers[high]
        return i

    def _quick_sort(numbers, low, high):
        if low < high :
            pivot = _partition(numbers, low, high)
            _quick_sort(numbers, low, pivot-1)
            _quick_sort(numbers, pivot+1, high)
        
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers

print('new_quick_sort = ', new_quick_sort(nums))


def fast_quick_sort(numbers):
    def _partition(numbers, low, high):
        i = low-1
        for j in range(high):
            if numbers[j] < numbers[high]:
                i+=1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        i+=1
        numbers[i], numbers[high] = numbers[high], numbers[i]
        
        return i

    def _quick_sort(numbers, low, high):
        if low < high:
            pivot = _partition(numbers, low, high)
            _quick_sort(numbers, low, pivot-1)
            _quick_sort(numbers, pivot+1, high)
    
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers

print(fast_quick_sort(nums))


def force_quick_sort(numbers):
    def _pertition(numbers, low, high):
        i = low-1
        for j in range(len(numbers)-1):
            if numbers[j] < numbers[high]:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        i+=1
        numbers[i], numbers[high] = numbers[high], numbers[i]
        return i

    def _quick_sort(numbers, low, high):
        if low < high :
            pertition = _pertition(numbers, low, high)
            _quick_sort(numbers, low, pertition-1)
            _quick_sort(numbers, pertition+1, high)
    
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers
print(force_quick_sort(nums))
