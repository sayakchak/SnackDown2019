import java.util.Scanner;
import java.util.Arrays;
//class fre{
//    int val;
//    fre no;
//}
class Main{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int T = s.nextInt();
        if (T<1 || T>1000)
            System.exit(0);
        int sum = 0;
        for (int i =0; i < T; i++){
            int N = s.nextInt();
            if (N%2 != 0 || N<2 || N>100000)
                System.exit(0);
            sum += N;
            if(sum>1000000)
                System.exit(0);
            int S[] = new int[N];
            for (int j = 0; j < N; j++){
                S[j] = s.nextInt();
                if (S[j]<1 || S[j]>1000000)
                    System.exit(0);
            }
            Arrays.sort(S);
            int freq[] = new int[N];
            /*int j = 0;
            while (j<N){
                System.out.println("Y");                
                int k = j;
                int frequency = 0;
                while (S[j]==S[k] && j<N){
                    frequency++;
                    System.out.println("x");
                    freq[k] = frequency;
                    k++;
                }
                j += (j-k);
            }*/
            int frequency = 1;
            freq[0] = frequency;
            for(int j= 1; j< N; j++){
                if (S[j-1]==S[j]){
                    frequency++;
                }
                else
                    frequency = 1;
                freq[j] = frequency;
            }
            for(int j= 1; j< N; j++){
                
            }
            /*for (int j = N-1; j>=0; j--)
                System.out.print(S[j]+" ");
            System.out.println();
            for (int j = N-1; j>=0; j--)
                System.out.print(freq[j]+" ");
            */  
            long f = 1;
            //for (int j = N-1; j>=0; j--)
            //    f*=freq[j];
            int top = 1;
            int j = N-1;
            while (j>0){
                if(top == 1){
                    if (freq[j]>1){
                        if (freq[j]>2){
                            if (freq[j]%2 == 0){
                                top = 0;
                            }
                            else{
                                top = 1;
                            }
                        }
                        else{
                            top = 0;
                        }
                    }
                    else{
                        top = 0;
                    }
                }
                else{
                    if(freq[j]==1){
                        top = 1;
                    }
                    else {
                        if (freq[j]>1){
                            if(freq[j]>2){
                                if(freq[j]%2==1){
                                    top = 1;
                                }
                                else
                                    top = 0;
                            }
                        else
                            top = 0;
                        }
                        else
                            top = 1;
                    }
                }
                f *= freq[j];
                j -= freq[j];
            }
            System.out.println(f%1000000007);
        }
    }
}
