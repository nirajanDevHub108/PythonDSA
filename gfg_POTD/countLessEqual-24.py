'''      Brute force solution is having O(n) Tc we need to optimize it using binary search implemented array i O(logn) Tc 
        count=0
        for num in arr:
            if num <= x:
                count+=1
        return count

        '''
def countLessEqual(arr, x):


arr=[6, 10, 12, 15, 2, 4, 5]
x = 14
res=countLessEqual(arr,x)
print(res)