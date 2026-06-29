class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
              return [hashmap[target - nums[i]], i]
            