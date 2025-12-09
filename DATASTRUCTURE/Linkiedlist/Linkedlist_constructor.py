class Node :
    def __init__ (self ,value):
        self.value=value
        self.next=None


class LinkiedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail =new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value ,end =" ")
            temp = temp.next
        print()
    def make_empty(self):
        self.head=None
        self.tail =None
        self.length=0

    def append(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1


#print(my_linked_list.head.value)






