'''Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.
Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers.
'''
arr =[9, 4, -2, -1, 5, 0, -5, -3, 2]

pos_num =[]
neg_num =[]

for x in arr:
    if x >= 0:
        pos_num.append(x)
    else :
        neg_num.append(x)
result=[]
i,j = 0,0
while i<len(pos_num) and j < len(neg_num):
    result.append(pos_num[i])
    result.append(neg_num[j])
    i+=1
    j+=1
while i < len(pos_num):
    result.append(pos_num[i])
    i+=1
while j < len(neg_num):
    result.append(neg_num[j])
    j+=1
    #arr[::] = result[::] assiging each elemet of result list to arr list
print(result)
