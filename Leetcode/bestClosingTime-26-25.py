def bestClosingTime( customers):
    n=len(customers)
    penalty=customers.count('Y')
    min_penalty=penalty
    bst_hour=0

    for hour in range(n):
        if (customers[hour] == 'Y'):
            penalty -=1
        else:
            penalty+=1
        
        if penalty <min_penalty:
            min_penalty=penalty
            bst_hour=hour+1
    return bst_hour

customers = "YNYY"
res=bestClosingTime(customers)
print(res)

