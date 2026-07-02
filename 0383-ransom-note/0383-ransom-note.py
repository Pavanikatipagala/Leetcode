class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap={}
        for i in range(len(magazine)):
            if magazine[i] not in hashmap:
                hashmap[magazine[i]]=1
            else:
                hashmap[magazine[i]]+=1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in hashmap:
                return False
            else:

                hashmap[ransomNote[i]]-=1
            if hashmap[ransomNote[i]] < 0:
                return False
        return True  



        