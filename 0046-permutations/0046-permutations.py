class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr =[]
        visited =[False] * len(nums)
        self.backTrack(0,visited,nums,curr,result)
        return result

    def backTrack(self,index,visited,nums,curr,result):
        if len(curr) == len(nums):
            result.append(curr.copy())

        if index >= len(nums):
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            curr.append(nums[i])
            visited[i] = True
            self.backTrack(index+1,visited,nums,curr,result)
            curr.pop()
            visited[i] = False