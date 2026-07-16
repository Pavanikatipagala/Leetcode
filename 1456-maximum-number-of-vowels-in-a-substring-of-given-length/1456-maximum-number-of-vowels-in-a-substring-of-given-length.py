class Solution(object):
    def maxVowels(self, s, k):
        vowels=['a','e','i','o','u']
        left = 0
        count = 0
        ans=0
        for right in range(len(s)):
            if s[right] in vowels:
                count +=1
            if right-left+1 == k:
                ans = max(ans,count)

                if s[left] in vowels:
                    count-=1
                left +=1
        return ans
                

        