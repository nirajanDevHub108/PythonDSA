from collections import defaultdict
def countDistinct(arr,k):
  
    freq = defaultdict(int)
    res=[]

    # 1st block of k
    for i in range(k):
        freq[arr[i]] += 1
    res.append(len(freq))

    #now from index 2 to length or arr
    for i in range(k,len(arr)):
        freq[arr[i]] += 1
        freq[arr[i-k]] -= 1

        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]
        res.append(len(freq))

    return res

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(countDistinct(arr,k))
