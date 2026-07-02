class Solution(object):
    def majorityElement(self, nums):
        hashmap={}
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        for key , value in hashmap.items():
            if value>(n/2):
                return key
            
        