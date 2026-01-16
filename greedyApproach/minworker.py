
'''
You are given an array arr[], where arr[i] denotes the range of working hours a person at position i can cover.

If arr[i] ≠ -1, the person at index i can work and cover the time interval [i - arr[i], i + arr[i]].
If arr[i] = -1, the person is unavailable and cannot cover any time.
The task is to find the minimum number of people required to cover the entire working day from 0 to n - 1. If it is not possible to fully cover the day, return -1.


'''
def minWroker(arr):
    n=len(arr)
    intervals=[]
    for i in range(n):
        if arr[i] != -1:
            start = max(0, i - arr[i])
            end   = min(n-1, i + arr[i])
            intervals.append((start,end))
    intervals.sort()
    people_count=0
    current_end=-1
    i = 0
    while current_end < n-1:
        max_reach=current_end
        
        while i < len(intervals) and intervals[i][0] <=current_end+1:
            max_reach = max(max_reach , intervals[i][1])
            i+=1 
        if max_reach == current_end:
            return -1
        people_count +=1
        current_end = max_reach 
        
    return people_count
    
  
arr=[-1 ,2 ,2 ,-1, 0 ,0]
print(minWroker(arr))