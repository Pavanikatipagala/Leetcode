class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <=  high:
            mid = (low+high)//2

            if self.isPossible(mid,piles,h):
                high = mid-1
            else:
                low =  mid+1
        return low
    
    def isPossible(self,speed,piles,h):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)
        if hours <= h:
            return True
        else:
            return False
        