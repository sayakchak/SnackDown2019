L = 10**9+7
T =0
temp = 0
f = 0
R = 0
i = 0
out = 0
T = int(input())
if (T<1 or T>1000):
        exit(0)
for t in range(T):
    N,K=[int(X) for X in input().split()]
    if(N<1 or K<1 or N>1000000000 or K>10000):
            exit(0)
    temp =  int(((K-1)*(2+K))/2); 
    out = 1
    if temp> (N-1):
        out = -1
    elif temp == N-1:
        out = 0
    else:
        f = int(N/K)
        R = N%K
        Z = []
        if(N%K != 0):
            i = int(K/2)
            while i>=1:
                Z.append(f-i)
                i -= 1
            if (K%2!=0):
                Z.append(f)
            for i in range (1,int(K/2)+1):
                Z.append(f+i)
            if (K%2 ==0):
                i = int(K/2) - 1
                while(R!=0 and i>=0):
                    Z[i] += 1
                    i-=1
                    R-=1
                i = K-1
                while(R!=0):
                    Z[i] += 1
                    i-=1
                    R-=1
            else:
                i = K-1
                while (R!=0):
                    Z[i] += 1
                    i-=1
                    R-=1
            for a in Z:
                print(a)
                f = a%L
                out *= ( ( f * ( (f -1) % L ) ) %L )
        else:
            i = int(K/2)
            while i>=1:
                out *= (((f-i)%L*(f-i-1)%L)%L)
                i -= 1
            if (K%2!=0):
                out *= (((f)%L*(f-1)%L)%L)
            for i in range (1,int(K/2)+1):
                out *= (((f+i)%L*(f+i-1)%L)%L)
                #print(Z)    
    if (out==-1 or out==0):
        print(out)
    else:
        print(out%L)
        