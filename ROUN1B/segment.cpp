#include<iostream>
#include<stdlib.h>
#include<vector>
#include<algorithm>
main(){
    std::ios::sync_with_stdio(0);
    std::cin.tie(NULL);
    int T, t;
    long N,K,i,M,count,j,k,S;
    std::cin>>T;
    if (T<1||T>1000)
        exit(0);
    for (t=0;t<T;t++){
        std::cin>>N>>K;
        std::vector<long> L;
        std::vector<long> R;
        for(i = 0; i<N;i++){
            std::cin>>M>>count;
            L.push_back(M);
            R.push_back(count);
        }
    std::sort(L.begin(),L.end());
    std::sort(R.begin(),R.end());
    j = 0; k = 0; count =1; 
    std::vector<long>start;
    std::vector<long>end;
    for (i = L[0];i<=R[N-1];i++){
        while(L[j]==i && j<N){
            count++;j++;
            if (count > K){
                start.push_back(i);
                //std::cout<<start<<"\t";
            }
        }
        while(R[k]==i && k<N){
            count--;k++;
            if(count==K){
                end.push_back(i);
                //std::cout<<end<<"\t";
            }
            S = start.size();
        }
    }
    M = 0;
    for (long a:start)
        std::cout<<a<<"\t";
    std::cout<<"\n";
    for(long a:end)
        std::cout<<a<<"\t";
        /*for(j=0;j<S;j++)
        M = std::max(M,end[S-j]-start[j]);*/
    }
    std::cout<<M<<"\n";
    
}