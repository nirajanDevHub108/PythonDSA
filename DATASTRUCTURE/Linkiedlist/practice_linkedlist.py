class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# head=Node(10)#first node head

# #linking to next node
# head.next=Node(20)

# #link the third node
# head.next.next=Node(30)
# #link 4th node
# head.next.next.next=Node(40)

# temp=head
# while temp is not None:
#     print(temp.data,end=" ")
#     temp=temp.next
# print()

#array to node
def arr_to_linklist(arr):
    if not arr:
        return None
    #taking 1st elemnt as head value
    head=Node(arr[0])
    current=head #step 2

    for val in arr[1:]:
        current.next=Node(val)
        current=current.next
    return head

def deltll(head):
    if head is None:
        return None
    temp=head
    head=head.next
    del temp
    return head
def delt_tail_ll(head):
    if head is None or head.next is None:
        return None
    temp=head
    while(temp.next.next != None):
        temp=temp.next
    temp.next=None
    del temp
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
def length_of_ll(head):
    count=0
    temp=head
    while temp:
        temp=temp.next
        count+=1

    return count
def  removeK(head,k):
    if head is None : return head
    if k == 1:
        temp=head
        head=head.next
        del temp
        return head
    #for k elemnt we will count the ref to check with k
    count=0
    temp=head
    prev = None
    while temp is not None:
        count+=1
        if(count == k):
            prev.next=prev.next.next
            break
        prev=temp
        temp=temp.next
    return head

def deleteNodeWithValueX(head, X):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head

        if head.data == X:
            head = head.next
            return head

        prev = None
        temp = head

        while temp is not None:
            if temp.data == X:
                prev.next = temp.next
                return head
            prev = temp
            temp = temp.next
        return head


arr = [1, 2, 3, 4,5,6,7,8]
k=3
X=5
head = arr_to_linklist(arr)
print_list(head)
len=length_of_ll(head)
print("length of ll :",len)

head=deltll(head)
print("List after deleting head: ", end="")
print_list(head)

head=delt_tail_ll(head)
print("List after deleting head: ", end="")
print_list(head)

head=removeK(head,k)
print("List after deleting kth value: ", end="")
print_list(head)

head=removeK(head,X)
print("List after deleting k elemnt: ", end="")
print_list(head)