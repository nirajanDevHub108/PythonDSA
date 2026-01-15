import math
def isArmstrong(n):
    org =n
    sumOfPow=0
    count=0
    temp = n
    while temp > 0:
        count +=1
        temp=temp//10
    temp = n
    while temp > 0:
        rem= temp % 10
        sumOfPow += rem ** count
        temp=temp//10
        
    return sumOfPow == org
n=153
print(isArmstrong(n))