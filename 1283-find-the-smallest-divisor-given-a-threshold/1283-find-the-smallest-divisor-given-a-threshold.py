class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low+high)//2

            if self.isPossible(nums,threshold,mid):
                high  = mid -1
            else:
                low = mid+1
        return low

    def isPossible(self,nums,threshold,d):
        count = 0
        for num in nums:
            count += math.ceil(num/d)
        if count <= threshold:
            return True
        else:
            return False