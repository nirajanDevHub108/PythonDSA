def minimumDeletions(s: str) -> int:
    b_count = 0      # number of 'b's seen so far
    deletions = 0    # minimum deletions needed

    for ch in s:
        if ch == 'b':
            b_count += 1
        else:  # ch == 'a'
            # Either delete this 'a' (deletions + 1)
            # or delete all previous 'b's (b_count)
            deletions = min(deletions + 1, b_count)

    return deletions
s = "aababbab"
print(minimumDeletions(s))