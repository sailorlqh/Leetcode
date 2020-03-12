class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(curr,remain):
            if curr==halfSum:
                return True

            for i in range(len(remain)-1,-1,-1):
                if curr+remain[i]>halfSum:
                    return False
                if dfs(curr+remain[i],remain[:i]+remain[i+1:]):
                    return True
            return False
        sumNum=sum(nums)
        if sumNum %2 != 0 or len(nums)<2:
            return False
        nums = sorted(nums)
        halfSum = sumNum // 2
        return dfs(0,nums)