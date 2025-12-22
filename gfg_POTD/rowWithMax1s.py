def rowWithMax1s( arr):
        # code here\maz
        max_count=0
        row_index=-1
        
        for i in range(len(arr)):
            count_ones=sum(arr[i])
            if count_ones > max_count:
                max_count=count_ones
                row_index=i
        return row_index

arr=[[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
res=rowWithMax1s(arr)
print(res)