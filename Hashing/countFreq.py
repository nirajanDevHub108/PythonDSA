arr=[6,5,4,3,4,5,6,6]
hashTable=[0]*10
for num in arr:
    hashTable[num] +=1

print(hashTable[6])

'''
java code:
public class Main
{
	public static void main(String[] args) {
	    int[] arr= {5,6,7,8,6,7,8,6};
	    int[] hashTable = new int[10];
	    for(int num: arr){
	        hashTable[num]++;
	       
	    }
		System.out.println(hashTable[6]);
	}
}
'''