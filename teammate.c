#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
main(){
    int T;
    long N, *S, *freq, sum = 0, j, t; 
    scanf("%d",&T);
    if(T<0||T>1000)
        exit(0);
    while(T>0){
        long ans = 1;
        T--;
        scanf("%ld",&N);
        if (N%2 != 0 || N<2 || N>100000)
            exit(0);
        sum += N;
        if(sum>1000000)
            exit(0);
        S = (long*)malloc(N*sizeof(long));
        freq = (long*)malloc(N*sizeof(long));
        for (j = 0; j < N; j++){
                scanf("%ld",&S[j]);
                if (S[j]<1 || S[j]>1000000)
                    exit(0);
            }
        qsort(S, N, sizeof(long), cmpfunc);
        long frequency = 1;
        freq[0] = frequency;
            for(j= 1; j< N; j++){
                if (S[j-1]==S[j])
                    frequency++;
                else
                    frequency = 1;
                freq[j] = frequency;
            }
        bool top = 1;
        bool y = 1;
        bool n = 0;
        j = N - 1;
        while(j>=0){
                if (freq[j] ==1 ){ //NO REP
                    if(top == y)
                        top = n;
                    else
                        top = y; //changing flag
                    j--; //update
                }
                else{//REP
                    if (top == n){
                        ans *= freq[j];
                        j--;
                        top = y;
                    }
                    else{
                        if(freq[j]%2 ==0){//EVEN
                            t = freq [j];
                            while(t!=0){
                                ans *= ((t*(t-1))/2);
                                t -= 2;
                            }
                            top = y;
                            j -= freq[j]; //update
                        }
                        else{//ODD
                            t = freq [j];
                            while(t!=1){
                                ans *= ((t*(t-1))/2);
                                t -= 2;
                            }
                            top = y;
                            j -= freq[j]+1; //update
                        }
                        
                    }
                }
            }
        printf("%ld\n",(ans%1000000007));        
    }
}
            