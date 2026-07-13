class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent=[i for i in range(n)]
        rank =[0 for i in range(n)]


        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    self.union(i,j,parent,rank)
        province =0
        for  i in range(n):
            if self.find(i,parent)==i:
                province+=1
        return province
    def union(self,u,v,parent,rank):
        pu = self.find(u,parent)
        pv = self.find(v,parent)

        if pu==pv:
            return

            
        if rank[pu]>rank[pv]:
            parent[pv]=pu
        elif rank[pv]>rank[pu]:
            parent[pu]=pv
        else:
            parent[pv]=pu
            rank[pu]+=1
       
                    
    def find(self,x,parent):
        if parent[x]==x:
            return x
        parent[x] = self.find(parent[x],parent)
        return parent[x]

