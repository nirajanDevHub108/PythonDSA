from collections import deque

def rearrangeQueue(q):
    n = len(q)
    firstHalf = deque()
    secondHalf = deque()

    # Split the queue into two halves
    for i in range(n // 2):
        firstHalf.append(q.popleft())

    # Move the remaining elements to the second half
    while q:
        secondHalf.append(q.popleft())

    # Interleave the elements from both halves
    while firstHalf and secondHalf:
        q.append(firstHalf.popleft())
        q.append(secondHalf.popleft())

if __name__ == "__main__":
    q = deque()
    q.append(2)
    q.append(4)
    q.append(3)
    q.append(1)
    
    rearrangeQueue(q)
    
    while q:
        print(q.popleft(), end=" ")
    print()