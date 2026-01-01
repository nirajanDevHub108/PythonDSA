class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to find the fractional node 
# in the linked list
def fractionalNode(head, k):
    if head is None or k<=0: return -1
        
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
    d=(count//k) if count % k == 0 else (count //k)+1
        
    prev=1
    curr=head
    while prev <=count:
        if prev == d:
            return curr.data
        prev+=1
        curr=curr.next
        
    return -1

# A utility function to print a linked list
def printList(node):
    while node is not None:
        print(node.data, end=' ')
        node = node.next
    print()

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(7)
    head.next.next = Node(9)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(5)

    k = 3

    print(fractionalNode(head, k))