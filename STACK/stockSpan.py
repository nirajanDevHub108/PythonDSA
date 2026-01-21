def removeKdig( arr):
        # code here
        n=len(arr)
        span=[0]*n
        st=[]
         
        for i in range(n):
            while st and arr[st[-1]] <=arr[i]:
                st.pop()
            
            if not st:
                span[i] = (i+1)
            else:
                span[i]=(i-st[-1])
            st.append(i)
        return span

arr = [10, 4, 5, 90, 120, 80]
result = removeKdig(arr)
print(result)