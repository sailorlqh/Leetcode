class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        max_count = 0
        max_num = None
        for i in range(len(nums)):
            if(nums[i] not in a.keys()):
                a[nums[i]] = 1
            else:
                a[nums[i]] += 1
            if(a[nums[i]] >= max_count):
                max_count = a[nums[i]]
                max_num = nums[i]
        return max_num
            
        