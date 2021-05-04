"""Check the Palindrome"""

import re
import time
import collections

def is_palindrome_match(string: str) -> bool:
    """Use the match method of regular expression and slicing"""
    string = string.lower()
    string = [char.lower() for char in string if re.match('[a-zA-Z]|[0-9]', char)]
    return string[::-1] == string

def is_palindrome_sub(string: str) -> bool:
    """User the sub method of regular expression and slicing"""
    string = string.lower()
    string = re.sub('[^a-z0-9]', '', string)
    return string[::-1] == string

def is_palindrome_isalnum(string: int) -> bool:
    """Use the isalnum function and slicing"""
    string = string.lower()
    string = [char for char in string if char.isalnum()]
    return string[::-1] == string

def is_palindrome_no_slicing(string: str) -> bool:
    """Use python while loop"""
    string = [char.lower() for char in string if char.isalnum()]

    while len(string) > 1:
        if string.pop(0) != string.pop():
            return False
    return True

def is_palindrome_deque_no_slicing(string: str) -> bool:
    """Use python while loop and deque"""
    string: Deque = collections.deque()
    string = [char.lower() for char in string if char.isalnum()]

    while len(string) > 1:
        if string.pop(0) != string.pop():
            return False
    return True

if __name__ == "__main__":

    EXAMPLE = "A man, a plan, a canal: Panama"

    start = time.time()
    is_palindrome_match(EXAMPLE)
    runtime = time.time() - start
    print(f"Runtime with re match method: {runtime:0.8f}")

    start = time.time()
    is_palindrome_sub(EXAMPLE)
    runtime = time.time() - start
    print(f"Runtime with re sub method: {runtime:0.8f}")

    start = time.time()
    is_palindrome_isalnum(EXAMPLE)
    runtime = time.time() - start
    print(f"Runtime with isalnum: {runtime:0.8f}")

    start = time.time()
    is_palindrome_no_slicing(EXAMPLE)
    runtime = time.time() - start
    print(f"Runtime without slicing: {runtime:0.8f}")

    start = time.time()
    is_palindrome_deque_no_slicing(EXAMPLE)
    runtime = time.time() - start
    print(f"Runtime with deque: {runtime:0.8f}")
