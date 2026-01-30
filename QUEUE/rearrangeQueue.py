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
    
'''
java code:

import java.util.LinkedList;
import java.util.Queue;

class GfG {
    public static void rearrangeQueue(Queue<Integer> q) {
        int n = q.size();
        Queue<Integer> firstHalf = new LinkedList<>();
        Queue<Integer> secondHalf = new LinkedList<>();

        // Split the queue into two halves
        for (int i = 0; i < n / 2; i++) {
            firstHalf.add(q.peek());
            q.remove();
        }

        // Move the remaining elements to the second half
        while (!q.isEmpty()) {
            secondHalf.add(q.peek());
            q.remove();
        }

        // Interleave the elements from both halves
        while (!firstHalf.isEmpty() && !secondHalf.isEmpty()) {
            q.add(firstHalf.peek());
            firstHalf.remove();
            q.add(secondHalf.peek());
            secondHalf.remove();
        }
    }

    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        q.add(2);
        q.add(4);
        q.add(3);
        q.add(1);

        rearrangeQueue(q);

        while (!q.isEmpty()) {
            System.out.print(q.peek() + " ");
            q.remove();
        }
    }
}
'''