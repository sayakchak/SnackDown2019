T = int(input())
if T<1 or T>1000:
    exit(0)
for t in range (T):
    N,K = [int(x) for x in input().split()]
    if(N<1 or K<1 or N>10**9 or K>10**4):
        exit(0)
    out = -1
    temp = int( ( (K-1)*(2+K) ) /2)
    if temp>N-1:
        out = -1
    elif temp == N-1:
        out = 0
    else:
        R = N%K
        Q = int(N/K)
        Z = []
        if R == 0:#rem 0
            f = Q #the no
            if K%2 == 0:#even
                z = int(K/2)
                for i in range(z):
                    f+=1
                    Z.append(f)
                f = Q
                for i in range(z):
                    f-=1
                    Z.append(f)
            else:#odd
                z = int((K-1)/2)
                for i in range(z):
                    f+=1
                    Z.append(f)
                f = Q
                Z.append(f)
                for i in range(z):
                    f-=1
                    Z.append(f)
        else:#rem not 0
            Q = int((N-R)/K)
            f = Q
            if K%2 == 0:#even
                z = int(K/2)
                for i in range(z):
                    f+=1
                    Z.append(f)
                f = Q
                for i in range(z):
                    f-=1
                    Z.append(f)
            else:#odd
                z = int((K-1)/2)
                for i in range(z):
                    f+=1
                    Z.append(f)
                f = Q
                Z.append(f)
                for i in range(z):
                    f-=1
                    Z.append(f)
            Z.sort(reverse = 1)
            i = 0         
            while R!=0:
                Z[i] += 1
                i += 1
                R -= 1
        print(Z,sum(Z))