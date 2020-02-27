class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, key = lambda x:x)
        ans = 0
        sum_ans = sum(nums)
        print(sum_ans)
        length = len(nums)
        diff = sum_ans % 3
        if(diff == 0):
            return sum_ans
        mod_1 = []
        mod_2 = []
        for i in range(0, length - 1):
            if(len(mod_1) >= 2 and len(mod_2) >= 2):
                break
            if(nums[i] % 3 == 1):
                mod_1.append(nums[i])
                # if(diff == 1):
                    # break
                continue
            if(nums[i] % 3 == 2):
                mod_2.append(nums[i])
                # if(diff == 2):
                    # break
                continue
        print(mod_1)
        print(mod_2)
        length_mod1 = len(mod_1)
        length_mod2 = len(mod_2)
        if(diff == 1):
            if(length_mod1 >= 1 and length_mod2 >= 2):
                return max(sum_ans - mod_1[0], sum_ans - sum(mod_2[0:2]))
            elif(length_mod1 >= 1):
                return sum_ans -mod_1[0]
            elif(length_mod2 >= 2):
                return sum_ans - sum(mod_2[0:2])
            else:
                return 0
        if(diff == 2):
            if(length_mod2 >= 1 and length_mod1 >= 2):
                return max(sum_ans - mod_2[0], sum_ans - sum(mod_1[0:2]))
            elif(length_mod2 >= 1):
                return sum_ans - mod_2[0]
            elif(length_mod1 >= 2):
                return sum_ans - sum(mod_1[0:2])
            else:
                return 0