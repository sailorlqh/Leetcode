import java.util.Collections; 
import java.util.Arrays; 
class Solution {
    public int rob(int[] nums) {
        if(nums.length <= 1) return nums.length == 0 ? 0 : nums[0];
        return Math.max(helper(nums, 0, nums.length-1), helper(nums, 1, nums.length));
    }
    
    public int helper(int[] nums, int left, int right) {
        int even = 0;
        int odd = 0;
        for(int i = left; i <right; i++) {
            if(i % 2 == 0) {
                even = Math.max(even + nums[i], odd);
            } else {
                odd = Math.max(odd + nums[i], even);
            }
        }
        return Math.max(even, odd);
    }
}