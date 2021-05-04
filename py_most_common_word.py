"""Most common word"""

import re
import collections

def most_common_word(paragraph: str, banned: list) -> str:
    """Return most common word except for banned words"""

    words = [word for word in re.sub(r"[^\w]", " ", paragraph)
    .lower()
    .split() if word not in banned]

    counts = collections.Counter(words)
    return sorted(counts.items(), key=lambda x : x[1], reverse=True)[0][0]

if __name__ == "__main__":
    PARAGRAPH_EX = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned_ex = ["hit"]
    print(most_common_word(PARAGRAPH_EX, banned_ex))
