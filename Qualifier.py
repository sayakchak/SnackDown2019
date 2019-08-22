sum = 0
T = int(input())
if T>1000 or T<1:
    exit(0)
for i in range(T):
    N, K = [int(x) for x in input().split()]
    sum += N
    if K<1 or N<1 or K>N or K>100000 or N>100000 or sum>1000000:
        exit(0)
    S = [int(x) for x in input().split()]
    if min(S)<1 or max(S)>1000000000:
        exit(0)
    S.sort()
    S.reverse()
    score = S[K-1]
    c = 0
    for j in range(N-1, -1, -1):
        if S[j] == score:
            break
        c += 1
    print(N-c)
    