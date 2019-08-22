T = int(input())
if T<1 or T> 3*(10**4):
    exit(0)
for z in range(T):
    N = int(input())
    if N<1 or N>50:
        exit(0)
    a = [int(x) for x in input().split()]
    count = 0
    if (len(a)==1):
        count = 0
    else:
        A = list(set(a))
        if A[0]<2 or A[-1]>50:
            exit(0)
        L = len(A)
    
        X = []
        for i in range(L):
            X.append(0)
        if L==1:
            count = 1
            a[a.index(A[0])] = 47 if A[0]==47 else 17
        else:
            for i in range(L-1):
                for j in range(i+1,L):
                    if A[j]%A[i]!=0:
                        X[i] = 1
                        X[j] = 1 #1 means they are coprimes
            x = []
            M = 1
            for i in range (L):
                if X[i]==0:#not coprime
                    x.append(A[i])
                else:
                    M = A[i] if M<A[i] else M
            #print(x)
            if len(x) == 0:
                count = 0
            elif len(x) == 1:
                count = 1
                if (x[0]==50):
                    a[a.index(x[0])] = 49
                else:
                    for i in range (x[0],51):
                        if i%M != 0 and M%i !=0:
                            a[a.index(x[0])] = i
                            break 
            else:
                count = 1
                for i in range (x[0],51):
                    if i%x[-1] != 0 and x[-1]%i !=0:
                        a[a.index(x[-1])] = i
                        break
        print(count)
        for i in range (N):
            print(a[i], end = " ")
         

        
        

