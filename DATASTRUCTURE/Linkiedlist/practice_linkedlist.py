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
arr = [1, 2, 3, 4]
head = arr_to_linklist(arr)
print_list(head)
len=length_of_ll(head)
print("length of ll :",len)

head=deltll(head)
print("List after deleting head: ", end="")
print_list(head)
