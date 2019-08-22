import java.util.Scanner;
import java.util.Arrays;
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
            int frequency = 1;
            freq[0] = frequency;
            for(int j= 1; j< N; j++){
                if (S[j-1]==S[j])
                    frequency++;
                else
                    frequency = 1;
                freq[j] = frequency;
            }
            long ans = 1;
            boolean top = true;
            boolean y = true;
            boolean n = false;
            int j = N-1;
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
                            top = y;
                        }
                        else{//ODD
                            top = n;
                            ans *= freq[i];
                        }
                        j -= freq[j]; //update
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
