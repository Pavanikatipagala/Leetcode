class Solution(object):
    def minAddToMakeValid(self, s):
        balance = 0
        moves = 0
        for i in s:
            if i=='(':
                balance+=1
            else:
                if balance>0:
                    balance -=1
                else:
                    moves+=1
        moves+=balance
        return moves
        