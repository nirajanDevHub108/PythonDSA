'''def hello_world():
    print("hello world")
hello_world()

#with argument ,parameters in function 
def sum(num1,num2):
    print(num1+num2)

sum(2,5)
sum(1,7)
sum(100,200)
#taking multiple arguments
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("dave","akhil","chotu")

#multinamed items 
def multiple_named_items(**kargs):
    print(kargs)
    print(type(kargs))

multiple_named_items(First="dave",Last="akhil")'''
'''
You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.


XOR operation
Key properties of XOR:

x ^ x = 0

x ^ 0 = x

XOR is commutative & associative

So if:

You XOR all numbers from 1 to n

And XOR all elements of the array

All matching numbers cancel out

The remaining value is the missing number
n = len(arr) + 1

    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    xor_arr = 0
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr
'''
def missingNum( arr):
        # code here
        n=len(arr)+1
        total_sum=n*(n+1)//2
        arr_sum=0
        for i in arr:
            arr_sum+=i
        
        res=total_sum-arr_sum

        return res

arr=[2, 6, 5, 1, 3]
res=missingNum(arr)
print(res)