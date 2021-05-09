"""Product except self, leetcode 238"""

import time

def product_except_self(nums: list) -> list():
    """Have to solve a problem within O(n)
    Do not use the divide operation"""
    result = []
    # Calculate the left side
    prod = 1
    for num in nums:
        result.append(prod)
        prod = prod * num
    # Calculate the right side product the left and right
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * prod
        prod = prod * nums[i]
    return result

if __name__ == "__main__":

    ex = [1, 2, 3, 4]
    start = time.time()
    product_except_self(ex)
    print(f"Runtime: {time.time() - start:0.9f}")
