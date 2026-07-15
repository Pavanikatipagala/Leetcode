class Solution(object):
    def makeConnected(self, n, connections):
        if  len(connections) < n-1:
            return -1
        parent=[i for i in range(n)]
        size = [1 for i in range(n)]
        count = n-1
        for u,v in connections:
            pu = self.find(u,parent)
            pv=  self.find(v,parent)

            if pu == pv:
                continue
            
            if size[pu] > size[pv]:
                parent[pv] = pu
            
            elif size[pv]>size[pu]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                size[pu]+=1
            
            count -=1
        return count 
    def find(self,x,parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x],parent)
        return parent[x]
        