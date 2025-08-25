#find pair with target sum using two pointer left and right 


'''
given a sorted array and target value , find if there exist any pair whose sum is equal to target
time complexity =O (n)

two pointer left start at 0 and right start and last index and left will move forward one step if target not found
def find_pair_with_sum(arr, target):
    left , right = 0 , len(arr)-1
    while left < right:
        total = arr[left] +arr[right]
        if total == target:
            return (arr[left], arr[right])
        elif total < target:
            left +=1
        else:
            right -= 1
    return []

print(find_pair_with_sum([1,3,2,2,4,5,7], 6))
'''

def find_pair_with_sum(arr, target):
    left , right = 0 , len(arr)-1
    arr.sort()
    resultList =[]
    while left < right:
        total = arr[left] +arr[right]
        if total == target:
            resultList.append((arr[left], arr[right]))

            while left < right and arr[left] == arr[left +1]:
                left +=1
            while left < right and arr[right] == arr[right - 1]:
                right -=1
            left +=1
            right -= 1
        
        elif total < target:
            left +=1
        else:
            right -= 1
    return resultList

print(find_pair_with_sum([1,3,2,2,4,5,7], 6))