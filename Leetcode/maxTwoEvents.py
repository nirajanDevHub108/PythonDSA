'''You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

'''
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