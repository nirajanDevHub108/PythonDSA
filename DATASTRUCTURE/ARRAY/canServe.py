def canServe( arr):
        # code here 
        count_five=0
        count_ten=0
        for num in arr:
            if num == 5:
                count_five +=1
            elif num == 10:
                if count_five == 0:
                    return False
                count_five -= 1
                count_ten +=1
            else:
                if count_ten > 0 and count_five > 0:
                    count_five -=1
                    count_ten -=1
                elif count_five >= 3:
                    count_five -=3
                else:
                    return False
        return True
    
arr=[5, 5, 10, 10, 20]
print(canServe(arr))