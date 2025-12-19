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