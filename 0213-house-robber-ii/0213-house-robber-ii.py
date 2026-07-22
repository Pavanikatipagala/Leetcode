class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        arr1 = nums[:-1]
        arr2 = nums[1:]

        dp1 = [-1] * len(arr1)
        dp2 = [-1] * len(arr2)

        ans1 = self.solve(len(arr1)-1,arr1,dp1)
        ans2 = self.solve(len(arr2)-1,arr2,dp2)

        return max(ans1,ans2)

    def solve(self,index,arr,dp):
        if index == 0:
            return arr[0]
        
        if index < 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]

        pick = arr[index] + self.solve(index - 2, arr, dp)

        notPick = self.solve(index - 1, arr, dp)

        dp[index] = max(pick, notPick)

        return dp[index]
