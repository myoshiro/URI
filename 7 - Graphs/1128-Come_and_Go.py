"""
1128 - Come and Go by myoshiro
"""

def myDFS(i, count, ret, o, adj):
    
    if ret[i] != -1:
        return ret[i]
    
    count += 1 
    o[i] = count 
    ret[i] = o[i]

    for j in range(0, len(adj[i])):
        
        aux0 = ret[i]
        aux1 = myDFS(adj[i][j], count, ret, o, adj)
        
        if type(aux1) == type([]):
            aux1 = aux1[0]
        
        ret[i] = min(aux0, aux1)
    
    return ret[i]

#################################################
#################################################

ret=[None for x in range(0,2000)]
o  =[None for x in range(0,2000)]
adj=[None for x in range(0,2000)]


In0 = input().split(" ")

while In0 != ["0","0"]:
    
    N = int(In0[0])
    M = int(In0[1])
    
    count = 0
    
    for i in range(0,N):
        ret[i] = -1
        o[i] = -1
        adj[i] = []

    for i in range (0, M):
        In1 = input().split(" ")
        V = int(In1[0])
        W = int(In1[1])
        P = int(In1[2])
        
        adj[V-1].append((W-1))
        
        if (P==2):
            adj[W-1].append(V-1)
    
    myDFS(0, count, ret, o, adj)
    
    aux3 = 1
    
    while aux3 < N and o[aux3] > ret[aux3]:
        aux3 += 1
           
    if aux3 >= N:
        print(1)
    else:
        print(0)

    In0 = input().split(" ")
