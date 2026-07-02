class Solution(object):
    def isAnagram(self, s, t):
        hashmap={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=1
            else:
                hashmap[s[i]]+=1
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]]-=1
            else:
                return False
        for value in hashmap.values():
            if value!=0:
                return False
        return True