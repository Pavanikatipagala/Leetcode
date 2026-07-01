class Solution(object):
    def runningSum(self, nums):
        ans=[]
        rsum=0
        for num in nums:
            rsum+=num
            ans.append(rsum)
        return ans