from typing import List

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

print(selection_sort([1,5,2,8,7,3]))

def my_selection_sort(numbers: List[int]) -> List[int]:
    length = len(numbers)
    for i in range(length-1):
        min = i
        for j in range(i+1, length):
            if numbers[min] > numbers[j]:
                min = j
        numbers[min], numbers[i] = numbers[i], numbers[min]
    return numbers

print(my_selection_sort([1,5,2,8,7,3]))
