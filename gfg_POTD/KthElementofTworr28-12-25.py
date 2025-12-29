'''brute force solution
res=a+b
res.sort()
return res[k-1]
but time will more when the arr size increases
tc=O(a+b log n)

'''
def kthElement(a, b, k):
    # ensure a is smaller array
    if len(a) > len(b):
        return kthElement(b, a, k)

    n, m = len(a), len(b)

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        i = (low + high) // 2
        j = k - i

        leftA = a[i-1] if i > 0 else float('-inf')
        rightA = a[i] if i < n else float('inf')

        leftB = b[j-1] if j > 0 else float('-inf')
        rightB = b[j] if j < m else float('inf')

        if leftA <= rightB and leftB <= rightA:
            return max(leftA, leftB)

        elif leftA > rightB:
            high = i - 1
        else:
            low = i + 1

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

print(kthElement(a, b, k))
