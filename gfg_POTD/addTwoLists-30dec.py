class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, head1, head2):
        # 1. Extract head1 as a whole integer
        def rev(head):
            prev=None
            curr=head
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        l1=rev(head1)
        l2=rev(head2)
        
        carry=0
        dummy=Node(0)
        curr=dummy
        while l1 or l2 or carry:
            val1=l1.data if l1 else 0
            val2=l2.data if l2 else 0
            total_val=val1+val2+carry
            carry=total_val // 10
            curr.next=Node(total_val %10)
            curr=curr.next
            
            if l1: l1=l1.next
            if l2: l2=l2.next
        return rev(dummy.next)

# --- Helper Functions for Testing ---

# Helper to create linked list from list
def create_linked_list(lst):
    dummy = Node(0)
    cur = dummy
    for num in lst:
        cur.next = Node(num)
        cur = cur.next
    return dummy.next

# Helper to print linked list
def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.data))
        head = head.next
    print(" -> ".join(res))

head1 = create_linked_list([1,2,3])
head2 = create_linked_list([9,9,9])
sol=Solution()
result = sol.addTwoLists(head1, head2)
print_linked_list(result)  # Output: 1 -> 1 -> 2 -> 2
