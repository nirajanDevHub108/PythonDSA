'''n=4
for i in range (1,n+1):
    for j in range(i):
        print(chr(65+ n +j -i),end=" ")
    print()
'''
t=int(input())

while t>0:
    x=int(input())
    t-=1

# up x down x x+x=2x
    total_distance=(2*x)* 5
    print(total_distance)