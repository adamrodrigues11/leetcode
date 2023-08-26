// My initial solution using O(n) space and O(n) time - note that the loops are not actually nested as smallest can only be bumped up in the worst case to
// the length of the nums array, which is n
public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int smallest = 1;
        HashSet<int> observed = new HashSet<int>();
        for ( int i = 0; i < nums.Length; i++ ) {
            if ( nums[i] > 0 ) {
                observed.Add(nums[i]);
            }
            while ( observed.Contains(smallest) ) {
                smallest++;
            }
        }
        return smallest;
    }
}


// Best solution as it uses O(1) space and O(n) time
public class Solution {
    public int FirstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.Length; i++ ) {
            while ( nums[i] > 0 && nums[i] <= nums.Length && nums[i] != nums[nums[i] - 1] ) {
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }
        for (int i = 0; i < nums.Length; i++ ) {
            if ( nums[i] != i + 1 ) return i + 1;
        }
        return nums.Length + 1;
    }
}