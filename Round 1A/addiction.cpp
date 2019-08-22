#include<bits/stdc++.h>
using namespace std;
main(){
    int t,T,A_1,B_1;
    long a,b,c,i,c_l;
    string A, B,x,y;
    scanf("%d",&T);
    if (T<1||T>1000)
        exit(0);
    for (t = 0;t<T;t++){
        scanf("%ld %ld %ld",&a,&b,&c);
        if (a<1 || b<1 || c<1 || a> 1000000000 || b>1000000000 || c> 1000000000 || ((a+b)!=c))
            exit(0);
        A = bitset<32>(a).to_string(); //conv to binary str
        B = bitset<32>(b).to_string();
        A_1 = count(A.begin(),A.end(),'1'); //count no 1s
        B_1 = count(B.begin(),B.end(),'1');
        c_l = 0;
        //cout<<A_1<<endl<<B_1<<endl;
        for (i=1;i<c;i++){ //for 5 ex 1+4, 2+2, 3+2, 4+1 (x+y)
            x = std::bitset<32>(i).to_string();
            y = std::bitset<32>(c-i).to_string();
            //cout<<x<<endl<<y<<endl;
            //cout<<x_1<<endl<<y_1<<endl;
            if (count(x.begin(),x.end(),'1') == A_1 && count(y.begin(),y.end(),'1') == B_1) //if no of 1 in x == no of 1 in A..
                c_l ++;
        }
        printf("%ld\n",c_l);
    }
}
