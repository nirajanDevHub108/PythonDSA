def sum_till_n(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2


# ---- Simple Tests ----
assert sum_till_n(0) == 0
assert sum_till_n(1) == 1
assert sum_till_n(5) == 15
assert sum_till_n(100) == 5050
assert sum_till_n(2)== 3

print("All test cases passed ✅")