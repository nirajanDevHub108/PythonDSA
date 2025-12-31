class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def searchInLL(head,key):
    temp=head
    while temp:
        if temp.data==key:
            return True
        temp=temp.next
    return False


if __name__ == "__main__":

    # create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # key to search in the linked list
    key = 5

    if searchInLL(head, key):
        print("true")
    else:
        print("false")