class Solution {
    public void moveZeroes(int[] nums) {
        int ptr = 0;
        int nonZeroPtr = 0;
        for(ptr = 0; ptr < nums.length; ptr++) {
            if(nums[ptr] != 0){
                continue;
            }
            nonZeroPtr = ptr + 1;
            while(nonZeroPtr < nums.length && nums[nonZeroPtr] == 0){
                nonZeroPtr += 1;
            }
            if(nonZeroPtr >= nums.length){
                break;
            }
            int temp = nums[nonZeroPtr];
            nums[nonZeroPtr] = nums[ptr];
            nums[ptr] = temp;
        }
    }
}