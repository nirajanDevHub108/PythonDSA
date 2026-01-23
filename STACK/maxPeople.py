def previousGreater(arr):
    n = len(arr)
    prev = [-1] * n  
    st = []

    for i in range(n):
        while st and arr[st[-1]] < arr[i]:
            st.pop()
        if st:
            prev[i] = st[-1]
        st.append(i)

    return prev


def nextGreater(arr):
    n = len(arr)
    next_ = [n] * n  
    st = []

    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] < arr[i]:
            st.pop()
        if st:
            next_[i] = st[-1]
        st.append(i)

    return next_


def maxPeople(arr):
    n = len(arr)

    # Compute Previous Greater and Next Greater
    prev = previousGreater(arr)
    next_ = nextGreater(arr)

    maxCount = 0

    for i in range(n):
        leftBound = 0 if prev[i] == -1 else prev[i] + 1
        rightBound = n - 1 if next_[i] == n else next_[i] - 1

        # Range size gives how many people visible including self
        count = rightBound - leftBound + 1

        maxCount = max(maxCount, count)

    return maxCount

if __name__ == "__main__":
    arr = [6, 2, 5, 4, 5, 1, 6]
    print(maxPeople(arr))