"""
1177 - Array Fill II by myoshiro
"""

T = int(input())
N=list()
i=0

while len(N) < 1000:
    
    k=0
    
    while k < T and len(N) < 1000:
       N.append(k)
       print("N[" + str(i) + "] = " + str(k))
       i+=1
       k+=1
