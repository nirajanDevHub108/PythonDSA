'''Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to calculate their comparison points by comparing each category:

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.'''
def compareTriplets(a, b):
    # Write your code here
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i] >b[i]:
            alice+= 1
        elif a[i]<b[i]:
            bob+=1
    return [alice,bob]

a = [1, 2, 3]
b = [3, 2, 1]
res=compareTriplets(a,b)
print(res)
            