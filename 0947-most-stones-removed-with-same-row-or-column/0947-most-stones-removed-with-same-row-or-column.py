class Solution(object):
    def removeStones(self, stones):
        n =  len(stones)
        parent=[i for i in range(n)]
        rank= [0 for i in range(n)]
        
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1]== stones[j][1]:
                    self.union(i,j, parent,rank)
        
        no_stones=0
        for i in range(n):
            if self.find(i,parent) == i:
                no_stones+=1
        return n-no_stones
    

    def find(self,x,parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x],parent)
        return parent[x]

    def union(self,u,v,parent,rank):
        pu = self.find(u,parent)
        pv= self.find(v,parent)

        if pu == pv:
            return
        if rank[pu]>rank[pv]:
            parent[pv] = pu
        elif rank[pv]>rank[pu]:
            parent[pu]=pv
        else:
            parent[pv]=pu
            rank[pu] +=1
        
