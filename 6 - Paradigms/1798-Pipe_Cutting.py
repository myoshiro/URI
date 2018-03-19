In0 = input().split(" ")

n = int(In0[0])
c = int(In0[1])
tamanhos=[]
valores=[]

for i in range(0,n):
    In0 = input().split(" ")
    tamanhos.append(int(In0[0]))
    valores.append(int(In0[1]))


t = [0 for i in range(c+1)]
      
i = 0
j = 0


for i in range(c+1):
    
    for j in range(n):
        
        if tamanhos[j] <= i:
            
            t[i] = max(t[i], t[i-tamanhos[j]] + valores[j])
            
        j = j +1        

print(t[c])
