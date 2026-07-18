class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0
        prefix =[0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        for i in range(len(prefix)):
            if i==0:
                left_sum = 0
            else:
                left_sum = prefix[i-1]
            right_sum = prefix[n-1] - prefix[i]


            if left_sum == right_sum:
                return i
        return -1
