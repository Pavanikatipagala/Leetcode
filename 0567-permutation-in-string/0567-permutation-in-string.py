class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq ={}
        for ch in s1:
            freq[ch] = freq.get(ch,0)+1
        count = len(freq)
        left = 0

        for right in range(len(s2)):
            if s2[right] in freq :
                freq[s2[right]] -=1

                if freq[s2[right]] == 0:
                    count -=1
            
            if right-left+1 > len(s1):
                if s2[left] in freq:
                    
                    if freq[s2[left]] == 0:
                        count += 1
                    
                    freq[s2[left]] += 1

                left += 1
            if count == 0: return True
        return False