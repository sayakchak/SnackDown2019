T = int(input())
if T<1 or T>1000:
    exit(0)
sum = 0
for t in range (T):
    M1 = []
    M2 = []
    L = []
    R = []
    P = []
    N,K = [int(x) for x in input().split()]
    sum += N
    if K<1 or N<1 or K>10**5 or N>10**5 or sum>(5 * 10**5) or K>N:
        exit(0)
    for i in range(N):
        a,b = [int(x) for x in input().split()]
        M1.append(a)
        M2.append(b)
        if 1>a or 1>b or a>b or a>10**9 or b>10**9:
            exit(0)
        L.append(a)
        R.append(b)
    L.sort()
    R.sort()
    j = 0
    k = 0
    for i in range (2*N):
        if k<N and j<N:
            if R[k]>L[j]:
                t = [L[j],"S"]
                P.append(t)
                j+=1
            else:
                ind = M2.index(R[k])
                t = [R[k],"E",M1[ind]]
                del(M1[ind])
                del(M2[ind])
                P.append(t)
                k+=1
        elif j<N and k>=N:
            t = [L[j],"S"]
            P.append(t)
            j+=1
        else:
            ind = M2.index(R[k])
            t = [R[k],"E",M1[ind]]
            del(M1[ind])
            del(M2[ind])
            P.append(t)
            k+=1
    print(P)
    count = 0
    dis = 0
    curr = []
    dict = {}
    for i in range(2*N):
        if P[i][1] == 'S':
            count+=1
            curr.append(P[i][0])
            dict.setdefault(P[i][0],[]) #creates a key iff the key doesn't already exist
            dict[P[i][0]].append(count)
        else:
            count -= 1
            if count>= K-1:
                dis = max(dis, P[i][0]-curr[-1])
                print(curr)
                print(dis)
                x = curr.index(P[i][2])
                for j in dict[curr[x]]:
                    if j>=K:
                        if P[i][0]-j>dis:
                            dis = P[i][0] - j
                            del[dict[curr[x]][dict[curr[x]].index(j)]]
                del(curr[x])
    print(dict)
