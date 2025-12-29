def pyramid_possible(bottom, allowed):
    from collections import defaultdict
    allowed_map = defaultdict(list)
    for a, b, c in allowed:
        allowed_map[(a, b)].append(c)

    memo = set()  # stores rows that are impossible

    def can_build(row):
            # If we already know this row fails
        if row in memo:
            return False

            # Base case
        if len(row) == 1:
            return True

        def dfs(next_row, idx):
            if idx == len(row) - 1:
                return can_build(next_row)

            pair = (row[idx], row[idx + 1])
            if pair not in allowed_map:
                return False

            for ch in allowed_map[pair]:
                if dfs(next_row + ch, idx + 1):
                    return True
            return False

        possible = dfs("", 0)
        if not possible:
            memo.add(row)  # cache failure
        return possible

    return can_build(bottom)
bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]
print(pyramid_possible(bottom, allowed))