class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        nonZeroPtr = 0
        while(ptr < len(nums)):
            if(nums[ptr] != 0):
                ptr += 1
                continue
            nonZeroPtr = ptr + 1
            while(nonZeroPtr < len(nums) and nums[nonZeroPtr] == 0):
                nonZeroPtr += 1
            if(nonZeroPtr >= len(nums)):
                break
            nums[ptr], nums[nonZeroPtr] = nums[nonZeroPtr], nums[ptr]
            ptr += 1
            # print(nums)
                
        