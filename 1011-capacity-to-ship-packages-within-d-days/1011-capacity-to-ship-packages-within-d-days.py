class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low+high)//2

            if self.isPossible(weights,days,mid):
                high = mid-1
            else:
                low = mid+1
        return low

    def isPossible(self,weights,days,lw):
        count = 1
        cur_sum =0
        for weight in weights:
            cur_sum +=weight

            if cur_sum >lw:
                count+=1
                cur_sum = weight
        return count<=days


        
