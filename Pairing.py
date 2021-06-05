from typing import List, Tuple, Optional


nums = [11, 2, 5, 9, 10, 3]
value = 12

# Find a combination that adds up to 12
def twelve(numbers, value):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            print(numbers[i],"+",numbers[j])
            if value == (numbers[i]+numbers[j]):
                return [numbers[i], numbers[j]]
    return None
print(twelve(nums, value))


# Find a combination that adds up to 12 with set()
def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        print('val = ', val)
        if val in cache:
            return val, num
        cache.add(num)
print(get_pair(nums, value))


# If the sum is divisible by 2, divide the sum into two
def get_pair_half_sum(numbers):
    if sum(numbers) % 2 != 0:
        return None
    half_sum = int(sum(numbers)/2)

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:

            return val, num,
        cache.add(num)
    return True
print(get_pair_half_sum(nums))
