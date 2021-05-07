"""Trapping rain water, leetcode 42, level 3"""

import time

def trap(height: int) -> int:
    """Use two pointers"""

    # The length of height is zero
    if not height:
        return 0

    # Set initial values
    volume = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    # Two pointer
    while left < right:

        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        # Move pointers for getting the heighest value
        if height[left] <= height[right]:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume

if __name__ == "__main__":

    height_ex = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    start = time.time()
    trap(height_ex)
    print(f'Two pointer: {time.time() - start:0.9f}')
