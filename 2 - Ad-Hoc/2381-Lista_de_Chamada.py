"""
2381 - Lista de Chamada by myoshiro
"""

import random

#Método Particione
def MyRandomSplit (A,p,r):
    i = random.randrange(p,r)
    aux = A[i]
    A[i] = A[r]
    A[r] = aux
    return MySplit(A,p,r)    


#Método Particione Aleatorizado   
def MySplit(A,p,r):
    aux=""
    
    x = A[r] #x é o pivô
    i = p-1
    
    for j in range (p,r):
        if A[j] <= x:
            i+=1
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    
    aux = A[i+1]
    A[i+1] = A[r]
    A[r] = aux
    return i + 1

#Método QuickSort Aleatorizado   
def MyRandomQuickSort(A,p,r):
    
    if p < r:
        q = MyRandomSplit(A,p,r)
        MyRandomQuickSort(A,p,q-1)
        MyRandomQuickSort(A,q+1,r)
    
    return A
    

#Inicialização de variáveis
myIndex = 0
Input=[]

#Leitura da primeira linha (cabeçalho)
header=input().split(" ")
qty = int(header[0])
pos = int(header[1])

#Leitura das entradas (nomes de alunos)
for i in range(qty):
    Input.append(input())


#Invocação do método QuickSort Aleatorizado
MyRandomQuickSort(Input,0,len(Input)-1)

print(Input[pos-1])
