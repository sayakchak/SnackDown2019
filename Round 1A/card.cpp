#include<iostream>
#include<stdlib.h>
using namespace std;
main(){
    bool flag;
    int T, j;
    long i, t, N, sum = 0,s=0, min;
    long *A, *B;
    string x;
    cin>>T;
    if (T<1||T>100)
        exit(0);
    for (j =0 ; j<T;j++){
        cin>>N;
        sum += N;
        if (N<2 || N> 100000 || sum > 1000000)
            exit(0);
        A = new long[N];
        B = new long[N];
        min = 1000000001;
        for (i=0;i<N;i++){
            cin>>A[i];
            if(A[i]<1||A[i]>1000000000)
                exit(0);
            if (A[i]<min){
                min = A[i];
                s = i;
            }
        }
        flag = 1;
        for (i=s,t=0;i<N;i++,t++)
            B[t] = A[i];
        for (i=0;i<s;i++,t++)
            B[t] = A[i];
        for (i=0;i<N-1;i++)
            if((B[i+1]-B[i])<0){
                flag = 0;
                break;
            }
        if (flag==1)
            x = "YES";
        else   
            x = "NO";
        cout<<x<<endl;    
    }
}
