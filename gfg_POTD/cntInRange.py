from bisect import bisect_left, bisect_right
'''def cntInRange(arr, queries):
    arr.sort()
    res=[]
    for a,b in queries:
        left=bisect_left(arr,a)
        right=bisect_right(arr,b)
        res.append(right-left)
    return res 
    optimal approach '''
def cntInRange(arr, queries):
    arr.sort()
    res=[]
    for a,b in queries:
        count=0
        for num in arr:
            if a <= num <=b:
                count+=1
        res.append(count)
    return res

arr=[1, 4, 2, 8, 5] 
queries= [[1, 4], [3, 6], [0, 10]]
res=cntInRange(arr,queries)
print(res)