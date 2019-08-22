# cook your dish here
N, Q = [int(x) for x in input().split()]
if N<1 or Q<1 or N>2*10**5 or Q>2*10**5:
    exit(0)
A = [int(x) for x in input().split()]
if min(A) < 0 or max(A)>10**9:
    exit(0)
m =0
for q in range (Q):
    B = {}
    B[0] = A
    K,X = [int(x) for x in input().split()]
    if K<0 or X<1 or K>10**9 or X>N:
        exit(0)
    if X == N:
        print(A[-1])
    else:
        if K not in B:
            #print(m)
            #temp = B[m]
            for t in (m+1,K+1):
                print(t)
                t_2 = []
                for i in range (N-1):
                    x1 = B[t-1][i]
                    x2 = B[t-1][i+1]
                    t_2.append(x1^x2)
                t_2.append(A[-1])
                B[t] = t_2
                m = K
            print(B)    
        print (B[K][X-1])
