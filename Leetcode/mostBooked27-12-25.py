import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort()

        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        busy_rooms = []  # (end_time, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have completed meetings
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Assign lowest-numbered free room
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # Delay meeting
                end_time, room = heapq.heappop(busy_rooms)
                new_end = end_time + duration
                heapq.heappush(busy_rooms, (new_end, room))

            count[room] += 1

        # Return room with max meetings (tie → smallest index)
        return count.index(max(count))
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
sol=Solution()
res=sol.mostBooked(n,meetings)
print(res)