def removeKdig( s, k):
        # code here
        n=len(s)
        st=[]
         
        for cur in s:
            while st and k > 0 and st[-1] >cur:
                st.pop()
                k-=1
            if  st or cur != '0':
                st.append(cur)
        while(st and k >0):
            st.pop()
            k-=1
        if not st:
            return "0"
        result = ''.join(st)
        return result

s = "765028321"
k = 5
result = removeKdig(s,k)
print(result)

'''
java code
'''