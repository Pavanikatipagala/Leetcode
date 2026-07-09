class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjList = []
        for i in range(n):
            adjList.append([])

        for time in times:
            u,v,w = time
            adjList[u-1].append([v-1,w])
            
        dist = [float('inf')] * n
        dist[k-1] = 0
        
        queue=[]
        heapq.heappush(queue,(0,k-1))

        while queue:
            curr =  heapq.heappop(queue)
            weight= curr[0]
            node = curr[1]
            
            if weight > dist[node]:
                continue
            
            for neighbour in adjList[node]:
                neighNode = neighbour[0]
                neighWeight = neighbour[1]
                
                if weight + neighWeight < dist[neighNode]:
                    dist[neighNode]= weight+neighWeight
                    heapq.heappush(queue, (dist[neighNode], neighNode))
                     
        ans = max(dist)
        if ans== float('inf'):
            return -1
        return ans
            
          
        