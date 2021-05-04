"""Reverse a list without return"""

import time

def reverse_string_ver1(string: list) -> None:
    "Use two pointers."
    left = 0
    right = len(string) - 1
    while left < right:
        string[left] = string[right]
        string[right] = string[left]
        left += 1
        right -= 1

def reverse_string_ver2(string: list) -> None:
    "Use python reverse function."
    string.reverse()

if __name__ == "__main__":

    string_ex = ["h", "e", "l", "l", "o"]
    start = time.time()
    reverse_string_ver1(string_ex)
    runtime = time.time() - start
    print(f"Runtime of Two pointer version: {runtime:0.9f}")

    string_ex = ["h", "e", "l", "l", "o"]
    start = time.time()
    reverse_string_ver2(string_ex)
    runtime = time.time() - start
    print(f"Runtime of reverse function version: {runtime:0.9f}")
