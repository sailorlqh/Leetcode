class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonZeroPointer = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != 0)
                continue;
            nonZeroPointer = i + 1;
            while(nonZeroPointer < nums.size() && nums[nonZeroPointer] == 0) {
                nonZeroPointer++;
            }
            if(nonZeroPointer >= nums.size()) {
                break;
            }
            int temp = nums[nonZeroPointer];
            nums[nonZeroPointer] = nums[i];
            nums[i] = temp;
            // for(int j = 0; j < nums.size(); j++) {
                // cout<<nums[i]<<" ";
            // }
            // cout << endl;
        }
    }
};