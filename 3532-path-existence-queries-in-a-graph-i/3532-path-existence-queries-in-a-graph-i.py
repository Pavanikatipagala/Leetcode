class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        parent =[i for i in range(n)]

        for i in range(1,n):
            if abs(nums[i]-nums[i-1]) <= maxDiff:
                self.union(i,i-1, parent)
        
        ans=[]
        for u, v in queries:
            ans.append(self.find(u,parent)== self.find(v,parent))
        return ans



    def find(self,x,parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x],parent)
        return parent[x]

    def union(self,u,v,parent):
        pu = self.find(u,parent)
        pv= self.find(v,parent)

        if pu==pv:
            return
        parent[pv] = pu

        