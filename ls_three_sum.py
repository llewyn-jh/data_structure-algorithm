"""Three sum, leetcode 13, level 2"""

import time

def three_sum(nums: list) -> list:
    """Two pointer"""

    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # Skip same value
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Set two pointers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            candidate = nums[i] + nums[left] + nums[right]
            if candidate < 0:
                left += 1
            elif candidate > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip same values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

if __name__ == "__main__":

    ex = [-1, 0, 1, 2, -1, -4]
    start = time.time()
    three_sum(ex)
    print((f"Two pointers: {time.time() - start:0.9f}"))
