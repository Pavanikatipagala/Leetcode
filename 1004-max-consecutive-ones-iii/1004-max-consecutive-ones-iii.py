class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left =0
        max_length = float('-inf')
        num_zeros = 0
        if len(nums) == k:
            return k
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -=1
                left +=1
            length = right - left + 1
            max_length = max(max_length, length)
        return max_length

