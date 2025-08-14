#find pair with target sum using two pointer left and right 


'''
given a sorted array and target value , find if there exist any pair whose sum is equal to target
time complexity =O (n)

two pointer left start at 0 and right start and last index and left will move forward one step if target not found
'''

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
    return None

print(find_pair_with_sum([1,2,3,4,6], 6))