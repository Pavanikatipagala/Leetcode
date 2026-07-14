class Solution(object):
    def accountsMerge(self, accounts):
        n =  len(accounts)
        parent =[i for i in range(n)]
        rank=[0] *n 
        email={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in email:
                    email[accounts[i][j]] = i
                else:
                    self.union(i,email[accounts[i][j]],parent,rank)
        merged = {}

        for mail in email:

            parentNode = self.find(email[mail], parent)

            if parentNode not in merged:
                merged[parentNode] = []

            merged[parentNode].append(mail)

        ans = []

        for node in merged:

            name = accounts[node][0]

            mails = sorted(merged[node])

            ans.append([name] + mails)

        return ans

    
    def find(self,x,parent):
        if parent[x] == x:
            return parent[x]
        parent[x] =  self.find(parent[x],parent)
        return parent[x]
    
    def union(self,u,v, parent,rank):
        pu = self.find(u,parent)
        pv = self.find(v,parent)

        if pu==pv:
            return
        
        if rank[pu]>rank[pv]:
            parent[pv] = pu
        elif rank[pv]>rank[pu]:
            parent[pu]= pv
        else:
            parent[pv]=pu
            rank[pu]+=1

