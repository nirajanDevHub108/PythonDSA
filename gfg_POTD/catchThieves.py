def catchThieves(arr, k):
    police=[]
    theif=[]
    for i in range(len(arr)):
        if arr[i] == 'P':
            police.append(i)
        else:
            theif.append(i)
    i=j= 0
    caught=0
    while i < len(police) and j < len(theif):
        if abs(police[i]-theif[j]) <=k:
            caught+=1
            i+=1
            j+=1
        elif police[i] < theif[j]:
            i+=1
        else:
            j+=1
    return caught
arr=['T', 'T', 'P', 'P', 'T', 'P'] 
k = 2
print(catchThieves(arr,k))