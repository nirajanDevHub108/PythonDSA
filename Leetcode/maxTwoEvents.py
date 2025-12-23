def maxTwoEvents(events):
    events.sort()
    max_sum=0
    n=len(events)
    # suffixMax[i] = max value from i to end
    suffixMax=[0]*n
    suffixMax[-1] = events[-1][2]
    for i in range(n-2,-1,-1):
        suffixMax[i]=max(suffixMax[i + 1], events[i][2])
    import bisect

    ans = 0
    starts = [event[0] for event in events]

    for i in range(n):
        start, end, value = events[i]

            # Take only this event
        ans = max(ans, value)

            # Find next event with start >= end + 1
        j = bisect.bisect_left(starts, end + 1)

        if j < n:
            ans = max(ans, value + suffixMax[j])

    return ans

events=[[1,3,2],[4,5,2],[2,4,3]]
res=maxTwoEvents(events)
print(res)