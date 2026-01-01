'''
You are given the heads of two non-empty singly linked lists, head1 and head2, that intersect at a certain point. Return that Node where these two linked lists intersect.

Note: It is guaranteed that the intersected node always exists.

In the custom input you have to give input for CommonList which pointed at the end of both head1 and head2 to form a Y-shaped linked list.

Input: head1: 10 -> 15 -> 30, head2: 3 -> 6 -> 9 -> 15 -> 30
Output: 15
Explanation: From the above image, it is clearly seen that the common part is 15 -> 30, whose starting point is 15.
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def intersectPoint(head1, head2):
        # code here
        pointer1=head1
        pointer2=head2
        
        while pointer1 !=pointer2:
            pointer1=pointer1.next if pointer1 else head2
            pointer2=pointer2.next if pointer2 else head1
        
        return pointer1
# Common part
common = ListNode(15)
common.next = ListNode(30)

# head1: 10 → 15 → 30
head1 = ListNode(10)
head1.next = common

# head2: 3 → 6 → 9 → 15 → 30
head2 = ListNode(3)
head2.next = ListNode(6)
head2.next.next = ListNode(9)
head2.next.next.next = common

result =intersectPoint(head1, head2)
print(result.val)  # Output: 15
