#include<iostream>
#include<stdlib.h>
#include<vector>
#define L 1000000007
long long mul(long long a,long long b, long long mod){ 
    long long res = 0;  
    a %= mod; 
    while (b){
        if (b & 1) 
            res = (res + a) % mod; 
        a = (2 * a) % mod; 
        b >>= 1;  
    } 
    return res; 
} 
main(){
    std::ios::sync_with_stdio(0);
    std::cin.tie(NULL);
    int T, temp;
    long N, K, f,R, i;
    //unsigned long long out;
    short o;
    std::cin>>T;
    if (T<1||T>1000)
        exit(0);
    for (int t=0;t<T;t++){
        std::cin>>N>>K;
        if(N<1||K<1||N>1000000000||K>10000)
            exit(0);
        temp =  ((K-1)*(2+K))/2; //2..1+(K-1) summation
        //out = 1;
        o = 1;
        std::vector<long long> out;
        if (temp> (N-1) || N<K)
            o = -1;
        else if(temp == N-1)
            o = 0;
        else{
            f = N/K;
        R = N%K;
        std::vector<long> Z;
        if(N%K != 0){
            i = K/2;
            while (i>=1){
                Z.push_back(f-i);
                i -= 1;
            }
            if (K%2!=0)
                Z.push_back(f);
            for (i=1; i< K/2+1; i++)
                Z.push_back(f+i);
            if (K%2 ==0){
                i = K/2 - 1;
                while(R!=0 && i>=0){
                    Z[i] += 1;
                    i-=1;
                    R-=1;
                }
                i = K-1;
                while(R!=0){
                    Z[i] += 1;
                    i-=1;
                    R-=1;
                }
            }
            else{
                i = K-1;
                while (R!=0){
                    Z[i] += 1;
                    i-=1;
                    R-=1;
                }
            }
            for (unsigned long long a:Z){
                //std::cout<<a<<"\t";
                f = a%L;
                out.push_back(mul(f,f-1,L));//out *= ( ( f * ( (f -1) % L ) ) %L );
            }
        }
        else{
            i = (K/2);
            while (i>=1){
                out.push_back(mul(f-i,f-i-1,L));//out *= (((f-i)%L*(f-i-1)%L)%L);
                i -= 1;
            }
            if (K%2!=0)
                out.push_back( mul(f,f-1,L));
            for (i= 1; i< (K/2)+1; i++){
                
                out.push_back(mul((f+i),(f+i-1),L));//out *= (((f+i)%L*(f+i-1)%L)%L);
                //std::cout<<Z[i]<<"\t";
            }
        }
        }   
    
    if (o==-1||o==0)
        std::cout<<o<<"\n";
    else{
        long long x;
        long S = out.size();
        if (S==1)
            x = out[0]%L;
        else
            x = mul(out[0],out[1],L);
            for (i = 2;i<S;i++){
                x = mul(x,out[i],L);
            }
        
        std::cout<<x<<"\n";
    }
    }
    }
