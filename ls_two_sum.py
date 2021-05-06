"""Two sum, leetcode #1"""

import time

def two_sum_ver1(nums: list, target: int) -> list:
    """Use try and except"""
    for i, num in enumerate(nums):
        try:
            return [nums.index(num), nums.index(target - num, i + 1)]
        except ValueError:
            continue
    return None

def two_sum_ver2(nums: list, target: int) -> list:
    """Use dictionay"""
    # Save numbers and indexes
    num_idx = {}
    for i, num in enumerate(nums):
        num_idx[num] = i

    # Search an index using a key target - num
    for i, num in enumerate(nums):
        if target - num in num_idx and i != num_idx[target - num]:
            return [i, num_idx[target - num]]
    return None

if __name__ == "__main__":

    nums_ex = [2, 5, 11, 15]
    TARGET = 9
    start = time.time()
    two_sum_ver1(nums_ex, TARGET)
    print(f"Try & Except: {time.time() - start:0.9f}")

    nums_ex = [2, 5, 11, 15]
    TARGET = 9
    start = time.time()
    two_sum_ver2(nums_ex, TARGET)
    print(f"Dictionary: {time.time() - start:0.9f}")
