class Solution(object):
    def sortedSquares(self, nums):
        ans = [0] * len(nums)
        r = len(nums)-1
        l = 0 
        k = len(nums)-1
        while l<=r:

            if nums[l] **2 > nums[r]**2:
                ans[k]=nums[l]**2
                l+=1
            else:
                ans[k] = nums[r]**2
                r-=1
            k-=1
        return ans

