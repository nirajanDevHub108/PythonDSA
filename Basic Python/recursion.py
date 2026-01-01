# #recursion fuction
# def add_one(num):
#     if (num >= 9):
#         return num+1
#     total=num+1
#     print(total)

#     return add_one(total)
# add_one(0)

def  sum(n):
    if n ==1 : return 1 #base condition
    return n+sum(n-1)
n=5
print(sum(n))