// 1976 - Matrices by myoshiro

#include<stdio.h>
#include<limits.h>
#include <iostream>
using namespace std;

int num;
string msg;
int out0;


void PrintOptimalParens(unsigned long s[][1001],int i,int j)
{
   if(i==j){
      msg = msg +"A" + to_string(num);
      num++;}
   else
   {
      msg = msg +"(";
      PrintOptimalParens(s,i,s[i][j]);
      PrintOptimalParens(s,s[i][j]+1,j);
      msg = msg +")";
   }
}
 
void MatrixChainOrder(int *p, int n)
{
 
   unsigned long m[1001][1001]={0};
   unsigned long s[1001][1001]={0};
   unsigned int q;
 
    int i, j, k, l;
 

    for(l = 2; l <= n ;l++)
  {
       for(i = 1 ; i <= n - l +1 ; i++)
      {
        j = i + l -1;
          m[i][j] = INT_MAX;
          for(k=i ; k < j ; k++)
         {
             q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
             if(q < m[i][j])
             {
                 m[i][j] = q;
                 s[i][j] = k;
            }
          }
       }
   }
   

    num=1;
    PrintOptimalParens(s,1,n);
    out0 = m[1][n];

}




int main()
{
   int n;
   int p[1001];
   int i;
   int aux1, aux2;
   int In;
   bool check1;
   //int out[2];
  
  check1 = false;

  cin >> In;

   while (In != 0){
     
     for (i=0; i < In; i++){
        int ind = i;

        cin >> aux1 >> aux2;
        p[ind] = aux1;
     
        if (In-1 == i){p[ind+1] = aux2;}
     
     }

    
     n = In;

     MatrixChainOrder(p,n);
     
     for (i=0;i<n;i++) {
       
       if (p[i] == p[i+1])
          check1 = true;
       
     }
     
     if (check1)
        cout <<  out0;
     else
        cout <<  msg;
     
     cout << "\n";    
     msg="";
    
    check1 = false;
    cin >> In;

     }

   return 0;
}
