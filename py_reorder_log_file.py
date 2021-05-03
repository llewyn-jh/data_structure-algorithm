"""LeetCode, 937
1. The first word in log is the identifier.
2. The letter logs come before all digit logs.
3. The letter-logs are sorted lexicographically by their contents.
If their contents are the same, then sort them lexicographically by their identifiers.
4. The digit-logs maintain their relative ordering."""

def reorder_log_file(logs: list) -> list:
    """Reorder a list of logs"""
    digits = []
    letters = []

    # Classifiy digits and letters.
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # Sort the letters
    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))

    return letters + digits

if __name__ == "__main__":
    input1 = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dog",
        "let3 art zero"
        ]

    reorder_log_file(input1)
