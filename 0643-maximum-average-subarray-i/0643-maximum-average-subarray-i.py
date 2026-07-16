class Solution(object):
    def findMaxAverage(self, nums, k):
        total_sum = 0
        l = 0 
        max_avg = float('-inf')
        for r in range(len(nums)):
            total_sum += nums[r]

            if  r-l+1 == k:
                avg = total_sum /float(k)
                max_avg = max(max_avg,avg)
                total_sum -=nums[l]
                l+=1
        return  max_avg
                
        

