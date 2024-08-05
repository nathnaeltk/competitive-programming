class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        term =set()  
        n =len(graph)
        d1=defaultdict(int)
        for i in range(n):
            c=0
            for j in graph[i]:
                c+=1
                d[j].append(i) 
            d1[i]=c
            if c==0: 
                term.add(i)
        
        
        ans =[]
        ret=[]
        
        q=list(term)
        while(q):
            x=q.pop(0)
            for node in d[x]:
                if node not in term:
                    d1[node]-=1 
                    if d1[node]==0:
                        q.append(node)
                        term.add(node)
        ans =list(term)
        ans.sort()
        return ans     