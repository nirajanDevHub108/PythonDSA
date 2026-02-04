def getLastMoment(n, left, right):
    # code here
    res = 0
    for i in range(len(left)):
        res = max(res, left[i])

    for i in range(len(right)):
        res = max(res, n - right[i])

    # Return the maximum time among all ants
    return res
n = 4
left = [2]
right = [0, 1, 3]
print(getLastMoment(n,left,right))