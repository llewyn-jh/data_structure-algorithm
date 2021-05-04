"""Group anagrams"""

import collections
import time

def group_anagrams_ver1(strs: list) -> list:
    """Mine solution
    this is slower than the ver2 because the ver1 has one more for loop iteration."""
    anagrams = []
    for i, word in enumerate(strs):
        if i == 0:
            anagrams.append([word])
        else:
            exist = False
            # Compare a word and the first element in anagram.
            for anagram in anagrams:
                chars = [char for char in word if char in anagram[0]]
                # Add a word to a anagram when have same letters and length
                if len(chars) == len(anagram[0]):
                    anagram.append(word)
                    exist = True
                else:
                    continue

            # Add new anagram when a word can not belong to any anagram.
            if exist == False:
                anagrams.append([word])

    return anagrams

def group_anagrams_ver2(strs: list) -> list:
    """Standard solution"""
    # Create a dictionary which has an empty list value as a default.
    anagrams = collections.defaultdict(list)

    # After sorting a word, append the word to a dictionary's value.
    for word in strs:
        anagrams["".join(sorted(word))].append(word)

    return anagrams.values()

if __name__ == "__main__":

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    start = time.time()
    group_anagrams_ver1(words)
    print(time.time() - start)

    start = time.time()
    group_anagrams_ver2(words)
    print(time.time() - start)
