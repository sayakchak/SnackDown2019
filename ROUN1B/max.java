//import java.math.BigInteger; 
import java.util.Scanner; 
import java.lang.System;
import java.util.ArrayList;
public class Main{
    public static void main(String[] args) {
    int T, temp;
    int N, K, f,R, i;
    long out;
    long L = 1000000007;
    short o;
    Scanner s = new Scanner(System.in);
    T = s.nextInt();
    if (T<1||T>1000)
        System.exit(0);
    for (int t=0;t<T;t++){
        if(N<1||K<1||N>1000000000||K>10000)
            System.exit(0);
        temp =  ((K-1)*(2+K))/2; //2..1+(K-1) summation
        out = 1;
        o = 1;
        if (temp> (N-1) || N<K)
            o = -1;
        else if(temp == N-1)
            o = 0;
        else{
            f = N/K;
        R = N%K;
        ArrayList<Integer> Z = new ArrayList<>();
        if(N%K != 0){
            i = K/2;
            while (i>=1){
                Z.add(f-i);
                i -= 1;
            }
            if (K%2!=0)
                Z.add(f);
            for (i=1; i< K/2+1; i++)
                Z.add(f+i);
            if (K%2 ==0){
                i = K/2 - 1;
                while(R!=0 && i>=0){
                    //Z[i] += 1;
                    Z.set(i,Z.get(i)+1);
                    i-=1;
                    R-=1;
                }
                i = K-1;
                while(R!=0){
                    Z.set(i,Z.get(i)+1);
                    //Z[i] += 1;
                    i-=1;
                    R-=1;
                }
            }
            else{
                i = K-1;
                while (R!=0){
                    Z.set(i,Z.get(i)+1);
                    //Z[i] += 1;
                    i-=1;
                    R-=1;
                }
            }
            for (int x = 0;x<K;x++){
                System.out.print(a+" ");
                f = a%L;
                out *= ( ( f * ( (f -1) % L ) ) %L );
            }
        }
        else{
            i = (K/2);
            while (i>=1){
                out *= (((f-i)%L*(f-i-1)%L)%L);
                i -= 1;
            }
            if (K%2!=0)
                out *= (((f)%L*(f-1)%L)%L);
            for (i= 1; i< (K/2)+1; i++){
                out *= (((f+i)%L*(f+i-1)%L)%L);
                //std::cout<<Z[i]<<"\t";
            }
        }
        }   
    
    if (o==-1||o==0)
        System.out.println(o);
    else
        System.out.println(out);
    }
    }
}
