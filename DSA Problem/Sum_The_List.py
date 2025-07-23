def listsSum(arr):
    # code here
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# Example usage
try:
    # Taking space-separated integers as input
    user_input = input()
    arr = list(map(int, user_input.strip().split()))
    result = listsSum(arr)
    print(result)
except ValueError:
    print("❌ Invalid input. Please enter only space-separated numbers.")