class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_pivot_index(left, right):
            if(nums[left] < nums[right]):
                print(0)
                return 0
            while(left <= right):
                mid = int((left + right) / 2)
                if(nums[mid] > nums[mid + 1]):
                    print(mid)
                    return mid + 1
                else:
                    if(nums[mid] < nums[left]):
                        right = mid - 1
                    else:
                        left = mid + 1
        def search_index(left, right):
            while(left <= right):
                mid = int((left + right) / 2)
                if(nums[mid] == target):
                    return mid
                else:
                    if(target < nums[mid]):
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1
        
        length = len(nums)
        if(length == 0):
            return -1
        if(length == 1):
            return -1 if nums[0] != target else 0
        
        pivot_index = find_pivot_index(0, length - 1)
        if target == nums[pivot_index]:
            return pivot_index
        if pivot_index == 0:
            return search_index(0, length-1)
        if target < nums[0]:
            return search_index(pivot_index, length-1)
        else:
            return search_index(0, pivot_index)