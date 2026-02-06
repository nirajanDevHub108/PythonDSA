def happiest_triplet(a, b, c):
    # Step 1: sort all arrays
    a.sort()
    b.sort()
    c.sort()

    i = j = k = 0
    n = len(a)

    best_diff = float('inf')
    best_sum = float('inf')
    best_triplet = None

    # Step 2: three-pointer traversal
    while i < n and j < n and k < n:
        x, y, z = a[i], b[j], c[k]

        current_max = max(x, y, z)
        current_min = min(x, y, z)
        diff = current_max - current_min
        total = x + y + z

        # Step 3: update best triplet
        if diff < best_diff or (diff == best_diff and total < best_sum):
            best_diff = diff
            best_sum = total
            best_triplet = [x, y, z]

        # Step 4: move pointer of minimum element
        if current_min == x:
            i += 1
        elif current_min == y:
            j += 1
        else:
            k += 1

    # Step 5: print in decreasing order
    best_triplet.sort(reverse=True)
    return best_triplet

a = [1, 4, 10]
b = [2, 15, 20]
c = [10, 12, 5]

print(happiest_triplet(a, b, c))