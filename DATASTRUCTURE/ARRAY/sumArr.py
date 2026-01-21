def sumOfArr(arr):
    sum=0
    for i in arr:
        sum += i
    return sum
arr=[2,4,5,6]
print(sumOfArr(arr))

'''
java code:
class Solution {
  public int sum(int arr[], int n) {

    int sum = 0;
    for (int i : arr) {
      sum += i;
    }
    return sum;
  }
}
'''