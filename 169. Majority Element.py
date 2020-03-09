class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(left_index, right_index):
            if(left_index == right_index):
                return nums[left_index]
            
            mid = (right_index - left_index) // 2 + left_index
            left_majority = helper(left_index, mid)
            right_majority = helper(mid+1, right_index)
            
            if(left_majority == right_majority):
                return left_majority
            left_count = 0
            right_count = 0
            for i in range(left_index, right_index+1):
                if(nums[i] == left_majority):
                    left_count += 1
                if(nums[i] == right_majority):
                    right_count += 1
            return left_majority if left_count > right_count else right_majority
        return helper(0, len(nums)-1)
        