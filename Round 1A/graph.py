def check(x):
    l  = len(x)
    for i in range 
T = int(input())
for z in range(T):
    N = int(input())
    a = [int(x) for x in input().split()]
    B = set(a)
    A = list(B)
    B = list(B)
    Lng = len(A)
    count = 0
    X = []
    for i in range(Lng):
        X.append(0)
    if Lng==1:
        count = 1
    else:
        L = len(A)
        for i in range(L-1):
            for j in range(i+1,L):
                if A[j]%A[i]!=0:
                    X[i] = 1
                    X[j] = 1 #1 means they are coprimes
        #t = []
        x = []
        for i in range (Lng):
            if X[i]==0:#not coprime
                x.append(A[i])
                #t.append(i) #index in original
        #print(x)
        #M = x[-1]
        for i in range (m,51):
            if i%m!=0:
                A[A.index(x[-1])] = i
                break
        check (x)


        

