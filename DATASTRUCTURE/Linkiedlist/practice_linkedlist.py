class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)#first node head

#linking to next node
head.next=Node(20)

#link the third node
head.next.next=Node(30)
#link 4th node
head.next.next.next=Node(40)

temp=head
while temp is not None:
    print(temp.data,end=" ")
    temp=temp.next
print()


