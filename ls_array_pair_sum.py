"""Array pari sum, leetcode 561, level 1"""

import time

def array_pair_sum_v1(nums):
    """Use even indexes"""
    nums.sort()
    result = [num for i, num in enumerate(nums) if i % 2 == 0]
    return sum(result)

def array_pair_sum_v2(nums: list) -> int:
    """Use even indexes and Pythonic way"""
    return sum(sorted(nums)[::2])

if __name__ == "__main__":

    ex = [-1, 0, 1, 2, -1, -4]
    start = time.time()
    array_pair_sum_v1(ex)
    print((f"Sum even indexes: {time.time() - start:0.9f}"))

    ex = [-1, 0, 1, 2, -1, -4]
    start = time.time()
    array_pair_sum_v2(ex)
    print((f"Use the slicing and sum even indexes: {time.time() - start:0.9f}"))
