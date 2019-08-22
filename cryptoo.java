import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Dictionary;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.Set;
import java.util.TreeSet;
class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Program obj = new Program();
        Dictionary<Integer,Character> alphabets = new Hashtable<>(26);
        short T = Short.parseShort(in.readLine());
        int N,max =0,i;
        String output = "";
        String ip[] = new String[2];
        String lip[] = new String [100];
        int ll[] = new int[100];
        int n[] = new int[100];
        Pair [] prime_factor = new Pair[100];
        String l[];
        for(short test = 1;test<=T;test++){
            ip = in.readLine().split(" ");
            N = Integer.parseInt(ip[0]); ll[test]= Integer.parseInt(ip[1]);
            if(N>max) max = N;
            lip[test] = in.readLine();
            n[test] = N;
        }
        boolean sieve[] = obj.siev(max);
        for (short test = 1; test<=T;test++){
            l = lip[test].split(" ");
            for (i=0;i<ll[test];i++) prime_factor[i] = obj.prime_fact( Integer.parseInt(l[i]),sieve );
            for (i=0;i<ll[test]-1;i++){
                if (prime_factor[i].a == prime_factor[i+1].a){
                    prime_factor[i].a = prime_factor[i].b;
                    prime_factor[i].b = prime_factor[i+1].a;
                }
                else if (prime_factor[i].a == prime_factor[i+1].b){
                    prime_factor[i].a = prime_factor[i].b;
                    prime_factor[i].b = prime_factor[i+1].b;
                    prime_factor[i+1].b = prime_factor[i+1].a;
                    prime_factor[i+1].a = prime_factor[i].b;                    
                }
                else if (prime_factor[i].b == prime_factor[i+1].b){
                    prime_factor[i+1].b = prime_factor[i+1].a;
                    prime_factor[i+1].a = prime_factor[i].b;    
                }
                else{
                    //pass
                }
            }
            Set <Integer> s = new HashSet<Integer>(26);
            for (i=0;i<ll[test];i++){
                for(i=0;i<ll[test];i++) {
                    s.add(prime_factor[i].a);
                    s.add(prime_factor[i].b);
                }
                
            }
            TreeSet <Integer> ss = new TreeSet<Integer>();
            ss.addAll(s);
            int count = 0;
            for (Integer var : ss) {
                alphabets.put(var, (char)(count+65));
                count++;
                //System.out.println(var);
            }
            //System.out.println(Arrays.asList(alphabets));
            output+="\nCase #"+test+" : ";
            for(i=0;i<ll[test];i++){
                output+=alphabets.get(prime_factor[i].a);
            }
            output+=alphabets.get(prime_factor[ll[test]-1].b);
            //System.out.println(Arrays.asList(alphabets));
            //for(i=0;i<ll[test];i++) System.out.print("xxx"+prime_factor[i].a+"xxx"+prime_factor[i].b+"xxx\n");
        }
        System.out.println(output);        
    }
    
}
class Pair{
    int a,b;
    Pair(int x, int y){
        a = x; b = y;
    }
}
class Program{
    boolean[] siev(int n){
        int i,temp;
        boolean primes [] = new boolean[n+1];
        for (i=2;i<=n;i++){
            if (!primes[i]){
                temp = 2*i;
                while(temp<=n){
                    primes[temp] = true;
                    temp += i;
                }
            }
        }
        return primes;
    }
    Pair prime_fact(int n,boolean[] primes){
        Pair p = new Pair(0,0);
        for(int i=3;i<=(int)Math.sqrt(n);i++){
            if (!primes[i] && n%i ==0 && !primes[n/i]){
                p = new Pair(i,n/i);
                break;
            }
        }
        return p;
    }
}






















