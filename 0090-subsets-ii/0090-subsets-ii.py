class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr =[]
        nums.sort()
        self.backTrack(0,nums,curr,result)
        return result

    def backTrack(self,index,nums,curr,result):
        result.append(curr.copy())
        for i in range(index,len(nums)):
            if i > index and  nums[i] == nums[i-1]:
                continue
        
            curr.append(nums[i])
            self.backTrack(i+1,nums,curr,result)
            curr.pop()