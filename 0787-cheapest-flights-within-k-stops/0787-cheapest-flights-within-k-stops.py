class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adjList = []

        for i in range(n):
            adjList.append([])

        for flight in flights:
            u, v, price = flight
            adjList[u].append([v, price])
        dist = [[float('inf')] * (k+2) for i in range(n)]
        dist[src][0] = 0

        queue=[]
        heapq.heappush(queue,(0,src,0))

        while queue:
            cost, city, flightsUsed = heapq.heappop(queue)
            if city == dst:
                return cost
            
            for nextCity,nextCost in adjList[city]:
                if flightsUsed == k+1:
                    continue

                if cost + nextCost< dist[nextCity][flightsUsed+1]:
                    dist[nextCity][flightsUsed+1] = cost + nextCost
                    heapq.heappush(queue,(cost + nextCost,nextCity,flightsUsed+1))
        return -1
                

                

