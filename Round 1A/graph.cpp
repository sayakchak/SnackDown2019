#include<bits/stdc++.h>
using namespace std;
void check (int left[],int t[], int n, int c, int A[], int N,int X[]){
    int i, j, pivot, gcd;
    bool flag = 0;
    for(i = 0;i<n;i++)
        for(j = 0;j<n;j++)
            if( (left[i]%left[j] != 0) || (left[j]%left[i] != 0) ){
                //cout<<"gaysex"<<A[t[i]]<<A[t[j]];
                if (flag == 0){
                    gcd = __gcd(left[i],left[i]);
                    flag = 1;
                }
                X[t[i]] = 1;
                X[t[j]] = 1;
                pivot = t[i];
                gcd = __gcd(A[i],gcd);
            }
    //cout<<gcd<<endl<<A[pivot]<<endl;
    j = 0;
    flag = 0;
    for (i=0;i<N;i++)
        if(X[i] == 1){
            cout<<"bitch";
            if (flag == 0){//SHIFT
                for (j =2; j<=50;j++)
                    if ((j%gcd != 0) && (gcd%j != 0) && (j%A[pivot] != 0) && (A[pivot]%j != 0)){
                        A[i] = j; c+=1; break;
                    }
                flag = 1;
            }
            left[j] = A[i];  //nos left
            t[j] = i; //index of the no left
            j++;
            }
    cout<<endl<<"j="<<j<<endl;
    n = j+1;
    if (n>1){
        cout<<endl<<"n="<<n<<endl<<"left="<<left<<endl;
        check(left,t,n,c, A, N, X);
    }
    else{
        cout<<c<<"\n";
        for(i=0;i<N;i++)
            cout<<A[i]<<" ";
        cout<<"\n";
    }    
}
main(){
    int T, n, c,t[50], t2,N,A[50],X[50],left[50];
    cin>>T;
    for(t2= 0;t2<T;t2++){
        cin>>N;
        for (int i=0;i<N;i++){
            cin>>A[i];
            t[i] = i;
            X[i] = 0;
            left[i] = A[i];
        }
    n = N;
    c = 0;
    check(left,t,n,c, A,N,X);    
    }
}

