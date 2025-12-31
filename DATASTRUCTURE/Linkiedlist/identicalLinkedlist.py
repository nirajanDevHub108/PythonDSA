# Python program to check if two linked lists
# are identical or not

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Returns true if linked lists head1 and head2 are
# identical, otherwise false
def areIdentical(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.data != head2.data:
            return False
        head1=head1.next
        head2=head2.next
    return head1 is  None and head2 is None
 


if __name__ == "__main__":
    # Create first linked list: 3 -> 2 -> 1
    head1 = Node(3)
    head1.next = Node(2)
    head1.next.next = Node(1)

    # Create second linked list: 3 -> 2 -> 1
    head2 = Node(3)
    head2.next = Node(2)
    head2.next.next = Node(2)

    # Function call
    if areIdentical(head1, head2):
        print("True")
    else:
        print("False")