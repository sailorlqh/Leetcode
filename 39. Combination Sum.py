class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(nums, target, res=[], n=[]):
            if target==0:
                n = sorted(n)
                if n not in res:
                    res.append(n)   
                return res            
            
            for i in range(len(nums)):
                temp = nums[i]
                if target - temp >= 0:
                    helper(nums, target-temp, res, n+[temp])
                else:
                    break
            return res    
        
        candidates = sorted(candidates)
        return helper(candidates, target)