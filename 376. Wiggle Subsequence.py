class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        if(length < 2):
            return length
        up = 1
        down = 1
        for i in range(1, length):
            if(nums[i] > nums[i-1]):
                up = down + 1
            elif(nums[i] < nums[i-1]):
                down = up + 1
        return max(up, down)
        