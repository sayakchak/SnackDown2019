#include<stdio.h>
#include<stdlib.h>
int main(){
    int T, t;
    long sum = 0, k, *ni, *mi, i, mul;
    scanf("%d",&T);
    if (T<1 || T>1000)
        exit(0);    
    for (t = 0; t<T; t++){
        scanf("%ld",&k);
        sum += k;
        if (k<1 || k>100000 || sum > 500000)
            exit(0);
        ni = (long*)malloc(k*sizeof(long));
        mi = (long*)malloc(k*sizeof(long));
        for (i = 0; i<k ; i++){
            scanf("%ld",&ni[i]);
            if (ni[i] < 0 || ni[i] > 100000000)
                exit(0);
        }
        for (i = 0; i<k ; i++){
            scanf("%ld",&mi[i]);
            if (mi[i] < 0 || mi[i] > 100000000)
                exit(0);
        }
        i=0;
        while ((i+2)<k){
            if (mi[i]!=ni[i]){
                if (mi[i] < ni[i])
                    break;
                else{
                    mul = mi[i] - ni[i];
                    ni[i] += (1*mul); ni[i+1] += (2*mul); ni[i+2] += (3*mul);
                }
            }
            i ++;
        }
        short flag = 1;
        for (i =0; i<k ;i++)
            if (mi[i]!=ni[i]){
                flag = 0;
                break;
            }
        if (flag == 1)
            printf("TAK\n");
        else
            printf("NIE\n");
    }
}