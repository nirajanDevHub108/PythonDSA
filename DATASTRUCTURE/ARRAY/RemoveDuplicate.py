#Remove Duplicates Sorted Array
'''You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
Examples :'''

arr = [2, 2, 2, 2, 2]
n = len(arr)
res =[]
for i in range (n):
    if len(res) == 0 or res[-1] != arr[i]:
        res.append(arr[i])
        
print(res)



