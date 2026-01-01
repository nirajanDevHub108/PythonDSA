def isLengthEven(self, head):
        # Code here
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        if count % 2==0:
            return True
        return False