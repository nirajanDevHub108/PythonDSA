'''
Given a linked list containing n head nodes where every node in the linked list contains two pointers:
(i) next points to the next node in the list.
(ii) bottom points to a sub-linked list where the current node is the head.
Each of the sub-linked lists nodes and the head nodes are sorted in ascending order based on their data. Flatten the linked list such that all the nodes appear in a single level while maintaining the sorted order.

Note:
1. ↓ represents the bottom pointer and → represents the next pointer.
2. The flattened list will be printed using the bottom pointer instead of the next pointer.
'''


from heapq import heappush,heappop
class Node:
    def __init__(self,data):
        self.data=data
        self.next=self.bottom=None

#function to push to the begining of the ll
def push(head,data):
    newNode=Node(data)
    newNode.bottom=head # Make next of newNode as head
    head=newNode # Move the head to point to newNode

    return head
def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.bottom is not None:
            print(" -> ", end="")
        node = node.bottom
    print()


# Class to compare two node objects
class Cmp:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data

def flatten(root):
    pq=[]
    head=None
    tail=None

    while root:
        heappush(pq,Cmp(root))
        root=root.next
    # Extracting the minimum node while the priority 
    # queue is not empty
    while pq:
        minNode=heappop(pq).node
        if head is None:
            head=minNode
            tail=minNode
        else:
            tail.bottom=minNode
            tail=tail.bottom

        if minNode.bottom:
            heappush(pq,Cmp(minNode.bottom))
            minNode.bottom=None
    return head

if __name__ == '__main__':
    head = Node(5)
    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next = Node(10)
    head.next.bottom = Node(20)

    head.next.next = Node(19)
    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next = Node(28)

    head = flatten(head)

    printList(head)