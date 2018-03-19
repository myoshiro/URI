"""
1152 - Dark Roads by myoshiro
"""
from collections import defaultdict
 
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices
        self.graph = [] 
         
  
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
#################################################
#       KRUSKAL
#################################################
    def myKruskal(self):
        
        global min_cost
        
        result =[] 
 
        i = 0 
        e = 0 
 
        self.graph =  sorted(self.graph,key=lambda item: item[2])
 
        parent = [] ; rank = []
 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        while e < self.V -1 :
 
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            if x != y:
                e = e + 1  
                result.append([u,v,w])
                self.union(parent, rank, x, y)

        for u,v,weight  in result:
            min_cost = min_cost + weight
            


In0 = input().split(" ")

while In0 != ["0","0"]:
    
    full_cost = 0
   
    V       =   int(In0[0])
    E       =   int(In0[1])

    G       = Graph(V)

    for i in range (0, E):
        In1 = input().split(" ")

        From = int(In1[0])
        To = int(In1[1])
        w = int(In1[2])
        
        full_cost = full_cost + w
        
        G.addEdge(From, To, w)
    
    min_cost = 0    
    G.myKruskal()
    
    print(full_cost - min_cost)
 
    In0 = input().split(" ")
