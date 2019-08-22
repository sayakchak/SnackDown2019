#include<iostream>
#include<stdlib.h>
#include<vector>
#define L 1000000007
void check(long f, long K, std::vector<long> & Z){
    for (long i= K/2 ;i>=1;i--)
        //std::cout<<(f-i)<<"\n";
        Z.push_back(f-i);
    if (K%2!=0)
        //std::cout<<f<<"\n";
        Z.push_back(f);
    for (long i=1 ;i<=K/2;i++)
        //std::cout<<(f+i)<<"\n";
        Z.push_back(f+i);
}
main(){
    std::ios::sync_with_stdio(0);
    std::cin.tie(NULL);
    int T, temp;
    long N, K, out, f,R, i;
    std::cin>>T;
    if (T<1||T>1000)
        exit(0);
    for (int t=0;t<T;t++){
        std::cin>>N>>K;
        if(N<1||K<1||N>1000000000||K>10000)
            exit(0);
        temp =  ((K-1)*(2+K))/2; //2..1+(K-1) summation
        out = 1;
        if (temp> (N-1))
            out = -1;
        else if(temp == N-1)
            out = 0;
        else{
            f = N/K;
            R = N%K;
            std::vector<long> Z;
            check(f,K,Z);
            /**if (N%K ==0){//No rem
                if (N%2 ==0){//even
                    check(f,K,Z);
                }
                else{//odd
                    check(f,K,Z);
                }
            }*/
            if(N%K != 0){//Rem
                if (N%2 ==0){//even
                    i = K/2 - 1;
                    while(R!=0 || i!=0){
                        Z[i] += 1;
                        i--;
                        R--;
                    }
                    i = K-1;
                    while(R!=0){
                        Z[i] += 1;
                        i--;
                        R--;
                    }
                }
                else{//odd
                    i = K-1;
                    while(R!=0){
                        Z[i] += 1;
                        i--;
                        R--;
                    }
                }
            }
            //std::cout<<sizeof(Z)/sizeof(long);
            for(auto a : Z)
                std::cout<<a<<"\t";
        }
        if (out==-1||out==0)
            std::cout<<out<<"\n";
        else
            std::cout<<(out%L)<<"\n";
    }
}