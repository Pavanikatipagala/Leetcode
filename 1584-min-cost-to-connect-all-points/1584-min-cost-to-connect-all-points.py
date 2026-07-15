class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        parent = [i for i in range(n)]
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                edges.append([i,j,abs(x1-x2)+abs(y1-y2)])
        edges.sort(key = lambda x:x[2])
        cost = 0
        count= 0
        for u,v,w in edges:
            pu = self.find(u,parent)
            pv = self.find(v,parent)
            if pu != pv:
                self.union(u,v,parent)
                cost += w
                count +=1
            if count == n-1:
                break
        return cost


    def find(self,x,parent):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent[x],parent)
        return parent[x]
        
    def union(self,u,v, parent):
        pu = self.find(u,parent)
        pv = self.find(v,parent)
        
        if pu==pv:
            return 
        parent[pv] = pu
        
        

                