n=5
for i in range(1,n+1):
    for j in range(n):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#1
#22
#333
#4444
#55555  
#no of line =n

for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()

# *****
# ****
# ***
# **
# *

#no of line =n pattern -5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print() 

#pattern-6
'''
12345
1234
123
12
1 
line=n
j =n-i+1 to print exact pattern
'''
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end="")
    print()

'''
    *
   ***
  *****
 *******
*********
[4 , 1, 4]
[3 , 3, 3]
[2 , 5, 2]
[1 , 7, 1]
[0 , 9, 0]
 n=5
 space calculation=(n-i-1 )
 i=o 
 5-i-1=4
 i=1
 5-1-1=3
 5-2-1=2
 5-3-1=1
 5-4-1=0

 start caclulation 2*i+1
 j=0
 2*i+1=2*0+1=1
 2*1+1=3
 2*2+1=5
 2*3+1=7
 2*4+1=9
'''
for i in range(n):
    #space printing
    for j in range(n-i-1):
        print(" ",end="")
    
    for j in range(2*i+1):
        print("*",end="")
    print()

print("---------------------")
'''
*********
 *******
  *****
   ***
    *
[0,9,0]
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]

star print(2*n-2*i+1) 
i=0
2*5-i-1=9
i=1
2*5-i-1=
space=i value

    '''
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*n - (2*i+1)):
        print("*",end="")
    # for j in range(i):
    #     print(" ",end="")
    print()
print("--------------------------")

''''''
for i in range(n):
    #space printing
    for j in range(n-i-1):
        print(" ",end="")
    
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*n - (2*i+1)):
        print("*",end="")

    print()
print("-----------------------")

'''
pattern-10
*
**
***
****
*****
****
***
**
*
upper part 
going for n times and printing i value

lower part
going for n time but printing n-i 
for i in range(1, 2 * n):
3	    stars = i if i <= n else 2 * n - i
4	            
5	            # for printing the stars in each row.
6	    for j in range(1, stars + 1):
7	        print("*", end="")
8	    print()
'''
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
print("---------------------") 
'''
pattern-11
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
''' 
start=1
for i in range(n):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(i+1):
        print(start,end="")
        start=1-start
    print()  

#pattern 12

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
# number
space=2*(n-1)
for i in range(1,n+1):

    for j in range(i):
        print(j+1,end="")
    
    for j in range(n-i):
            print(" ", end="")

    for j in range(i):
        print(i-j,end="")
    print()
    space-=2
    # for j in range(1,)
    # print()
    
# 1
# 3 5
# 7 9 11
# 13 15 17 19