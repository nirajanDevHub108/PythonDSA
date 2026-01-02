# find max uisng range value
arr=[1,2,3]
max_val=0
for i in range(len(arr)):#iterating 0 to n-1 0,1,2,3,4=5 elemnts
    if max_val < arr[i]:
        max_val=arr[i]
print(max_val)

#for each loop is useful when index is not requried like freq count,sum,validation

total=0
for num in arr:
    total+=num
print("total of al number is :",total)

#loop with range value but with jumping logic range(start,end,step)
#wehn to use skiping elemnt,even/odd index,arthemetic progression ect

#reverseing using jumping loging
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=' ')
print()

#find all even indices element from an array
for i in range(0,len(arr),2):
    print(arr[i],end='')
print()

print("----------------------------")

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print(arr[i],arr[j])
print("----------------------------")

#loop with break satatement
target=2
for num in arr:
    if num == target:
        print(target," :found")
        break
print("----------------------------")
#loop with continue satatement-skip the condition ignore unwanted elements
arr1=[1,-2,3,-4]
for num in arr1:
    if num<0:
        continue
    print(num)

print("----------------------------")

#Two pointer loop (while>for) when pointer move dynamically
left,right=0,len(arr1)-1

while (left <right):
    print(arr1[left],arr1[right])
    left+=1
    right-=1

#Hashing in array used by creating a dict 
arr2=[1,2,3,4,2,3]
freq={}
for num in arr2:
    freq[num]=freq.get(num,0)+1
print(freq)

#loop +sliding window technique

def isSorted(arr) -> bool:
        # code here
        res=arr[0]
        
        for i in range(len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True

arr= [90, 80, 100, 70, 40, 30]
print(isSorted(arr))