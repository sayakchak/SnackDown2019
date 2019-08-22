#include<iostream>
#include<stdlib.h>
#include<vector>
#include<algorithm>
main(){
    std::ios::sync_with_stdio(0);
    std::cin.tie(NULL);
    long sum = 0;
    int T, t;
    long N,K,i,M,count,j,k,S;
    std::cin>>T;
    if (T<1||T>1000)
        exit(0);
    for (t=0;t<T;t++){
        std::cin>>N>>K;
        sum += N;
        if (K<1||N<1||K>100000||N>100000||sum>500000||K>N)
            exit(0);
        std::vector<long> L;
        std::vector<long> R;
        for(i = 0; i<N;i++){
            std::cin>>M>>count;
            if (1>M||1>count||M>count||M>1000000000||count>1000000000)
                exit(0);
            L.push_back(M);
            R.push_back(count);
        }
    std::sort(L.begin(),L.end());
    std::sort(R.begin(),R.end());
    j = 0; k = 0; count =0; 
    std::vector<long>start;
    std::vector<long>end;
    for (i = L[0];i<=R[N-1];i++){
        while(L[j]==i && j<N){
            count++;j++;
            if (count >= K){
                start.push_back(i);
                //std::cout<<"yy"<<i<<"\t";
            }
        }
        //std::cout<<count<<"\n";
        while(R[k]==i && k<N){
            count--;k++;
            if(count>= K-1){
                end.push_back(i);
                //std::cout<<"xx"<<i<<"\t";
            }
            S = start.size();
        }
    }
    M = 0;
    //std::reverse(end.begin(),end.end());
    //for (long a:start)
    //    std::cout<<a<<"\t";
    //std::cout<<"\n";
    //for(long a:end)
    //    std::cout<<a<<"\t";
    if (K%2==0)
        for(j=0;j<S;j++)
            M = std::max(M,end[j]-start[j]);
    else
        for(j=0;j<S;j++)
            M = std::max(M,end[S-j-1]-start[j]);
    std::cout<<M<<"\n";
    }
}