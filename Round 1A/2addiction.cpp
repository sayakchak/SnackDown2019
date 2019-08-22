#include<stdio.h>
#include<algorithm>
#include<string>
#include<bitset>
main(){
    int t,T,A_1,B_1;
    long a,b,c,i,c_l;
    scanf("%d",&T);
    if (T<1||T>1000)
        exit(0);
    for (t = 0;t<T;t++){
        scanf("%ld %ld %ld",&a,&b,&c);
        if (a<1 || b<1 || c<1 || a> 1000000000 || b>1000000000 || c> 1000000000 || ((a+b)!=c))
            exit(0);
        std::bitset<30>A(a); //conv to binary str
        std::bitset<30>B(b);
        A_1 = A.count(); //count no 1s
        B_1 = B.count();
        c_l = 0;
        //cout<<A_1<<endl<<B_1<<endl;
        for (i=1;i<c;i++){ //for 5 ex 1+4, 2+2, 3+2, 4+1 (x+y)
            std::bitset<30>x(i);
            std::bitset<30>y(c-i);
            //cout<<x<<endl<<y<<endl;
            //cout<<x_1<<endl<<y_1<<endl;
            if (x.count() == A_1 && y.count() == B_1) //if no of 1 in x == no of 1 in A..
                c_l ++;
        }
        printf("%ld\n",c_l);
    }
}
