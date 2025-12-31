'''You are given the head of a singly linked list of positive integers. You have to check if the given linked list is palindrome or not.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # 1️⃣ Find middle using slow & fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3️⃣ Compare both halves
        left = head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

def create_linked_list(arr):
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# MAIN
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1]   # Try [1,2,2,1] also
    head = create_linked_list(arr)

    print("Linked List:")
    print_list(head)

    sol = Solution()
    result = sol.isPalindrome(head)
    print("Is Palindrome:", result)