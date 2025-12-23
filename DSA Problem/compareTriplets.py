def compareTriplets(a, b):
    # Write your code here
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i] >b[i]:
            alice+= 1
        elif a[i]<b[i]:
            bob+=1
    return [alice,bob]

a = [1, 2, 3]
b = [3, 2, 1]
res=compareTriplets(a,b)
print(res)
            