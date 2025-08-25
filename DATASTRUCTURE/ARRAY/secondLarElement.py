'''Second Largest Element
Find the second largest element in the array. If it doesn’t exist (array size < 2), return -1.
👉 Similar to largest element, but you must handle duplicates carefully.'''
arr=[3,2,4,5,6]

def secondLargElement(arr):
    LargElement = arr[0]
    second_largest = float("-inf")
    if len(arr)<2:
        return -1
    for i in range( 1, len(arr)):
        if arr[i] > LargElement:
            second_largest=LargElement
            LargElement =arr[i]
        elif arr[i] > second_largest and arr[i] != LargElement:
            second_largest=arr[i]
    return second_largest

print(secondLargElement(arr))